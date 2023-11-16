// ./controller/login_controller.js

require('dotenv').config();
const jwt = require('jsonwebtoken');
const dbManager = require('../model/dbManager');
const config = require('../config/config.js');
const logger = require('../utils/logger');
const { hashPassword } = require('../utils/security');
const responseFormatter = require('../utils/responseFormatter');

const jwtSecretKey = process.env.JWT_SECRET_KEY;  // JWT 비밀키, 실제 서비스에서는 환경변수 등으로 보호되어야 합니다.

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

                const token = jwt.sign({ email }, jwtSecretKey, { expiresIn: '1d' });  // 토큰을 발행합니다.

                response = responseFormatter.formatResponse('SUCCESS', '로그인에 성공했습니다.', {
                    token // 클라이언트에게 토큰을 전달합니다.
                });

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


const serverAddr = config.serverAddr;
const httpPort = config.httpPort;

exports.get_userInfo = function(req, res) {
  const userEmail = req.userId; // 클라이언트에서 전달된 email

  // 사용자의 id를 기반으로 정보 가져오기
  dbManager.getUserByEmail(userEmail, (error, userInfo) => {
    if (error || !userInfo) {
      return res.json(responseFormatter.formatResponse('FAIL', '사용자 정보를 불러올 수 없습니다.'));
    }

    const userId = userInfo.id; // 사용자의 id

    // 친구 정보 가져오기
    dbManager.getFriendsInfoByUserId(userId, (error, friendsInfo) => {
      if (error) {
        return res.json(responseFormatter.formatResponse('FAIL', '친구 목록을 불러올 수 없습니다.'));
      }

      // 친구 목록의 프로필 이미지 경로를 수정합니다.
      if (friendsInfo && friendsInfo.length > 0) {
        friendsInfo.forEach(friend => {
          if (friend.profile_picture) {
            friend.profile_picture = `http://${serverAddr}:${httpPort}/profile_picture/${friend.profile_picture}`;
          }
        });
      }

      // 대화 목록 및 대화 내용 가져오기
      dbManager.getConversationsByUserId(userId, (error, conversations) => {
        if (error) {
          return res.json(responseFormatter.formatResponse('FAIL', '대화 목록을 불러올 수 없습니다.'));
        }

        // 사용자의 알림 정보 가져오기
        dbManager.getNotificationsForUser(userId, (error, notifications) => {
          if (error) {
            return res.json(responseFormatter.formatResponse('FAIL', '알림 정보를 불러올 수 없습니다.'));
          }

          // 프로필 이미지를 URL로 변경
          const profileImageUrl = `http://${serverAddr}:${httpPort}/profile_picture/${userInfo.profile_picture}`;
          userInfo['profile_picture'] = profileImageUrl

          // notifications 배열을 순회하면서 각 알림의 이미지 경로를 수정합니다.
          if (notifications && notifications.length > 0) {
            notifications.forEach(notification => {
              if (notification.img) {
                notification.image_path = `http://${serverAddr}:${httpPort}/friends_request/${notification.img}`;
              }
            });
          }

          res.json(responseFormatter.formatResponse('SUCCESS', '정보를 성공적으로 가져왔습니다.', {
            userInfo, // 사용자의 전체 프로필 정보
            friendsInfo, // 친구의 전체 정보
            conversations, // 대화 목록 및 대화 내용
            notifications  // 사용자의 알림 정보
          }));
        });
      });
    });
  });
};
