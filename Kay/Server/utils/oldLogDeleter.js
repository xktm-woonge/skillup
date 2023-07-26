const fs = require('fs');
const path = require('path');

module.exports.deleteOldLogs = function (dirPath, maxAgeInDays) {
    const files = fs.readdirSync(dirPath);

    files.forEach(file => {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);
        const now = new Date().getTime();
        const fileTime = new Date(stats.ctime).getTime();
        const diffTime = now - fileTime;
        const diffDays = diffTime / (1000 * 3600 * 24);

        // If the file is older than maxAgeInDays, delete it
        if (diffDays > maxAgeInDays) {
            fs.unlinkSync(filePath);
        }
    });
};