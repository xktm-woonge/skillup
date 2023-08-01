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
  const sql = `SELECT * FROM users WHERE email = ?`;
  pool.query(sql, [email], (error, results, fields) => {
      if (error) {
          return callback(error, null, null);
      }

      let user = results[0];
      // assuming 'profile_picture' is the correct column name in your table
      user.profile_picture = path.join("/uploads", user.profile_picture);

      return callback(null, user, fields);
  });
};