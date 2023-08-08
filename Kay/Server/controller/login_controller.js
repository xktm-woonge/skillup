// ./controller/register_controller.js

const jwt = require('jsonwebtoken');
const dbManager = require('../model/dbManager');
const config = require('../config/config.js');
const logger = require('../utils/logger');
const { hashPassword } = require('../utils/security');
const responseFormatter = require('../utils/responseFormatter');

const jwtSecretKey = process.env.JWT_SECRET_KEY;  // JWT 비밀키, 실제 서비스에서는 환경변수 등으로 보호되어야 합니다.
const serverAddr = config.serverAddr;
const httpPort = config.httpPort;

exports.handleLogin = function(req, res) {
    const email = req.body.email;
    const password = req.body.password;

    dbManager.getUserByEmail(email, (error, user, fields) => {
        let response;
        if (error) {
            response = responseFormatter.formatResponse('FAIL', '로그인에 실패했습니다.');
        } else if (!user) {
            response = responseFormatter.formatResponse('UNREGISTERED', '존재하지 않는 계정입니다.');
        } else {
            const salt = user.salt;
            const hashedPassword = hashPassword(password, salt);

            if (hashedPassword === user.password) {
                // const profileImageUrl = `http://${serverAddr}:${httpPort}/profile_picture/${user.profile_picture}`;

                const token = jwt.sign({ email }, jwtSecretKey, { expiresIn: '1d' });  // 토큰을 발행합니다.

                response = responseFormatter.formatResponse('SUCCESS', '로그인에 성공했습니다.', {
                    token // 클라이언트에게 토큰을 전달합니다.
                });


                // response = responseFormatter.formatResponse('SUCCESS', '로그인에 성공했습니다.', {
                //     user: {
                //         name: user.name,
                //         email: user.email,
                //         profile_img_url: profileImageUrl,
                //         status: "online"
                //         // token // 클라이언트에게 토큰을 전달합니다.
                //     }
                // });
            } else {
                response = responseFormatter.formatResponse('FAIL', '비밀번호가 잘못되었습니다.');
            }
        }

        if (response.status === 'SUCCESS') {
            dbManager.updateUserStatus(email, 'online', (error, results, fields) => {
                if (error) {
                    logger.error('Failed to update user status:', error);
                }
            });
        }

        res.json(response);
    });
};