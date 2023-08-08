// ./controller/chatting_controller.js

const dbManager = require('../model/dbManager');
const responseFormatter = require('../utils/responseFormatter');

exports.get_userInfo = function(req, res) {
  // 토큰에서 추출한 사용자 ID를 사용
  const userId = req.body.email;

  // 사용자의 프로필 정보 가져오기
  dbManager.getUserInfoByUserId(userId, (error, userInfo) => {
    if (error) {
      return res.json(responseFormatter.formatResponse('FAIL', '사용자 정보를 불러올 수 없습니다.'));
    }

    // 친구 정보 가져오기
    dbManager.getFriendsInfoByUserId(userId, (error, friendsInfo) => {
      if (error) {
        return res.json(responseFormatter.formatResponse('FAIL', '친구 목록을 불러올 수 없습니다.'));
      }

      // 대화 목록 및 대화 내용 가져오기
      dbManager.getConversationsByUserId(userId, (error, conversations) => {
        if (error) {
          return res.json(responseFormatter.formatResponse('FAIL', '대화 목록을 불러올 수 없습니다.'));
        }

        res.json(responseFormatter.formatResponse('SUCCESS', '정보를 성공적으로 가져왔습니다.', {
          userInfo, // 사용자의 프로필 정보 (status, profile_picture 등)
          friendsInfo,
          conversations
        }));
      });
    });
  });
};