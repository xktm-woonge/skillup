// ./controller/websocket_controller.js

const notificationsController = require('./notifications_controller');
const socketManager = require('../utils/socketManager');

let wss;

function ensureWSSInitialized() {
    if (!wss) {
        wss = socketManager.getWSS();
    }
}

exports.initializeWebsocketListeners = function() {
    ensureWSSInitialized();

    wss.on('connection', (ws, req) => {
        const user_id = req.url.split('=')[1];
        console.log('A user connected with user_id:', user_id);

        ws.on('message', (message) => {
            let data = JSON.parse(message);
            switch (data.event) {
                case 'sendFriendRequest':
                    notificationsController.handleFriendRequest(data, user_id, ws);
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
