const mysql = require('mysql');

const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'localhost',
  user: 'root',
  password: '0000',
  database: 'chatting'
});

exports.createUser = function(email, password, salt, callback) {
  const profilePicture = 'images/base_profile.png';
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
  pool.query('SELECT * FROM users WHERE email = ?', [email], callback);
}
