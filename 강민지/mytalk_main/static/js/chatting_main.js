let socket = new WebSocket("ws://localhost:8000/ws/main/"); // ws:// 이후의 주소는 routing.py 의 경로
let side_bar_class = Array.from(document.getElementsByClassName('side_bar--tab'))
const csrfToken = getCSRFCookie();


socket.onopen = function(){
    const message = {
        'message':'open'
    };
    socket.send(JSON.stringify(message));
}
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



function add_user_status_event() {
    document.querySelector('.user--activeSet').addEventListener('change', function(e){
        e.preventDefault()
        let changed_status = {'changed_status' : e.target.value,}
        fetch('/main/user_active_set_api/', {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,  // CSRF 토큰을 헤더에 추가
            },
            body : JSON.stringify(changed_status),
        })
        .then(function(response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error: ' + response.status);
            }
        })
        .then(data => console.log(data));
      })
}
function set_profile_pic() {
    const userImgs = document.querySelectorAll(".friends--profile");
    userImgs.forEach(function(userImg) {
        const profilePictureUrl = userImg.getAttribute("data-image");
        userImg.style.background = `url('../static/img/${profilePictureUrl}') center / cover`;
    });
}

function add_event() {
    document.getElementById('send_message').addEventListener('submit', function(e) {
        e.preventDefault();
        send_message();
    });
    document.getElementById('message_input_text').addEventListener('keydown', function(e) {
        if (e.key === 'Enter'){
            send_message();
        }
    });
}

function conv_chatbot(question, roomnum) {
    fetch('/main/recive_chatbot_conv_api/', {
        method: 'POST', 
        body : question,
    })
    .then(function(response){
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error:' + response.status);
        }
    })
    .then(function(data){
        document.getElementsByClassName('chat_contents')[0].innerHTML += data.data;
        scroll_to_bottom_in_chatting();
        document.getElementById(`room_num_${roomnum}`).querySelector('.room_final_message').textContent = data.last_message;
    })
}

function send_message() {
    let send_message_data = new FormData(document.getElementById('send_message'));
    let room_num = send_message_data.get('room_number');

    if (send_message_data.get('send_text')){
        fetch('/main/send_message_api/', {
            method: 'POST',
            body: send_message_data,
        })
        .then(function(response) {
            if (response.ok) {
                document.getElementById('message_input_text').value = '';
                return response.json();
            } else {
                throw new Error('Error: ' + response.status);
            }
        })
        .then(function(data){
            document.getElementsByClassName('chat_contents')[0].innerHTML += data.data;
            scroll_to_bottom_in_chatting();
            document.getElementById(`room_num_${room_num}`).querySelector('.room_final_message').textContent = data.last_message;
            if(!data.is_chatbot_conv){conv_chatbot(send_message_data, room_num)};
        })
    }
}
    

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
        document.getElementById('online_friends').innerHTML += page_data.friend_list.online;
        document.getElementById('offline_friends').innerHTML += page_data.friend_list.offline;
        document.getElementById('chatting_list').innerHTML += page_data.chatting_room_list;
        document.querySelector(".side_bar--body.notice").innerHTML = page_data.notice_data;
        document.querySelector(".setting--user").innerHTML = page_data.curr_user_data;
        set_profile_pic();
        add_user_status_event();
    })
}


function scroll_to_bottom_in_chatting(){
    var scroll_body = document.querySelector('.chat_contents');
    
    scroll_body.scrollTop = scroll_body.scrollHeight;
}

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




// GNB_bnt.addEventListener('click', function(){
    
//     
// });

window.onload = load_curr_user_data();
document.getElementById('user_logout').addEventListener('click', function(e){
    e.preventDefault();
    userLogout();
});

// window.addEventListener('beforeunload', function(e){
//     userLogout();
// })
