// server.js
const net = require('net');
const port = 3000;

const server = net.createServer();

server.on('connection', (socket) => {
    console.log('New client connected');
    
    socket.on('data', (data) => {
        let message = data.toString();
        console.log('Received:', message);
        
        // Parse and handle message here
        let [command, ...args] = message.split('|');

        switch (command) {
            case 'VERIFICATIONCODE':
                handleVerificationRequest(args[0]); // e.g., send email verification code
                break;
            case 'VERIFY':
                verifyVerificationCode(args[0], args[1]); // verify the code
                break;
            case 'REGISTER':
                registerUser(args[0], args[1], args[2]); // register user
                break;
            case 'LOGIN':
                loginUser(args[0], args[1]); // login user
                break;
            default:
                console.log('Unknown command:', command);
                break;
        }
    });
    
    socket.on('end', () => {
        console.log('Client disconnected');
    });
    
    socket.on('error', (err) => {
        console.log('Socket error:', err);
    });
});

server.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

function handleVerificationRequest(email) {
    // TODO: Implement function to handle verification code request
}

function verifyVerificationCode(email, code) {
    // TODO: Implement function to verify verification code
}

function registerUser(email, password, salt) {
    // TODO: Implement function to register user
}

function loginUser(email, password) {
    // TODO: Implement function to login user
}
