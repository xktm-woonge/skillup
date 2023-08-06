const logger = require('../utils/logger');
const responseFormatter = require('../utils/responseFormatter');
const { generateVerificationCode } = require('../utils/generateVerificationCode');
const dbManager = require('../model/dbManager');
const { sendEmail } = require('../model/emailService');

exports.handleVerificationCodeRequest = function(req, res) {
    const email = req.body.info.email;

    dbManager.getUserByEmail(email, (error, user, fields) => {
        let response;
        if (error) {
            response = responseFormatter.formatResponse('VERIFICATIONCODE', 'FAIL', '이메일 조회 중 에러가 발생했습니다.');
        } else if (user) {
            response = responseFormatter.formatResponse('VERIFICATIONCODE', 'DUPLICATE', '이미 가입된 계정입니다.');
        } else {
            const verificationCode = generateVerificationCode();

            sendEmail(email, verificationCode, (error, info) => {
                if (error) {
                    response = responseFormatter.formatResponse('VERIFICATIONCODE', 'FAIL', '이메일 전송에 실패했습니다.');
                } else {
                    req.session.verificationCode = verificationCode;
                    response = responseFormatter.formatResponse('VERIFICATIONCODE', 'SUCCESS', '이메일 전송에 성공했습니다.');
                }
                res.json(response);
            });
        }
    });
};

exports.handleVerify = function(req, res) {
    const received_code = req.body.info.verification_code;

    if (received_code === req.session.verificationCode) {
        response = responseFormatter.formatResponse('VERIFY', 'SUCCESS', '인증에 성공했습니다.');
    } else {
        response = responseFormatter.formatResponse('VERIFY', 'FAIL', '인증에 실패했습니다. 다시 확인해 주세요.');
    }
    res.json(response);
};

exports.handleRegister = function(req, res) {
    const email = req.body.info.email;
    const password = req.body.info.password;
    const salt = req.body.info.salt;

    dbManager.createUser(email, password, salt, (error, results, fields) => {
        let response;
        if (error) {
            response = responseFormatter.formatResponse('REGISTER', 'FAIL', '회원가입에 실패했습니다.');
        } else {
            response = responseFormatter.formatResponse('REGISTER', 'SUCCESS', '축하합니다! 회원가입이 완료되었습니다.');
        }
        res.json(response);
    });
};