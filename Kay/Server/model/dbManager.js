// ./model/dbManager.js

const mysql = require('mysql');
// const path = require('path');
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
      // // assuming 'profile_picture' is the correct column name in your table
      // user.profile_picture = path.join("/uploads", user.profile_picture);

      return callback(null, user, fields);
  });
};


exports.getFriendsList = function(userId, callback) {
  const sql = 'SELECT friends.* FROM friends JOIN users_friends ON friends.id = users_friends.friend_id WHERE users_friends.user_id = ?';
  pool.query(sql, [userId], (error, results, fields) => {
    if (error) {
      return callback(error, null, null);
    }

    return callback(null, results, fields);
  });
};

exports.getRecentChats = function(userId, callback) {
  const sql = 'SELECT chats.* FROM chats JOIN users_chats ON chats.id = users_chats.chat_id WHERE users_chats.user_id = ? ORDER BY chats.timestamp DESC LIMIT 10';
  pool.query(sql, [userId], (error, results, fields) => {
    if (error) {
      return callback(error, null, null);
    }

    return callback(null, results, fields);
  });
};

exports.getUserGroups = function(userId, callback) {
  const sql = 'SELECT groups.* FROM groups JOIN users_groups ON groups.id = users_groups.group_id WHERE users_groups.user_id = ?';
  pool.query(sql, [userId], (error, results, fields) => {
    if (error) {
      return callback(error, null, null);
    }

    return callback(null, results, fields);
  });
};
