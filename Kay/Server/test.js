const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

io.on('connection', (socket) => {
    console.log('Client connected');

    // Echo back messages from the client
    socket.on('message', (data) => {
        console.log('Received:', data);
        socket.emit('message', 'Echo: ' + data);
    });
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
