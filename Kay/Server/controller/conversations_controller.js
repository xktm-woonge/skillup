// ./controller/conversations_controller.js

// dbManager와 다른 필요한 모듈들을 require로 불러옵니다.
const dbManager = require('../model/dbManager');
const websocketFormatter = require('../utils/websocketFormatter');

exports.handleConversations = function(data, ws, callback) {
    const user_email = data.info.user_email;
    const target_email = data.info.email;
    const name = data.info.name;
    const imagePath = data.info.image_path;

    // 응답 객체 초기화
    let response = {
        conversationId: null,
        isNewConversation: false,
        name: name,
        email: target_email,
        imagePath: imagePath
    };

    // 대화방이 존재하는지 확인합니다.
    dbManager.getConversationByEmail(user_email, target_email, (err, conversation) => {
        if (err) return callback(err);

        if (conversation) {
            // 대화방이 이미 존재하는 경우
            response.conversationId = conversation.id;
        } else {
            // 대화방이 존재하지 않는 경우
            dbManager.createConversation(target_email, (createErr, newConversationId) => {
                if (createErr) return callback(createErr);

                // 대화방 참여자를 추가합니다.
                dbManager.addParticipantToConversation(newConversationId, user_email, (addErr) => {
                    if (addErr) return callback(addErr);

                    response.conversationId = newConversationId;
                    response.isNewConversation = true;
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
};
