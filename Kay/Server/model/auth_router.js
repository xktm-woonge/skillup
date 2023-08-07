// ./model/auth_router.js

const express = require('express');
const router = express.Router();
const registerController = require('../controller/register_controller');
const loginController = require('../controller/login_controller');

router.post('/register/sendEmail_api', registerController.handleVerificationCodeRequest);
router.post('/register/confirmCertNum_api', registerController.handleVerify);
router.post('/register/addUser_api', registerController.handleRegister);
router.post('/login_api', loginController.handleLogin);

module.exports = router;