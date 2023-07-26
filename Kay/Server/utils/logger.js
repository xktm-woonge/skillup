// utils/logger.js
const winston = require('winston');
const path = require('path');
const { createLogFolder } = require('./logFolderCreator');
const { deleteOldLogs } = require('./oldLogDeleter');

const parentDir = path.dirname(__dirname);
const logDir = path.join(parentDir, 'log');

// Create log folder if it doesn't exist
createLogFolder(logDir);

// Delete logs older than 30 days
deleteOldLogs(logDir, 30);

// Get current date and time for log file name
const currentDate = new Date();
const timestamp = `${currentDate.getFullYear()}${currentDate.getMonth() + 1}${currentDate.getDate()}_${currentDate.getHours()}${currentDate.getMinutes()}${currentDate.getSeconds()}`;

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.File({ filename: path.join(logDir, `${timestamp}_error.log`), level: 'error' }),
        new winston.transports.File({ filename: path.join(logDir, `${timestamp}_combined.log`) })
    ]
});

module.exports = logger;
