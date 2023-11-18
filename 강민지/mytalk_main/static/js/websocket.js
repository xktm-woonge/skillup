const userId = document.body.dataset.userId;
const socketPath = `ws://127.0.0.1:8000/ws/main/${userId}/`
var socket = null;

// 웹소켓 통신으로 변경할 함수

function addDefaultSocketFunction(message){
    if(message.message === "user_auth_error"){
        console.log("유저 인증 에러");
    }
}

function addChattingSocketFunction(message){
    if (["send_message", "receive_mesaage"].indexOf(message.message) !== -1){
        console.log(message.message);
        document.getElementsByClassName("chat--body")[0].innerHTML += addMessageBox(message);
        scrollToBottomInChatting();
    }
}

function addChatJustReceiveFuntion(message){
    if(["send_message", "receive_mesaage"].indexOf(message.message) !== -1){
        let roomnum = message.data["roomnum"];
        document.getElementById(`room_num_${roomnum}`).querySelector(".room__status").textContent = message.data["message"];
    }
}

function addNotiFunction(message){
    if(message.message === 'friend_request'){

    }
    else if(message.message === 'system'){

    }
    else if(message.message === 'receive_message'){

    }
}
function addReloadFunction(message){
    if(message.message === "reload"){
        loadCurrUserData();
    }
}

function webSocketInitialization(initSocketPath, action){
    if(socket){
        socket.onmessage = null;
        socket.close();
    }
    socket = new WebSocket(`${initSocketPath}`);
    let messageHandlers = [];
    switch (action){
        case "enter_chat_room":
            messageHandlers.push(addChattingSocketFunction);
        default:
            messageHandlers.push(addDefaultSocketFunction);
            messageHandlers.push(addChatJustReceiveFuntion);
            messageHandlers.push(addReloadFunction);
            messageHandlers.push(addNotiFunction);
    }
    socket.onmessage = function (e) {
        let message = JSON.parse(e.data); // message 정의
        print(message);
        for (const handler of messageHandlers) {
            handler(message);
        }
    };
}

// message box 추가하는 함수
function addMessageBox(data){
    let messageBoxTemplate = MESSAGE_BOX;
    let messageBoxItem = data.data;
    let messageBoxHTML = applyTemplate(messageBoxTemplate, messageBoxItem);
    return messageBoxHTML;
}

// form data를 json 형식으로 변경하여 전달하는 함수
function transFormDataToJson(formData){
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });
    return JSON.stringify(jsonData);
}

// message를 websocket을 통해 보내는 함수
function sendMessage() {
    let send_message_data = new FormData(document.getElementById("send_message"));

    if (send_message_data.get("send_text")){
        send_message_data.append("message", "send_message");
        send_message_data = transFormDataToJson(send_message_data);
        socket.send(send_message_data);
        document.querySelector(".chat--footer__text").value = "";
    }
}


// user의 상태가 변경되었을 때 적용 함수
function addUserStatusEvent() {
    document.querySelector(".activeSet").addEventListener("change", function(e) {
        let send_data = JSON.stringify({"message":"change_user_status","changed_status": e.target.value});
        socket.send(send_data);
    });
}


// 메세지를 보내는 함수
function addEvent() {
    document.getElementById("send_message").addEventListener("submit", function(e) {
        e.preventDefault();
        sendMessage();
    });
    document.querySelector(".chat--footer__text").addEventListener("keydown", function(e) {
        if (e.key === "Enter"){
            e.preventDefault();
            sendMessage();
        }
    });
}

// user logout
function userLogout(){
    fetch("/main/logout_api/", {
        method: "POST",
        headers: {
            "Content-Type" : "application/json",
            "X-CSRFToken" : csrfToken
        },
        body: JSON.stringify({"status":"logout"}),
    }).then(function(response){
        if(response.ok){
            return response.json();
        } else{
            throw new Error("Error:: "+response.status);
        }
    })
    .then(function(data){
        if(data.message === "Success"){
            alert("로그아웃 되었습니다.");
            window.location.href = "../";
        }
    })
}

document.getElementById("user_logout").addEventListener("click", function(e){
    e.preventDefault();
    userLogout();
});


// 자꾸 파이썬이랑 헷갈려서 임시로 만든 함수
function print(string){
    console.log(string);
}