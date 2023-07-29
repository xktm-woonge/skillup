const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '0000',
  database: 'chatting'
});

connection.connect();

exports.createUser = function(email, password, salt, callback) {

  connection.query('INSERT INTO accounts SET ?', {
    email: email,
    password: password,
    salt: salt
  }, callback);
}