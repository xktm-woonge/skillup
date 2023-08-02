// ./controller/login_controller.js

const dbManager = require('../model/dbManager');
const config = require('../config/config.js');
const logger = require('../utils/logger');
const { hashPassword } = require('../utils/security');
const httpPort = config.httpPort;

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
                // 여기서 필요한 정보를 데이터베이스로부터 가져옵니다.
                const friendsList = dbManager.getFriendsList(user.id);
                const recentChats = dbManager.getRecentChats(user.id);
                const groups = dbManager.getUserGroups(user.id);
                // 프로필 이미지 URL을 생성합니다.
                const profileImageUrl = `http://127.0.0.1:${httpPort}/profile_picture/${user.profile_picture}`;

                response = {
                    command: 'LOGIN',
                    status: 'SUCCESS',
                    message: '로그인에 성공했습니다.',
                    user: {
                        name: user.name,
                        email: user.email,
                        profile_img_url: profileImageUrl,
                        status: user.status
                    },
                    friendsList: friendsList,
                    recentChats: recentChats,
                    groups: groups
                    // 기타 필요한 정보를 여기에 추가
                };
            } else {
                response = {command: 'LOGIN', status: 'FAIL', message: '비밀번호가 잘못되었습니다.'};
            }
            session.socket.write(JSON.stringify(response));
        }
    });
}
