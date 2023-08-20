// ./services/notificationService.js

const dbManager = require('../model/dbManager');
const notificationsController = require('../controller/notificationsController');

exports.startNotificationService = function() {
    // 주기적으로 DB를 조회하여 새로운 알림이 있는지 확인
    setInterval(() => {
        dbManager.getLatestNotifications((error, notifications) => {
            if (error) {
                console.error("Error fetching latest notifications:", error);
                return;
            }

            notifications.forEach(notification => {
                const user_id = notification.user_id;
                notificationsController.sendRealtimeNotification(user_id, notification);
            });
        });
    }, 1000);  // 매 1초마다 실행
};
