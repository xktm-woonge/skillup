// ./controller/notifications_controller.js

const dbManager = require('../model/dbManager');
const socketManager = require('../utils/socketManager');
const websocketSenderFormatter = require('../utils/websocketSenderFormatter');
const io = socketManager.getIO();

exports.initializeNotificationListeners = function() {
    io.on('connection', (socket) => {
        
        const user_id = socket.handshake.query.user_id;

        dbManager.getNotificationsForUser(user_id, (error, notifications) => {
            if (error) {
                console.error("Error fetching notifications:", error);
                return;
            }

            socket.emit('notifications', notifications);
        });
    });
};

exports.sendRealtimeNotification = function(user_id, notification) {
    const formattedNotification = websocketSenderFormatter.formatNotification(notification);
    io.to(user_id).emit('new_notification', formattedNotification);
};
