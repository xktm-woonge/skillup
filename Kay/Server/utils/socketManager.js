// ./utils/socketManager.js

const WebSocket = require('ws');
let wss = null;

exports.initialize = (server) => {
    wss = new WebSocket.Server({ server });
    return wss;
};

exports.getWSS = () => {
    if (!wss) {
        throw new Error("WebSocket Server not initialized!");
    }
    return wss;
};
