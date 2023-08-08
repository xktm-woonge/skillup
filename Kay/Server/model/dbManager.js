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