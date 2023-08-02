// ./model/emailService.js

const nodemailer = require('nodemailer');

exports.sendEmail = function(email, verificationCode, callback) {
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

    transporter.sendMail(mailOptions, callback);
}