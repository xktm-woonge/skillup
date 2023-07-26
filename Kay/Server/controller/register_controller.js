const nodemailer = require('nodemailer');
const logger = require('../utils/logger');

function generateVerificationCode() {
    return Math.floor(100000 + Math.random() * 900000).toString();  // 6자리 랜덤 숫자 생성
}

exports.handleVerificationCodeRequest = function (message, session) {
    logger.info(`message: ${message}, session: ${session}`)
    const email = message['info']['email'];

    const verificationCode = generateVerificationCode();

    // Configure your email transport options here
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'endteamchat@gmail.com',
            pass: 'fxerdbpuijwurack'
        }
    });

    const mailOptions = {
        from: 'endteamchat@gmail.com',
        to: email,
        subject: '채팅 프로그램 인증번호',
        text: `Your verification code is ${verificationCode}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        let response;
        if (error) {
            response = {command: 'VERIFICATIONCODE' , status: 'FAIL',  message: '이메일 전송에 실패했습니다.'};
        } else {
            session.verificationCode = verificationCode;
            response = {command: 'VERIFICATIONCODE' , status: 'SUCCESS',  message: '이메일 전송에 성공했습니다.'};
        }

        logger.info(`response: ${JSON.stringify(response)}`);
        session.socket.write(JSON.stringify(response));
    });    
}
