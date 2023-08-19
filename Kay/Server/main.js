// ./main.js

const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const config = require('./config/config.js');

const app = express();
const server = http.createServer(app); // 이 부분은 변경 없음
const io = socketIo(server); // 이 부분은 변경 없음
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

// app.listen 대신 server.listen을 사용하여 서버 시작
server.listen(httpPort, () => {
    console.log(`HTTP Server listening on port ${httpPort}`);
});

io.on('connection', (socket) => {
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