exports.formatResponse = (command, status, message, data) => {
    return {
        command: command,
        status: status,
        message: message,
        data: data || {} // data는 옵셔널하게 처리
    };
}