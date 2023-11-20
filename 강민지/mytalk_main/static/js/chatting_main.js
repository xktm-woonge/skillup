// DOM 요소 캐시
const sideBarTabs = Array.from(document.getElementsByClassName("side_bar--tab"));

/** 쿠키에서 csrf Token 가져오기 */
const csrfToken = getCSRFCookie();
function getCSRFCookie() {
  const name = "csrftoken=";
  const decodedCookie = decodeURIComponent(document.cookie);
  const ca = decodedCookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

/** response 값 가져오기 */
function handleResponse(response) {
  if (response.ok) {
    return response.json();
  } else {
    throw new Error("Error: " + response.status);
  }
}



/** 프로필 사진 설정 */
// 각 tag에 저장되어 있는 dataset의 파일을 불러온다.
function setProfilePic() {
  const userImgs = document.querySelectorAll(".profile");
  userImgs.forEach(function (userImg) {
    let profilePictureUrl = userImg.dataset.image || "profile_basic.png";
    userImg.style.background = `url('../static/img/${profilePictureUrl}') center / cover`;
  });
}



/** 사용자 정보 수정 버튼 클릭 시 동작 */
function addUserEditEvent() {
  document.querySelector(".user--cover__edit").addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(".user__name").disabled = false;
    document.querySelector(".user--status_message").disabled = false;
  });
}



/** 템플릿에 데이터 적용 */ 
function applyTemplate(template, data) {
  return template.replace(/{{\s*([^}]+)\s*}}/g, function (match, key) {
    return data[key];
  });
}

/** 공지사항 상자 생성 함수*/
function createNoticesBox(notice_data) {
  let resultHTML = "";
  let notice_box_template = NOTICE_BOX;
  Object.keys(notice_data).forEach(function (key) {
    let noticeItem = notice_data[key];
    noticeItem["button_type"] === "friends" ?  noticeItem["button_type"] = NOTICE_BOX_SELECT : (
      noticeItem["button_type"] = '<button class="notice--btn delete"></button>'
    );
    let noticeHTML = applyTemplate(notice_box_template, noticeItem);
    resultHTML += noticeHTML;
  });
  return resultHTML;
}

/** 친구 목록 생성 함수 */
function createFriendsList(friends_data) {
  let resultHTML = "";
  let friend_list_template = FRIENDS_LIST;
  Object.keys(friends_data).forEach(function (key) {
    let friendItem = friends_data[key];
    let friendHTML = applyTemplate(friend_list_template, friendItem);
    resultHTML += friendHTML;
  });
  return resultHTML;
}

/** 채팅 목록 생성 함수 */
function createChatList(chat_list_data) {
  let resultHTML = "";
  let chat_list_template = CHAT_LIST;
  Object.keys(chat_list_data).forEach(function (key) {
    let chatItem = chat_list_data[key];
    let chatHTML = applyTemplate(chat_list_template, chatItem);
    resultHTML += chatHTML;
  });
  return resultHTML;
}

/** 보낸 메시지 생성 함수 */
function sendedMessage(message_data) {
  let resultHTML = "";
  let message_box_template = MESSAGE_BOX;
  resultHTML = applyTemplate(message_box_template, message_data);
  return resultHTML;
}


function addOfflineUser(data){
  let offlinePoint = document.getElementById("offline_friends");
  let childNodes = offlinePoint.childNodes;
  print(childNodes.length);
  for (let i = childNodes.length - 1; i > 2; i--) {
    print(childNodes[i]);
    offlinePoint.removeChild(childNodes[i]);
  }
  offlinePoint.innerHTML += createFriendsList(data);
}


/** 현재 사용자 데이터 로드 함수 */
// load 시 해당 유저의 정보 DB에서 전달 받음
function loadCurrUserData() {
  fetch("/main/push_data_api/", {
    method: "GET",
  })
    .then(handleResponse)
    .then(function (page_data) {
      if (page_data != "") {
        document.getElementById("online_friends").innerHTML = createFriendsList(page_data.friend_list.online);
        document.querySelector(".side_bar--body.room").innerHTML = createChatList(page_data.chatting_room_list);
        document.querySelector(".side_bar--body.notice").innerHTML = createNoticesBox(page_data.notice_data);
        document.querySelector(".setting--user").innerHTML = page_data.curr_user_data;
        document.querySelector(".activeSet").value = page_data.present_status;
        addOfflineUser(page_data.friend_list.offline);
      }
      setProfilePic();
      webSocketInitialization(socketPath, 'load');
      settingUserEditing();
      addUserStatusEvent();
      addDeleteNoticeEvent();
      addFriendAcceptEvent();
      addFriendRejectEvent();
    });
}

// 실행
/* loadCurrUserData();*/
window.onload = loadCurrUserData();



/** 채팅방 메시지 스크롤 함수 */
// chatting room 에서 메시지를 가장 아래부터 볼 수 있게 스크롤하는 함수
function scrollToBottomInChatting() {
  var scroll_body = document.querySelector(".chat--body");
  scroll_body.scrollTop = scroll_body.scrollHeight;
}

/** 채팅 메시지 데이터 로드 함수 */
// chatting room 진입 시 해당 room에서 나눈 대화 load
function loadChattingMessageData(room_num) {
  fetch("/main/get_message_api/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken, // CSRF 토큰을 헤더에 추가
    },
    body: JSON.stringify({ "room_num": room_num }),
  })
    .then(handleResponse)
    .then(function (data) {
      document.getElementById("chatting_room_detail").innerHTML = data.data;
      setProfilePic();
      document
        .getElementById("chatting_room_detail")
        .classList.remove("displayNone");
      scrollToBottomInChatting();
      addEvent();
      document.getElementById("empty_contents").classList.add("displayNone");
      webSocketInitialization(socketPath+`${room_num}/`, "enter_chat_room");      
    })
    .then(
      socket.send(JSON.stringify({"message":"enter_chatting_room", "room_number":room_num})),
      document.querySelector(`#room_num_${room_num}`).classList.remove("new")
    )
}



// 임시용 데이터 테스트 함수
function chattingListClickerTest() {
  setProfilePic();
  document
    .getElementById("chatting_room_detail")
    .classList.remove("displayNone");
  scrollToBottomInChatting();
  addEvent();
  document.getElementById("empty_contents").classList.add("displayNone");
}


// 파일 처리 함수
function addProfileFile(fileData, used='apply') {
  let fileReader = new FileReader();
  fileReader.onload = (fileEvent) => {
    fileResult = fileEvent.target.result
    if(used === "send"){
      let file_data = {"message":"change_user_pic"}
      file_data["data"] = fileResult
      socket.send(JSON.stringify(file_data));
    } else{
      fileData.parentNode.style.background = `url('${fileResult}') center / cover`;
    }
  };
  fileReader.readAsDataURL(fileData.files[0]);
}

function toggleEditingMode(user, userInputs, toggleBtn) {
  if (!user.classList.contains("editing")) {
    toggleBtn.querySelector("img").src = "/static/icon/Check.svg";
    toggleBtn.querySelector("p").innerText = "저장";
    userInputs.forEach((input) => {
      input.disabled = false;
    });
  } else {
    let edit_data = {"message":"change_user_info"}
    toggleBtn.querySelector("img").src = "/static/icon/Edit.svg";
    toggleBtn.querySelector("p").innerText = "수정";
    userInputs.forEach((input) => {
      input.disabled = true;
      // 아래는 수정된 내용 websocket으로 전달하는 내용
      if(input.type === "file" && input.files && input.files.length > 0){
        addProfileFile(input, "send");
      } else {
        edit_data[`${input.type}`] = input.value;
      }
    });
    socket.send(JSON.stringify(edit_data));
  }
  user.classList.toggle("editing");
}

function settingUserEditing() {
  const user = document.querySelector(".setting--user");
  const userInputs = user.querySelectorAll("input, textarea");
  const toggleBtn = document.querySelector(".editToggle");
  const userPicture = user.querySelector("#profile_uploader");

  toggleBtn.addEventListener("click", function () {
    toggleEditingMode(user, userInputs, toggleBtn);
  });
  userPicture.addEventListener("change", function(){
    addProfileFile(this);
  })

}

// window.onload = settingUserEditing;
