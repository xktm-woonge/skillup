// ./model/auth_router.js

const express = require('express');
const router = express.Router();
const registerController = require('../controller/register_controller');
const loginController = require('../controller/login_controller');

router.post('/verificationCode', registerController.handleVerificationCodeRequest);
router.post('/verify', registerController.handleVerify);
router.post('/register', registerController.handleRegister);
router.post('/login', loginController.handleLogin);

module.exports = router;