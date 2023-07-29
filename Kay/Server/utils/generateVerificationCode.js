// utils/generateVerificationCode.js
exports.generateVerificationCode = function() {
    return Math.floor(100000 + Math.random() * 900000).toString();  // 6자리 랜덤 숫자 생성
}