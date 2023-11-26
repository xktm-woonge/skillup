// ./controller/conversations_controller.js

const dbManager = require('../model/dbManager');
const websocketFormatter = require('../utils/websocketFormatter');

exports.handleConversations = function(data, ws, callback) {
    const user_email = data.info.user_email;
    const target_email = data.info.email;
    const name = data.info.name;
    const imagePath = data.info.image_path;

    let response = {
        conversationId: null,
        isNewConversation: false,
        name: name,
        email: target_email,
        imagePath: imagePath
    };

    // user_email을 통해 userId를 찾습니다.
    dbManager.getUserIdByEmail(user_email, (userIdErr, userId) => {
        if (userIdErr) return callback(userIdErr);

        // userId를 사용하여 대화방 참여 여부를 확인합니다.
        dbManager.getConversationByUserId(userId, (convErr, conversation) => {
            if (convErr) return callback(convErr);

            if (conversation) {
                // 대화방이 이미 존재하는 경우
                response = {
                    conversationId: conversation.id,
                    isNewConversation: false,
                    name: name,
                    email: target_email,
                    imagePath: imagePath
                };
            } else {
                // 대화방이 존재하지 않는 경우
                dbManager.createConversation('chatting_name', (createErr, newConversationId) => {
                    if (createErr) return callback(createErr);

                    // 대화방 참여자를 추가합니다.
                    dbManager.addParticipantToConversation(newConversationId, user_email, target_email, (addErr) => {
                        if (addErr) return callback(addErr);

                        response = {
                            conversationId: newConversationId,
                            isNewConversation: true,
                            name: name,
                            email: target_email,
                            imagePath: imagePath
                        };
                    });
                });
            }

            // 클라이언트에게 응답을 전송합니다.
            const formattedResponse = websocketFormatter.formatWebSocket(
                'SUCCESS',
                'conversations',
                response.isNewConversation ? 'New conversation created successfully.' : 'Existing conversation found.',
                response
            );
            ws.send(JSON.stringify(formattedResponse));
        });
    });
};



exports.handleSendMessage = function(data, wss, callback) {
    const sender_email = data.info.sender_email;
    const conversation_id = data.info.conversation_id;
    const target_email = data.info.email;
    const message_text = data.info.message_text;

    // 대상 사용자의 대화방 존재 여부를 확인하고, 없으면 생성합니다.
    dbManager.checkAndCreateConversation(conversation_id, [sender_email, target_email], (checkErr, updatedConversationId) => {
        if (checkErr) return callback(checkErr);

        // 메시지를 데이터베이스에 저장합니다.
        dbManager.addMessageToConversation(updatedConversationId, sender_email, message_text, (addErr) => {
            if (addErr) return callback(addErr);

            // 대상 사용자의 상태를 확인합니다.
            dbManager.getUserStatus(target_email, (statusErr, targetStatus) => {
                if (statusErr) return callback(statusErr);

                if (targetStatus === 'online') {
                    // 상대방이 온라인 상태인 경우 메시지를 전송합니다.
                    wss.clients.forEach(client => {
                        if (client.user_email === target_email && client.readyState === WebSocket.OPEN) {
                            client.send(JSON.stringify({ event: 'newMessage', data: { conversationId: updatedConversationId, sender_email, message_text }}));
                        }
                    });
                }
            });
        });
    });
};