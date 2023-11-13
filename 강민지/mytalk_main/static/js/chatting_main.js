let side_bar_class = Array.from(document.getElementsByClassName('side_bar--tab'))

// 쿠키에서 csrf Token 을 가져온다.
const csrfToken = getCSRFCookie();
function getCSRFCookie() {
    const name = 'csrftoken=';
    const decodedCookie = decodeURIComponent(document.cookie);
    const ca = decodedCookie.split(';');
    for (let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

// 각 tag에 저장되어 있는 dataset의 파일을 불러온다.
function set_profile_pic() {
    const userImgs = document.querySelectorAll(".profile");
    userImgs.forEach(function(userImg) {
        let profilePictureUrl = userImg.dataset.image || 'profile_basic.png';
        userImg.style.background = `url('../static/img/${profilePictureUrl}') center / cover`;
    });
}

// user 수정 버튼을 누를 때 user name 및 status message box 활성화
function add_user_edit_event(){
    document.querySelector('.user--cover__edit').addEventListener('click', function(e){
        e.preventDefault();
        document.querySelector('.user__name').disabled = false;
        document.querySelector('.user--status_message').disabled = false;
    })
}



function applyTemplate(template, data) {
    return template.replace(/{{\s*([^}]+)\s*}}/g, function (match, key) {
        return data[key];
    });
}

function createNoticesBox(notice_data){
    let resultHTML = '';
    let notivce_box_template = NOTICE_BOX;
    Object.keys(notice_data).forEach(function(key){
        let noticeItem = notice_data[key];
        if (noticeItem['button_type'] === 'friends'){
            noticeItem['button_type'] = NOTICE_BOX_SELECT;
        } else {
            noticeItem['button_type'] = '<button class="notice--btn delete"></button>';
        }
        let noticeHTML = applyTemplate(notivce_box_template, noticeItem);
        resultHTML += noticeHTML;
    });
    return resultHTML;
}

function createFriendsList(friends_data){
    let resultHTML = '';
    let friend_list_template = FRIENDS_LIST;
    Object.keys(friends_data).forEach(function(key){
        let friendItem = friends_data[key];
        let friendHTML = applyTemplate(friend_list_template, friendItem);
        resultHTML += friendHTML;
    });
    return resultHTML;
}

function createChatList(chat_list_data){
    let resultHTML = '';
    let chat_list_template = CHAT_LIST;
    Object.keys(chat_list_data).forEach(function(key){
        let chatItem = chat_list_data[key];
        let chatHTML = applyTemplate(chat_list_template, chatItem);
        resultHTML += chatHTML;
    });
    return resultHTML;
}

function sended_message(message_data){
    let resultHTML = '';
    let message_box_template = MESSAGE_BOX;
    resultHTML = applyTemplate(message_box_template, message_data);
    return resultHTML;
}

// load 시 해당 유저의 정보 DB에서 전달 받음
function load_curr_user_data(){
    fetch('/main/push_data_api/', {
        method:'GET',
    })
    .then(function(response){
        if(response.ok){
            return response.json();
        } else {
            throw new Error('Error:'+response.status);
        }
    })
    .then(function(page_data){
        document.getElementById('online_friends').innerHTML += createFriendsList(page_data.friend_list.online);
        document.getElementById('offline_friends').innerHTML += createFriendsList(page_data.friend_list.offline);
        document.querySelector(".side_bar--body.room").innerHTML += createChatList(page_data.chatting_room_list);
        document.querySelector(".side_bar--body.notice").innerHTML = createNoticesBox(page_data.notice_data);
        document.querySelector(".setting--user").innerHTML = page_data.curr_user_data;
        document.querySelector('.activeSet').value = page_data.present_status;
        set_profile_pic();
        add_user_status_event();
    })
}


// chatting room 에서 메시지를 가장 아래부터 볼 수 있게 스크롤하는 함수
function scroll_to_bottom_in_chatting(){
    var scroll_body = document.querySelector('.chat_contents');
    
    scroll_body.scrollTop = scroll_body.scrollHeight;
}


// chatting room 진입 시 해당 room에서 나눈 대화 load
function load_chatting_message_data(room_num) {

    fetch('/main/get_message_api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,  // CSRF 토큰을 헤더에 추가
        },
        body: JSON.stringify({'room_num': room_num})
    })
    .then(function(response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error: ' + response.status);
        }
    })
    .then(function(data) {
        document.getElementById('chatting_room_detail').innerHTML = data.data;
        set_profile_pic();
        document.getElementById('chatting_room_detail').style.display = 'block';
        scroll_to_bottom_in_chatting();
        add_event();
        document.getElementById('empty_contents').style.display = 'none';
    });
}

// user logout
function userLogout(){
    fetch('/main/logout_api/', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrfToken
        },
        body: JSON.stringify({'status':'logout'}),
    }).then(function(response){
        if(response.ok){
            return response.json();
        } else{
            throw new Error('Error:: '+response.status);
        }
    })
    .then(function(data){
        if(data.message === 'Success'){
            alert('로그아웃 되었습니다.');
            window.location.href = '../';
        }
    })
}

document.getElementById('user_logout').addEventListener('click', function(e){
    e.preventDefault();
    userLogout();
});

window.onload = load_curr_user_data();