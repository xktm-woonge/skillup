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
function changeSideBar(goto){
    removeActiveClass(gnbButtons);
    removeActiveClass(gnbSides);
    closeDropdowns();
    document.querySelector(`#${goto}`).classList.add("active");
    document.querySelector(`#side_bar_${goto}`).classList.add("active");
}


// 채팅방 내 대화 시 소켓 통신 후 실행할 함수
function addChattingSocketFunction(message){
    if (["send_message", "receive_mesaage"].indexOf(message.message) !== -1){
        console.log(message.message);
        document.getElementsByClassName("chat--body")[0].innerHTML += addMessageBox(message);
        scrollToBottomInChatting();
    }
    if(message.message === "receive_mesaage"){
        document.querySelector(".chat--user_info__recent").setAttribute('datetime', new Date());
    }
}

// 채팅방에 들어가 있지 않은 경우 소켓 통신 후 실행할 함수
function addChatJustReceiveFuntion(message){
    if(["last_message"].indexOf(message.message) !== -1){
        let roomnum = message.data["roomnum"];
        const thisRoom = document.getElementById(`room_num_${roomnum}`);
        const timeSet = thisRoom.querySelector(".room__time");
        timeSet.setAttribute('datetime', new Date());
        thisRoom.querySelector(".room__status p").textContent = message.data["message"];
        thisRoom.querySelector(".room__status").appendChild(timeSet);
        sortChatList(true, roomnum);
        chatListTime();
        if (!message.is_sender){
            document.querySelector(`#room_num_${roomnum}`).classList.add("new");
            swal("📨새로운 메세지가 있습니다!");
            playNotificationSound();
        }
    }
}
// 알림창 내부 소켓 통신 후 실행할 함수 -- 개발 중
function addNotiFunction(message){
    if(message.message === "friend_request"){
        print(message.message)
        document.querySelector(".side_bar--body.notice").innerHTML += createNoticesBox({"1":message.data});
        setProfilePic();
        addFriendEvent();
        swal("알림", "친구 요청이 도착하였습니다.", "info");
        playNotificationSound();
    }
    else if(message.message === "system"){

    }
    else if(message.message === "receive_message"){

    }
    else if(["delete_notice", "accept_friend", "reject_friend"].indexOf(message.message) !== -1){
        let notiNum = message["noti_num"];
        let deleteElement = document.querySelector(`.notice--group.num_${notiNum}`);
        if (deleteElement){
            deleteElement.classList.add("deleted");
            setTimeout(() => deleteElement.remove(), 300);
        }
        if (message.message === "accept_friend"){
            if(message.friends_data.is_online){
                document.getElementById("online_friends").innerHTML += createFriendsList({"1":message.friends_data.online});
            } else {
                addOfflineUser({"1":message.friends_data.offline}, false);
            }
            setProfilePic();
            changeSideBar("friends");
            addOpenChattingFromFriendsListEvent();
            swal("친구가 추가되었습니다.");
            playNotificationSound();
        }
    }
}

// user 정보 변경 시 sideBar reload 적용 함수
function addReloadFunction(message){
    if(message.message === "reload"){
        loadCurrUserData(true);
    }
}
function addChatUserInfoReloadFunction(message){
    if(message.message === "reload"){
        loadChattingMessageData(currRoomNum, true);
    }
}
function addChatListFunction(message){
    if(message.message === "add_chat_list"){
        let currRoomNum = message.data.room_num;
        document.querySelector(".side_bar--body.room").innerHTML += createChatList({"1":message.data});
        sortChatList(true, currRoomNum);
    }
}

function addEnterChatRoomFromFriendFunction(message){
    if(message.message === "enter_chat_room_from_friend"){
        currRoomNum = message.room_num;
        if(message.is_new_chat){
            socket.send(JSON.stringify({"message":"add_chat_list", "room_number":currRoomNum}))
        }
        changeSideBar("chat");
        loadChattingMessageData(currRoomNum);
    }
}

// room 마다 소켓 레이어 재생성하기 위한 함수
function webSocketInitialization(initSocketPath, action) {
    return new Promise((resolve, reject) => {
        if (socket) {
            socket.onmessage = null;
            socket.close();
        }
        socket = new WebSocket(`${initSocketPath}`);
        let messageHandlers = [];
        switch (action) {
            case "enter_chat_room":
                setInterval(userResponseTime, 100);
                messageHandlers.push(addChattingSocketFunction);
                messageHandlers.push(addChatUserInfoReloadFunction);
            default:
                messageHandlers.push(addDefaultSocketFunction);
                messageHandlers.push(addChatJustReceiveFuntion);
                messageHandlers.push(addReloadFunction);
                messageHandlers.push(addNotiFunction);
                messageHandlers.push(addEnterChatRoomFromFriendFunction);
                messageHandlers.push(addChatListFunction);
        }
        socket.onopen = () => {
            resolve(); // WebSocket이 생성되면 resolve 호출
        };
        socket.onmessage = function (e) {
            let message = JSON.parse(e.data); // message 정의
            // print(message);
            for (const handler of messageHandlers) {
                handler(message);
            }
        };
    });
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
        button.addEventListener("click", function(){
            let parentClassList = this.parentElement.classList;
            let noticeNum = findNumInClassName(parentClassList);
            socket.send(JSON.stringify({"message":"delete_notice", "noti_num":noticeNum}));
        })
    })
}

// 친구 요청 버튼 Click 시 실행 될 함수
function addFriendEvent() {
    const actionType = ['accept', 'reject'];
    actionType.forEach(function(action){
        document.querySelectorAll(".actions__" + action).forEach(function (element) {
            element.addEventListener("click", function () {
                let parentClassList = this.parentElement.parentElement.classList;
                let friendNotiNum = findNumInClassName(parentClassList);
                socket.send(JSON.stringify({"message": `${action}_friend`, "noti_num": friendNotiNum}));
            });
        });
    })
    
}

// 친구 목록 Double Click 시 실행될 함수
function addOpenChattingFromFriendsListEvent(){
    document.querySelectorAll('.friends--box').forEach(function(friendList){
        friendList.addEventListener("dblclick", function(){
            let selectedName = this.querySelector(".friends__name").textContent;
            socket.send(JSON.stringify({"message":"enter_chat_from_friends", "friend_name":selectedName}))
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
    swal("Log out", "로그아웃 하시겠습니까?", "warning", {
        buttons: ["취소", "로그아웃"],
        dangerMode: true,
    }).then(function(willLogout){
        if(willLogout){
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
                    socket.send(JSON.stringify({ "message": "user_logout" }));
                    swal("로그아웃 되었습니다.", {
                        icon: "success", 
                    }).then(function (moveScreen) {
                        if (moveScreen) {
                            socket.close();
                            window.location.href = "../";
                        }
                    })
                }
            })
        }
    })
}


document.getElementById("alert--logout").addEventListener("click", function(e){
    e.preventDefault();
    userLogout();
});


// 자꾸 파이썬이랑 헷갈려서 임시로 만든 함수
function print(string){
    console.log(string);
}