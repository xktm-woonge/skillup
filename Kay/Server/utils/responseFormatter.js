// ./utils/responseFormatter.js

exports.formatResponse = (status, message, data) => {
    return {
        status: status,
        message: message,
        data: data || {} // data는 옵셔널하게 처리
    };
}