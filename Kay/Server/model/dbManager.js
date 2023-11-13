// ./model/dbManager.js

const mysql = require('mysql');
const config = require('../config/config.js');
const serverAddr = config.serverAddr;

const pool = mysql.createPool({
  connectionLimit: 10,
  host: serverAddr,
  user: 'root',
  password: '0000',
  database: 'chatting'
});

exports.createUser = function(email, password, salt, callback) {
  const profilePicture = 'base_profile.png';
  pool.query('INSERT INTO users SET ?', {
    name: "Hi",
    email: email,
    profile_picture: profilePicture,
    status: "offline",
    password: password,
    salt: salt
  }, callback);
}

exports.getUserByEmail = function(email, callback) {
  const sql = `SELECT * FROM users WHERE email = ?`;
  pool.query(sql, [email], (error, results, fields) => {

      if (error) {
          return callback(error, null, null);
      }

      let user = results[0];
      
      return callback(null, user, fields);
  });
};

exports.updateUserStatus = function(email, status, callback) {
  const sql = `UPDATE users SET status = ? WHERE email = ?`;
  pool.query(sql, [status, email], callback);
}

// 친구 목록 가져오기
exports.getFriendsByUserId = function(user_id, callback) {
  const query = `SELECT * FROM Friends JOIN Users ON Friends.friend_id = Users.id WHERE Friends.user_id = ?`;
  pool.query(query, [user_id], callback);
};

// 대화 목록 및 대화 내용 가져오기
exports.getConversationsByUserId = function(user_id, callback) {
  const query = `SELECT * FROM Conversations
                 JOIN ConversationParticipants ON Conversations.id = ConversationParticipants.conversation_id
                 JOIN Messages ON Conversations.id = Messages.conversation_id
                 WHERE ConversationParticipants.user_id = ?`;
  pool.query(query, [user_id], callback);
};

// 자신과 친구들의 정보 가져오기
exports.getFriendsInfoByUserId = function(userId, callback) {
  const sql = `
    SELECT u.id, u.name, u.email, u.profile_picture, u.status
    FROM Users AS u
    JOIN Friends AS f ON (f.user_id = ? AND u.id = f.friend_id) OR (f.friend_id = ? AND u.id = f.user_id)
    WHERE u.id != ?
  `;

  pool.query(sql, [userId, userId, userId], callback);
};

exports.getUserInfoByUserId = function(email, callback) {
  const sql = `
    SELECT profile_picture, status
    FROM users
    WHERE email = ?
  `;

  pool.query(sql, [email], (error, results) => {
    if (error) {
      return callback(error, null);
    }

    if (results.length > 0) {
      callback(null, results[0]); // 첫 번째 결과 반환
    } else {
      callback(new Error("No user found with the given email"), null);
    }
  });
};

exports.getNotificationsForUser = function(user_id, callback) {
  const sql = `SELECT * FROM Notifications WHERE user_id = ? ORDER BY created_at DESC`;
  pool.query(sql, [user_id], callback);
};

exports.insertFriendRequestNotification = function(senderId, receiverId, callback) {
  const sql = `
      INSERT INTO Notifications (user_id, type, content, sender_id) 
      VALUES (?, 'FRIEND_REQUEST', 'New friend request from user '?, ?)
  `;
  pool.query(sql, [receiverId, senderId, senderId], callback);
};

exports.deleteNotification = function(user_id, sender_id, callback) {
  const sql = `DELETE FROM Notifications WHERE user_id = ? AND sender_id = ?`;
  pool.query(sql, [user_id, sender_id], callback);
};

exports.addFriend = function(user_id, friend_id, callback) {
  const sql = `INSERT INTO Friends (user_id, friend_id) VALUES (?, ?)`;
  pool.query(sql, [user_id, friend_id], (error, results) => {
    if (error) {
      // 오류 처리
      return callback(error);
    }

    // 성공적으로 추가된 경우
    callback(null, results);
  });
};