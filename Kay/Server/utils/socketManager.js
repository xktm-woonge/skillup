const socketIo = require('socket.io');
let io = null;

exports.initialize = (server) => {
    io = socketIo(server);
    return io;
};

exports.getIO = () => {
    if (!io) {
        throw new Error("Socket.io not initialized!");
    }
    return io;
};