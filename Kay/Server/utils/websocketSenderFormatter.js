exports.formatNotification = function(notificationData) {
    return {
        type: 'notification',
        data: notificationData,
        timestamp: new Date().toISOString()
    };
};