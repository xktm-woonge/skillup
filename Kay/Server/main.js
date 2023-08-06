const express = require('express');
const app = express();
const config = require('./config/config.js');
const httpPort = config.httpPort;

// 정적 파일 제공
app.use('/profile_picture', express.static(__dirname + '/images'));

// JSON 미들웨어
app.use(express.json());

// 라우터 설정
const authRouter = require('./model/auth_router');
app.use('/auth', authRouter);

app.listen(httpPort, () => {
    console.log(`HTTP Server listening on port ${httpPort}`);
});