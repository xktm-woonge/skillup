// ./model/router.js

const express = require('express');
const router = express.Router();
const registerController = require('../controller/register_controller');
const loginController = require('../controller/login_controller');
const verifyToken = require('../utils/verifyToken'); // 미들웨어 임포트

router.post('/register/sendEmail_api', registerController.handleVerificationCodeRequest);
router.post('/register/confirmCertNum_api', registerController.handleVerify);
router.post('/register/addUser_api', registerController.handleRegister);
router.post('/login_api', loginController.handleLogin);
router.get('/userInfo_api', verifyToken, loginController.get_userInfo); // 미들웨어 사용

module.exports = router;