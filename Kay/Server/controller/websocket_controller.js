// ./controller/websocket_controller.js

const notificationsController = require('./notifications_controller');
const socketManager = require('../utils/socketManager');
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
                    notificationsController.handleFriendResponse(data.user_id, data.sender_id, data.response, (err) => {
                        if (err) {
                            console.error('Error deleting notification:', err);
                            // 필요한 경우 클라이언트에게 오류 메시지를 전송할 수 있습니다.
                        } else {
                            console.log('Notification deleted successfully');
                            // 필요한 경우 클라이언트에게 성공 메시지를 전송할 수 있습니다.
                        }
                    });
                    break;
                case 'sendMessage':
                    wss.clients.forEach(client => {
                        if (client.readyState === WebSocket.OPEN) {
                            client.send(JSON.stringify({ event: 'newMessage', data: data.data }));
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
