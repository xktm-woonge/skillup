const userId = document.body.dataset.userId;
const socketPath = `ws://127.0.0.1:8000/ws/main/${userId}/`
var socket = null;

// 웹소켓 통신으로 변경할 함수

// 유저 로그인 확인 함수 --- 수정 예정
function addDefaultSocketFunction(message){
    if(message.message === "user_auth_error"){
        console.log("유저 인증 에러");
    }
}

// 채팅방 내 대화 시 소켓 통신 후 실행할 함수
function addChattingSocketFunction(message){
    if (["send_message", "receive_mesaage"].indexOf(message.message) !== -1){
        // console.log(message.message);
        document.getElementsByClassName("chat--body")[0].innerHTML += addMessageBox(message);
        scrollToBottomInChatting();
    }
}

// 채팅방에 들어가 있지 않은 경우 소켓 통신 후 실행할 함수
function addChatJustReceiveFuntion(message){
    if(["send_message", "receive_mesaage"].indexOf(message.message) !== -1){
        let roomnum = message.data["roomnum"];
        document.getElementById(`room_num_${roomnum}`).querySelector(".room__status").textContent = message.data["message"];
    }
}

// 알림창 내부 소켓 통신 후 실행할 함수 -- 개발 중
function addNotiFunction(message){
    if(message.message === "friend_request"){

    }
    else if(message.message === "system"){

    }
    else if(message.message === "receive_message"){

    }
    else if(message.message === "delete_notice"){
        let notiNum = message["noti_num"];
        let deleteElement = document.querySelector(`.notice--group.num_${notiNum}`);
        deleteElement.remove();
    }
}

// user 정보 변경 시 sideBar reload 적용 함수
function addReloadFunction(message){
    if(message.message === "reload"){
        loadCurrUserData();
    }
}

// room 마다 소켓 레이어 재생성하기 위한 함수
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


// notice box 내 notice number를 찾아서 반환하는 함수
function findNumInClassName(classList){
    let numClass = Array.from(classList).find(className => className.startsWith("num_"));
    let match = numClass.match(/\d+/);
    if (match) {
        return parseInt(match[0], 10);
        } else {
        return null
    }
}

// delete 버튼을 누를 떄 실행 할 함수
function addDeleteNoticeEvent(){
    document.querySelectorAll(".notice--btn.delete").forEach(function(button){
        button.addEventListener("click", function(e){
            let parentClassList = this.parentElement.classList;
            let noticeNum = findNumInClassName(parentClassList);
            socket.send(JSON.stringify({"message":"delete_notice", "noti_num":noticeNum}));
        })
    })
}



// 아래 두 함수 비슷한 게 너무 많아서 차후 가능한 방향 찾아서 통합하고 싶음
// 친구 요청 수락 시 실행 할 함수
function addFriendAcceptEvent(){
    document.querySelectorAll(".actions__accept").forEach(function(accept){
        accept.addEventListener("click", function(e){
            let parentClassList = this.parentElement.parentElement.classList;
            let friendNotiNum = findNumInClassName(parentClassList);
            socket.send(JSON.stringify({"message":"accept_friend", "noti_num":friendNotiNum}));
        })
    })
}

// 친구 요청 거절 시 실행 할 함수
function addFriendRejectEvent(){
    document.querySelectorAll(".actions__reject").forEach(function(reject){
        reject.addEventListener("click", function(e){
            let parentClassList = this.parentElement.parentElement.classList;
            let friendNotiNum = findNumInClassName(parentClassList);
            socket.send(JSON.stringify({"message":"reject_friend", "noti_num":friendNotiNum}));
        })
    })
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