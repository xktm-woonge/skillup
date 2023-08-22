// ./main.js

const express = require('express');
const http = require('http');
const socketManager = require('./utils/socketManager');

const config = require('./config/config.js');
const notificationsController = require('./controller/notifications_controller');

const app = express();
const server = http.createServer(app); // 이 부분은 변경 없음
const io = socketManager.initialize(server);  // Socket.io 초기화
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

io.on('connection', (socket) => {
  const user_id = socket.handshake.query.user_id;
  socket.join(user_id);
  console.log('A user connected');

  // 기존의 chat message 이벤트 리스너
  socket.on('chat message', (msg) => {
      io.emit('chat message', msg);
  });

  // 공지사항 이벤트 리스너 추가
  socket.on('send notification', (notification) => {
      io.emit('notification', notification);
  });

  socket.on('disconnect', () => {
      console.log('A user disconnected');
  });
});

notificationsController.initializeNotificationListeners(io);

server.listen(httpPort, () => {
    console.log(`HTTP Server listening on port ${httpPort}`);
    // notificationService.startNotificationService();  // 추가
});
