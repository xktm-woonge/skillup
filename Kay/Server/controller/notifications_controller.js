// ./controller/notifications_controller.js

const dbManager = require('../model/dbManager');
const websocketConnectionsManager = require('../utils/websocketConnectionsManager');
const config = require('../config/config.js');
const websocketFormatter = require('../utils/websocketFormatter');

const serverAddr = config.serverAddr;
const httpPort = config.httpPort;


exports.handleFriendRequest = function(user_email, sender_email, socket) {
    // 먼저 사용자와 발신자의 ID를 조회
    dbManager.getUserIdByEmail(user_email, (error, userId) => {
        if (error || !userId) {
            console.error("Error finding user ID:", error);
            socket.send(JSON.stringify(websocketFormatter.formatWebSocket('FAIL', 'notifications', 'userLookupError')));
            return;
        }

        dbManager.getUserIdByEmail(sender_email, (error, senderId) => {
            if (error || !senderId) {
                console.error("Error finding sender ID:", error);
                socket.send(JSON.stringify(websocketFormatter.formatWebSocket('FAIL', 'notifications', 'senderLookupError')));
                return;
            }

            // notifications 테이블에서 해당 항목 조회
            dbManager.checkNotificationExists(userId, senderId, (checkErr, exists) => {
                if (checkErr) {
                    console.error("Error checking notification existence:", checkErr);
                    return;
                }

                if (!exists) {
                    // notifications 테이블에 데이터 추가
                    dbManager.insertFriendRequestNotification(userId, senderId, (insertErr) => {
                        if (insertErr) {
                            console.error("Error inserting friend request notification:", insertErr);
                            return;
                        }

                        // 사용자가 온라인 상태인지 확인
                        dbManager.getUserStatus(user_email, (statusErr, userStatus) => {
                            if (statusErr) {
                                console.error("Error getting user status:", statusErr);
                                return;
                            }

                            if (userStatus === 'online') {
                                // 온라인 상태일 경우 사용자에게 알림 전송
                                const notificationData = {
                                    sender_email: sender_email,
                                    created_at: new Date().toISOString() // 현재 시간을 ISO 형식으로 설정
                                };

                                // 대상 사용자의 웹소켓 연결 찾기
                                const targetSocket = websocketConnectionsManager.getConnection(user_email);
                                if (targetSocket) {
                                    targetSocket.send(JSON.stringify(websocketFormatter.formatWebSocket('SUCCESS', 'notifications', 'friendRequest', notificationData)));
                                }
                            }
                        });
                    });
                }
            });
        });
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
                            socket.send(JSON.stringify(websocketFormatter.formatWebSocket('SUCCESS', 'notifications', 'friendResponseSuccess', senderInfo )));
                            const targetSocket = websocketConnectionsManager.getConnection(sender_email);
                                if (targetSocket) {
                                    targetSocket.send(JSON.stringify(websocketFormatter.formatWebSocket('SUCCESS', 'notifications', 'friendResponseSuccess', senderInfo)));
                                }
                        });
                    });
                }
            });
        });
    });
};
