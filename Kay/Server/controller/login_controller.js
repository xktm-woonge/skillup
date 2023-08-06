const dbManager = require('../model/dbManager');
const config = require('../config/config.js');
const logger = require('../utils/logger');
const { hashPassword } = require('../utils/security');
const responseFormatter = require('../utils/responseFormatter');

const serverAddr = config.serverAddr;
const httpPort = config.httpPort;

exports.handleLogin = function(req, res) {
    const email = req.body.info.email;
    const password = req.body.info.password;

    dbManager.getUserByEmail(email, (error, user, fields) => {
        let response;
        if (error) {
            response = responseFormatter.formatResponse('LOGIN', 'FAIL', '로그인에 실패했습니다.');
        } else if (!user) {
            response = responseFormatter.formatResponse('LOGIN', 'UNREGISTERED', '존재하지 않는 계정입니다.');
        } else {
            const salt = user.salt;
            const hashedPassword = hashPassword(password, salt);

            if (hashedPassword === user.password) {
                const profileImageUrl = `http://${serverAddr}:${httpPort}/profile_picture/${user.profile_picture}`;

                response = responseFormatter.formatResponse('LOGIN', 'SUCCESS', '로그인에 성공했습니다.', {
                    user: {
                        name: user.name,
                        email: user.email,
                        profile_img_url: profileImageUrl,
                        status: "online"
                    }
                });
            } else {
                response = responseFormatter.formatResponse('LOGIN', 'FAIL', '비밀번호가 잘못되었습니다.');
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