// ./controller/websocket_controller.js

const notificationsController = require('./notifications_controller');
const conversationsController = require('./conversations_controller');
const socketManager = require('../utils/socketManager');
const dbManager = require('../model/dbManager');
const url = require('url');

let wss;

function ensureWSSInitialized() {
    if (!wss) {
        wss = socketManager.getWSS();
    }
}

exports.initializeWebsocketListeners = function() {
    ensureWSSInitialized();

    wss.on('connection', (ws, req) => {
        const queryObject = url.parse(req.url, true).query;
        const user_id = queryObject.user_id;
        
        if (user_id) {
            console.log('A user connected with user_id:', user_id);
        } else {
            console.log('A user connected, but user_id is missing.');
        }

        ws.on('message', (message) => {
            let data = JSON.parse(message);
            switch (data.event) {
                case 'sendFriendRequest':
                    notificationsController.handleFriendRequest(data, user_id, ws);
                    break;
                case 'sendFriendResponse':
                    // sendFriendResponse 이벤트 처리
                    // 여기서 data 객체는 필요한 정보를 담고 있어야 합니다.
                    // 예를 들어, user_id와 sender_id가 필요합니다.
                    notificationsController.handleFriendResponse(data.info.user_id, data.info.sender_id, data.info.response, ws, (err) => {
                        if (err) {
                            console.error('Error deleting notification:', err);
                            // 필요한 경우 클라이언트에게 오류 메시지를 전송할 수 있습니다.
                        } else {
                            console.log('Notification deleted successfully');
                            // 필요한 경우 클라이언트에게 성공 메시지를 전송할 수 있습니다.
                        }
                    });
                    break;
                case 'makeConversation':
                    conversationsController.handleConversations(data, ws, (err) => {
                        if (err) {
                            console.error('Error makeConversation:', err);
                            // 필요한 경우 클라이언트에게 오류 메시지를 전송할 수 있습니다.
                        } else {
                            console.log('makeConversation successfully');
                            // 필요한 경우 클라이언트에게 성공 메시지를 전송할 수 있습니다.
                        }
                    });
                    break;
                case 'sendMessage':
                    conversationsController.handleSendMessage(data, wss, (err) => {
                        if (err) {
                            console.error('Error in sendMessage:', err);
                            // 필요한 경우 오류 메시지 전송
                        }
                    });
                    break;
                case 'changeStatus':
                    wss.clients.forEach(client => {
                        if (client.readyState === WebSocket.OPEN) {
                            client.send(JSON.stringify({ event: 'statusChanged', data: { user_id, status: data.data } }));
                        }
                    });
                    break;
                // 추가적인 웹소켓 이벤트 처리는 여기에...
            }
        });

        ws.on('close', () => {
            console.log('User disconnected', user_id);
            // 연결이 끊어지면 사용자 상태를 offline으로 변경
            dbManager.updateUserStatus(user_id, 'offline', (error, results) => {
                if (error) {
                    console.error('Failed to update user status to offline:', error);
                } else {
                    console.log(`User status for user_id ${user_id} updated to offline.`);
                }
            });
        });
    });
};

exports.sendRealtimeMessage = function(user_id, data) {
    ensureWSSInitialized();
    wss.clients.forEach(client => {
        if (client.user_id === user_id && client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(data));
        }
    });
};

// 다른 함수들도 여기에 추가할 수 있습니다...
