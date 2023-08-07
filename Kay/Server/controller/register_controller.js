// ./controller/register_controller.js

const logger = require('../utils/logger');
const responseFormatter = require('../utils/responseFormatter');
const { generateVerificationCode } = require('../utils/generateVerificationCode');
const dbManager = require('../model/dbManager');
const { sendEmail } = require('../model/emailService');

let verificationCodes = {};

exports.handleVerificationCodeRequest = function(req, res) {
    const email = req.body.email;

    dbManager.getUserByEmail(email, (error, user, fields) => {
        let response;
        if (error) {
            response = responseFormatter.formatResponse('FAIL', '이메일 조회 중 에러가 발생했습니다.');
            return res.json(response);
        } 
        if (user) {
            response = responseFormatter.formatResponse('DUPLICATE', '이미 가입된 계정입니다.');
            return res.json(response);
        } 
        
        const verificationCode = generateVerificationCode();

        sendEmail(email, verificationCode, (error, info) => {
            if (error) {
                response = responseFormatter.formatResponse('FAIL', '이메일 전송에 실패했습니다.');
            } else {
                verificationCodes[email] = verificationCode;
                response = responseFormatter.formatResponse('SUCCESS', '이메일 전송에 성공했습니다.');
            }
            res.json(response);
        });
    });
};

exports.handleVerify = function(req, res) {
    const email = req.body.email;
    const received_code = req.body.verification_code;

    if (received_code === verificationCodes[email]) {
        response = responseFormatter.formatResponse('SUCCESS', '인증에 성공했습니다.');
    } else {
        response = responseFormatter.formatResponse('FAIL', '인증에 실패했습니다. 다시 확인해 주세요.');
    }
    res.json(response);
};

exports.handleRegister = function(req, res) {
    const email = req.body.email;
    const password = req.body.password;
    const salt = req.body.salt;

    dbManager.createUser(email, password, salt, (error, results, fields) => {
        let response;
        if (error) {
            response = responseFormatter.formatResponse('FAIL', '회원가입에 실패했습니다.');
        } else {
            response = responseFormatter.formatResponse('SUCCESS', '축하합니다! 회원가입이 완료되었습니다.');
        }
        res.json(response);
    });
};