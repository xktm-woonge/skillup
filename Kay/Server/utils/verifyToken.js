// ./utils/verifyToken.js

const jwt = require('jsonwebtoken');

function verifyToken(req, res, next) {
  const authHeader = req.headers['authorization'];

  if (!authHeader) return res.status(403).send({ status: 'FAIL', message: 'No token provided.' });

  const token = authHeader.split(' ')[1]; // Bearer를 제거하고 토큰만 추출

  jwt.verify(token, process.env.JWT_SECRET_KEY, (err, decoded) => {
    console.error(err); // 에러 로깅
    if (err) return res.status(500).send({ status: 'FAIL', message: 'Failed to authenticate token.' });

    // 토큰이 검증되면, 이후 처리를 위해 사용자 ID를 저장
    req.userId = decoded.email;
    next();
  });
}

module.exports = verifyToken;