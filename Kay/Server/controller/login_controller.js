// login_controller.js

const dbManager = require('../model/dbManager');
const logger = require('../utils/logger');
const { hashPassword } = require('../utils/security');

exports.handleLogin = function(message, session) {
    const email = message['info']['email'];
    const password = message['info']['password'];

    dbManager.getUserByEmail(email, (error, user, fields) => {
        let response;
        if (error) {
            response = {command: 'LOGIN', status: 'FAIL', message: '로그인에 실패했습니다.'};
            session.socket.write(JSON.stringify(response));
        } else if (!user) {
            response = {command: 'LOGIN', status: 'UNREGISTERED', message: '존재하지 않는 계정입니다.'};
            session.socket.write(JSON.stringify(response));
        } else {
            const salt = user.salt;
            const hashedPassword = hashPassword(password, salt);

            if (hashedPassword === user.password) {
                response = {
                    command: 'LOGIN',
                    status: 'SUCCESS',
                    message: '로그인에 성공했습니다.',
                    profile_img_url: user.profile_img_path  // Add profile_img_url to the response
                };
            } else {
                response = {command: 'LOGIN', status: 'FAIL', message: '비밀번호가 잘못되었습니다.'};
            }
            session.socket.write(JSON.stringify(response));
        }
    });
}
