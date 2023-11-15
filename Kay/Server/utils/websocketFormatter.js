exports.formatWebSocket = function(status, category, message, data) {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // 월은 0부터 시작하므로 1을 더합니다.
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    const timestamp = `${year}.${month}.${day} ${hours}:${minutes}:${seconds}`;

    return {
        status: status,
        category: category,
        message: message || '',
        data: data || {}, // 여기서 category가 올바른 필드인지 확인하세요.
        timestamp: timestamp
    };
};