// ./controller/websocket_controller.js

const dbManager = require('../model/dbManager');
const notificationsController = require('./notifications_controller');
const socketManager = require('../utils/socketManager');

let io;

function ensureIOInitialized() {
    if (!io) {
        io = socketManager.getIO();
    }
}

exports.initializeWebsocketListeners = function() {
    ensureIOInitialized();

    io.on('connection', (socket) => {
        const user_id = socket.handshake.query.user_id;
        console.log('A user connected with user_id:', user_id);

        // 친구 요청 이벤트 처리
        socket.on('sendFriendRequest', (data) => {
            notificationsController.handleFriendRequest(data, user_id, socket);
        });

        // 채팅 메시지 이벤트 처리
        socket.on('sendMessage', (data) => {
            io.emit('newMessage', data);
        });

        // 사용자 상태 변경 이벤트 처리
        socket.on('changeStatus', (status) => {
            io.emit('statusChanged', { user_id, status });
        });

        // 추가적인 웹소켓 이벤트 처리는 여기에...
    });
};

exports.sendRealtimeMessage = function(user_id, data) {
    ensureIOInitialized();
    io.to(user_id).emit(data.event, data.payload);
};

// 다른 함수들도 여기에 추가할 수 있습니다...
