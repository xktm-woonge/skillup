const logger = require('../utils/logger');
const { generateVerificationCode } = require('../utils/generateVerificationCode');
const dbManager = require('../model/dbManager');
const { sendEmail } = require('../model/emailService');


exports.handleVerificationCodeRequest = function (message, session) {
    logger.info(`message: ${JSON.stringify(message)}, session: ${JSON.stringify(session)}`)
    const email = message['info']['email'];

    dbManager.getUserByEmail(email, (error, results, fields) => {
        if (error) {
            let response = {command: 'VERIFICATIONCODE', status: 'FAIL', message: '이메일 조회 중 에러가 발생했습니다.'};
            logger.info(`response: ${JSON.stringify(response)}`);
            session.socket.write(JSON.stringify(response));
        } else if (results.length > 0) {
            let response = {command: 'VERIFICATIONCODE', status: 'DUPLICATE', message: '이미 가입된 계정입니다.'};
            logger.info(`response: ${JSON.stringify(response)}`);
            session.socket.write(JSON.stringify(response));
        } else {
            const verificationCode = generateVerificationCode();

            sendEmail(email, verificationCode, (error, info) => {
                let response;
                if (error) {
                    response = {command: 'VERIFICATIONCODE', status: 'FAIL', message: '이메일 전송에 실패했습니다.'};
                } else {
                    session.verificationCode = verificationCode;
                    response = {command: 'VERIFICATIONCODE', status: 'SUCCESS', message: '이메일 전송에 성공했습니다.'};
                }

                logger.info(`response: ${JSON.stringify(response)}`);
                session.socket.write(JSON.stringify(response));
            });    
        }
    });
}


exports.handleVerify = function (message, session) {
    logger.info(`message: ${JSON.stringify(message)}, session: ${JSON.stringify(session)}`)
    const received_code = message['info']['verification_code'];

    if (received_code === session.verificationCode) {
        response = {command: 'VERIFY' , status: 'SUCCESS',  message: '인증에 성공했습니다.'};
    } else {
        response = {command: 'VERIFY' , status: 'FAIL',  message: '인증에 실패했습니다. 다시 확인해 주세요.'};
    };

    logger.info(`response: ${JSON.stringify(response)}`);
    session.socket.write(JSON.stringify(response));
}


exports.handleRegister = function (message, session) {
    logger.info(`message: ${JSON.stringify(message)}, session: ${JSON.stringify(session)}`);
    const email = message['info']['email'];
    const password = message['info']['password'];
    const salt = message['info']['salt'];
  
    dbManager.createUser(email, password, salt, (error, results, fields) => {
      let response;
      if (error) {
        response = {command: 'REGISTER', status: 'FAIL', message: '회원가입에 실패했습니다.'};
      } else {
        response = {command: 'REGISTER', status: 'SUCCESS', message: '축하합니다.\n회원가입에 성공했습니다.'};
      }
      session.socket.write(JSON.stringify(response));
    });
  }