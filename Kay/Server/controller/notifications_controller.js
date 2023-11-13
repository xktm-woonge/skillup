// ./controller/notifications_controller.js

const dbManager = require('../model/dbManager');
const websocketController = require('./websocket_controller');
const responseFormatter = require('../utils/responseFormatter');

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

exports.handleFriendResponse = function(user_id, senderId, action, socket) {
    // 알림 삭제
    dbManager.deleteNotification(user_id, senderId, (error) => {
        if (error) {
            console.error("Error deleting notification:", error);
            // 실패 응답
            // socket.send(JSON.stringify({ event: 'friendResponseError', message: 'Failed to process friend response.' }));
            socket.send(JSON.stringify(responseFormatter.formatResponse('FAIL', 'friendResponseError')));
            return;
        }
        if (action == 'accepted') {
            // 친구 추가 로직 (예시)
            dbManager.addFriend(user_id, senderId, (addFriendError) => {
                if (addFriendError) {
                    console.error("Error adding friend:", addFriendError);
                    // 실패 응답
                    // socket.send(JSON.stringify({ event: 'addFriendError', message: 'Failed to add friend.' }));
                    socket.send(JSON.stringify(responseFormatter.formatResponse('FAIL', 'addFriendError')));
                    return;
                }

                // 성공 응답
                // socket.send(JSON.stringify({ event: 'friendResponseSuccess', message: 'Friend response processed successfully.' }));
                socket.send(JSON.stringify(responseFormatter.formatResponse('FAIL', 'friendResponseSuccess')));
            });
        }
    });
};