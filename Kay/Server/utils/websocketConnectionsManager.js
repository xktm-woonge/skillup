// websocketConnectionsManager.js
const websocketConnections = {};

function addConnection(userId, ws) {
    websocketConnections[userId] = ws;
}

function removeConnection(userId) {
    delete websocketConnections[userId];
}

function getConnection(userId) {
    return websocketConnections[userId];
}

module.exports = { addConnection, removeConnection, getConnection };