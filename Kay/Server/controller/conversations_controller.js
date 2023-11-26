// ./controller/conversations_controller.js

const dbManager = require('../model/dbManager');
const websocketFormatter = require('../utils/websocketFormatter');

exports.handleConversations = function(data, ws, callback) {
    const user_email = data.info.user_email;
    const target_email = data.info.email;
    const name = data.info.name;
    const imagePath = data.info.image_path;

    // 두 사용자의 userId 조회
    dbManager.getUserIdByEmail(user_email, (userIdErr, userId) => {
        if (userIdErr) return callback(userIdErr);

        dbManager.getUserIdByEmail(target_email, (targetUserIdErr, targetUserId) => {
            if (targetUserIdErr) return callback(targetUserIdErr);

            // 대화방 존재 여부 확인
            dbManager.checkConversationExistence(userId, targetUserId, (convExistErr, conversation) => {
                if (convExistErr) return callback(convExistErr);

                if (conversation) {
                    // 대화방이 존재하는 경우
                    const response = {
                        conversationId: conversation.conversation_id,
                        isNewConversation: false,
                        name: name,
                        email: target_email,
                        imagePath: imagePath
                    };

                    // 클라이언트에게 응답 전송
                    sendResponse(ws, 'SUCCESS', 'Existing conversation found.', response);
                } else {
                    // 대화방이 존재하지 않는 경우, 새 대화방 생성
                    dbManager.createConversation('chatting_name', (createErr, newConversationId) => {
                        if (createErr) return callback(createErr);

                        dbManager.addParticipantToConversation(newConversationId, userId, targetUserId, (addErr) => {
                            if (addErr) return callback(addErr);

                            const response = {
                                conversationId: newConversationId,
                                isNewConversation: true,
                                name: name,
                                email: target_email,
                                imagePath: imagePath
                            };

                            // 클라이언트에게 응답 전송
                            sendResponse(ws, 'SUCCESS', 'New conversation created successfully.', response);
                        });
                    });
                }
            });
        });
    });
};

function sendResponse(ws, status, message, data) {
    const formattedResponse = websocketFormatter.formatWebSocket(status, 'conversations', message, data);
    ws.send(JSON.stringify(formattedResponse));
}


exports.handleSendMessage = function(data, wss, callback) {
    const sender_email = data.info.sender_email;
    const conversation_id = data.info.conversation_id;
    const target_email = data.info.email;
    const message_text = data.info.message_text;

    // sender_email을 통해 sender의 userId를 가져옵니다.
    dbManager.getUserIdByEmail(sender_email, (err, senderUserId) => {
        if (err) return callback(err);

        // 메시지를 데이터베이스에 저장합니다.
        dbManager.addMessageToConversation(conversation_id, senderUserId, message_text, (addMessageErr) => {
            if (addMessageErr) return callback(addMessageErr);

            // target_email을 통해 상대방의 userId를 가져옵니다.
            dbManager.getUserIdByEmail(target_email, (getUserErr, targetUserId) => {
                if (getUserErr) return callback(getUserErr);

                // 대화방 존재 여부 확인
                dbManager.checkConversationExistence(conversation_id, targetUserId, (checkErr, exists) => {
                    if (checkErr) return callback(checkErr);

                    if (!exists) {
                        // 대화방이 존재하지 않는 경우, 새로운 대화방 참여자를 추가합니다.
                        dbManager.addParticipantToConversation(conversation_id, targetUserId, senderUserId, (addParticipantErr) => {
                            if (addParticipantErr) return callback(addParticipantErr);
                        });
                    }

                    // 상대방의 상태 확인
                    dbManager.getUserStatus(target_email, (statusErr, targetStatus) => {
                        if (statusErr) return callback(statusErr);

                        if (targetStatus === 'online') {
                            // 상대방이 온라인 상태인 경우, 메시지를 전송합니다.
                            wss.clients.forEach(client => {
                                if (client.user_email === target_email && client.readyState === WebSocket.OPEN) {
                                    client.send(JSON.stringify({ event: 'newMessage', data: { conversationId: conversation_id, sender_email, message_text }}));
                                }
                            });
                        }
                    });
                });
            });
        });
    });
};
