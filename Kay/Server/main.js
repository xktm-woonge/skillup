// ./main.js

const express = require('express');
const http = require('http');
const socketManager = require('./utils/socketManager');
const websocketController = require('./controller/websocket_controller');

const config = require('./config/config.js');

const app = express();
const server = http.createServer(app);
const httpPort = config.httpPort;

// 정적 파일 제공
app.use('/profile_picture', express.static(__dirname + '/images'));

// JSON 미들웨어
app.use(express.json());

// 라우터 설정
const router = require('./model/router');
app.use('', router);

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// 웹소켓 초기화 및 이벤트 리스너 설정
socketManager.initialize(server);
websocketController.initializeWebsocketListeners();

server.listen(httpPort, () => {
    console.log(`HTTP Server listening on port ${httpPort}`);
    // notificationService.startNotificationService();  // 추가 (만약 필요하다면)
});
