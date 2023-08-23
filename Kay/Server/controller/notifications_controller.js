// ./controller/notifications_controller.js

const dbManager = require('../model/dbManager');
const websocketController = require('./websocket_controller');

exports.handleFriendRequest = function(data, senderId, socket) {
    const receiverId = data.friendId; // The ID of the user to whom the friend request is being sent

    // Insert the friend request into the Notifications table
    dbManager.insertFriendRequestNotification(senderId, receiverId, (error) => {
        if (error) {
            console.error("Error inserting friend request notification:", error);
            return socket.emit('friendRequestError', 'Failed to send friend request.');
        }

        // Send the friend request as a realtime notification to the receiving user
        const notification = {
            type: 'FRIEND_REQUEST',
            content: 'You have received a new friend request!',
            sender_id: senderId
        };
        websocketController.sendRealtimeMessage(receiverId, notification);

        socket.emit('friendRequestSuccess', 'Friend request sent successfully.');
    });
};
