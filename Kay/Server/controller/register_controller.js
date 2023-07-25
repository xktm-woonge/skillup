const nodemailer = require('nodemailer');

function generateVerificationCode() {
    return Math.floor(100000 + Math.random() * 900000).toString();  // 6자리 랜덤 숫자 생성
}

exports.handleVerificationCodeRequest = function (message, session) {
    const email = message['info']['email'];

    const verificationCode = generateVerificationCode();

    // Configure your email transport options here
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@example.com',
            pass: 'your-password'
        }
    });

    const mailOptions = {
        from: 'your-email@example.com',
        to: email,
        subject: '채팅 프로그램 인증번호',
        text: `Your verification code is ${verificationCode}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        let response;
        if (error) {
            response = 'VERIFICATIONCODE FAIL';
        } else {
            // If the email was sent successfully, store the verification code in the user's session
            session.verificationCode = verificationCode;
            response = 'VERIFICATIONCODE SUCCESS';
        }
        session.socket.write(response);
    });
}
