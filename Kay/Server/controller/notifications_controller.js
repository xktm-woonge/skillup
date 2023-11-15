// ./controller/notifications_controller.js

const dbManager = require('../model/dbManager');
const websocketController = require('./websocket_controller');
const responseFormatter = require('../utils/responseFormatter');
const config = require('../config/config.js');
const websocketFormatter = require('../utils/websocketFormatter');

const serverAddr = config.serverAddr;
const httpPort = config.httpPort;


exports.handleFriendRequest = function(data, senderId, socket) {
    const receiverId = data.friendId; // The ID of the user to whom the friend request is being sent

    // Insert the friend request into the Notifications table
    dbManager.insertFriendRequestNotification(senderId, receiverId, (error) => {
        if (error) {
            console.error("Error inserting friend request notification:", error);
            return socket.emit('friendRequestError', 'Failed to send friend request.');
        }

        // Send the friend request as a realtime notification to the receiving user
        const notification = {
            type: 'FRIEND_REQUEST',
            content: 'You have received a new friend request!',
            sender_id: senderId
        };
        websocketController.sendRealtimeMessage(receiverId, notification);

        // socket.emit 대신 socket.send 사용
        socket.send(JSON.stringify({ event: 'friendRequestSuccess', message: 'Friend request sent successfully.' }));
    });
};

exports.handleFriendResponse = function(user_email, sender_email, action, socket) {
    // 먼저 사용자와 발신자의 ID를 조회
    dbManager.getUserIdByEmail(user_email, (error, userId) => {
        if (error || userId == null) {
            console.error("Error finding user ID:", error);
            socket.send(JSON.stringify(websocketFormatter.formatWebSocket('FAIL', 'notifications', 'userLookupError')));
            return;
        }

        dbManager.getUserIdByEmail(sender_email, (error, senderId) => {
            if (error || senderId == null) {
                console.error("Error finding sender ID:", error);
                socket.send(JSON.stringify(websocketFormatter.formatWebSocket('FAIL', 'notifications', 'senderLookupError')));
                return;
            }

            // 알림 삭제
            dbManager.deleteNotification(userId, senderId, (error) => {
                if (error) {
                    console.error("Error deleting notification:", error);
                    socket.send(JSON.stringify(websocketFormatter.formatWebSocket('FAIL', 'notifications', 'friendResponseError')));
                    return;
                }
                if (action == 'accepted') {
                    // 친구 추가 로직
                    dbManager.addFriend(userId, senderId, (addFriendError) => {
                        if (addFriendError) {
                            console.error("Error adding friend:", addFriendError);
                            socket.send(JSON.stringify(websocketFormatter.formatWebSocket('FAIL', 'notifications', 'addFriendError')));
                            return;
                        }

                        // 사용자 정보 조회
                        dbManager.getSenderByEmail(sender_email, (error, senderInfo) => {
                            if (error || !senderInfo) {
                                console.error("Error retrieving sender information:", error);
                                socket.send(JSON.stringify(websocketFormatter.formatWebSocket('FAIL', 'notifications', 'senderInfoError')));
                                return;
                            }

                            // 프로필 이미지를 URL로 변경
                            const profileImageUrl = `http://${serverAddr}:${httpPort}/profile_picture/${senderInfo.profile_picture}`;
                            senderInfo['profile_picture'] = profileImageUrl

                            // 성공 응답 및 사용자 정보 반환
                            socket.send(JSON.stringify(websocketFormatter.formatWebSocket('SUCCESS', 'notifications', 'friendResponseSuccess', { senderInfo })));
                        });
                    });
                }
            });
        });
    });
};
