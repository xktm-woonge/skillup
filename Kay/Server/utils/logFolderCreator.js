const fs = require('fs');
const path = require('path');

module.exports.createLogFolder = function (dirPath) {
    // Check if folder exists
    if (!fs.existsSync(dirPath)) {
        // If not, create it
        fs.mkdirSync(dirPath, { recursive: true });
    }
};