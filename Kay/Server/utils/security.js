const crypto = require('crypto');

exports.hashPassword = function(password, salt) {
    const passwordBytes = Buffer.from(password, 'utf-8');
    const saltBytes = Buffer.from(salt, 'utf-8');
    return crypto.pbkdf2Sync(passwordBytes, saltBytes, 100000, 64, 'sha256').toString('hex');
};