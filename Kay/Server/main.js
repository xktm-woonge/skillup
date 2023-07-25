const net = require('net');
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const registerController = require('./controller/register_controller');

const tcpPort = 8000;
const httpPort = 3000;

const tcpServer = net.createServer();
const app = express();
const httpServer = http.createServer(app);
const io = socketIo(httpServer);

let userSessions = {}; // 사용자 세션 정보를 저장하는 객체

tcpServer.on('connection', (socket) => {
    let userId = socket.id;  // Set the userId as the socket's ID
    userSessions[userId] = { socket: socket, environment: 'PC' };

    socket.on('data', (data) => {
        let message = JSON.parse(data);  // Parse the JSON string
        let command = message.command;  // Access the command property
        
        switch (command) {
            case 'VERIFICATIONCODE':
                registerController.handleVerificationCodeRequest(message, userSessions[userId]);
                break;
            case 'VERIFY':
                authController.handleVerify(message, userSessions[userId]);
                break;
            case 'REGISTER':
                authController.handleRegister(message, userSessions[userId]);
                break;
            case 'LOGIN':
                authController.handleLogin(message, userSessions[userId]);
                break;
            default:
                console.log('Unknown command:', command);
                break;
        }
    });

    socket.on('end', () => {
        console.log('Client disconnected');
        delete userSessions[userId];
    });

    socket.on('error', (err) => {
        console.log('Socket error:', err);
    });
});

// io.on('connection', (socket) => {
//     let userId = ...;
//     userSessions[userId] = { socket: socket, environment: 'Web' };
    
//     socket.on('message', (message) => {
//         let command = message.split(' ')[0];
//         switch (command) {
//             case 'VERIFICATIONCODE':
//                 authController.handleVerificationCodeRequest(message, userSessions[userId]);
//                 break;
//             case 'VERIFY':
//                 authController.handleVerify(message, userSessions[userId]);
//                 break;
//             case 'REGISTER':
//                 authController.handleRegister(message, userSessions[userId]);
//                 break;
//             case 'LOGIN':
//                 authController.handleLogin(message, userSessions[userId]);
//                 break;
//             default:
//                 console.log('Unknown command:', command);
//                 break;
//         }
//     });

//     socket.on('disconnect', () => {
//         console.log('User disconnected');
//         delete userSessions[userId];
//     });
// });

tcpServer.listen(tcpPort, () => {
    console.log(`TCP Server listening on port ${tcpPort}`);
});

// httpServer.listen(httpPort, () => {
//     console.log(`HTTP Server listening on port ${httpPort}`);
// });
