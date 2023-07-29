const mysql = require('mysql');

const pool = mysql.createPool({
  connectionLimit: 10, // 연결 풀에 생성될 수 있는 최대 연결 수. 기본값은 10입니다.
  host: 'localhost',
  user: 'root',
  password: '0000',
  database: 'chatting'
});

exports.createUser = function(email, password, salt, callback) {
  pool.query('INSERT INTO accounts SET ?', {
    email: email,
    password: password,
    salt: salt
  }, callback);
}

exports.getUserByEmail = function(email, callback) {
  pool.query('SELECT * FROM accounts WHERE email = ?', [email], callback);
}