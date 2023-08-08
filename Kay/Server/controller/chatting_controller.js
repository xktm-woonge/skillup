// ./controller/chatting_controller.js

const dbManager = require('../model/dbManager');
const responseFormatter = require('../utils/responseFormatter');

// ./controller/chatting_controller.js

exports.get_userInfo = function(req, res) {
    // 토큰에서 추출한 사용자 ID를 사용
    const userId = req.userId;
  
    // 자신과 친구들의 정보 가져오기
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
          friendsInfo,
          conversations
        }));
      });
    });
  };
  