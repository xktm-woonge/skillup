const userId = document.body.dataset.userId;
const socket = new WebSocket(`ws://127.0.0.1:8000/ws/main/${userId}/`);

// 웹소켓 통신으로 변경할 함수

socket.onmessage = function(e){
    let message = JSON.parse(e.data);
    // console.log(message);
    // user 가 로그인되지 않은 경우
    if(message.message === 'user_auth_error'){
        console.log('유저 인증 에러');
    }
    // 각 메세지에 따라 실행 함수 변경
    else if (['send_message', 'recive_mesaage'].indexOf(message.message) !== -1){
        console.log('넘어왔어?'+message.message);
        let roomnum = message.data.add_data['roomnum'];
        document.getElementsByClassName('chat--body')[0].innerHTML += add_message_box(message);
        scroll_to_bottom_in_chatting();
        document.getElementById(`room_num_${roomnum}`).querySelector('.room__status').textContent = message.data.add_data['last_message'];
    }
    else if (message === 'change_friend_status'){
        change_friend_status('name')
    }
}


function change_friend_status(user_name){

}

// message box 추가하는 함수
function add_message_box(data){
    let message_box_template = MESSAGE_BOX;
    let messageBoxItem = data.data;
    let messageBoxHTML = applyTemplate(message_box_template, messageBoxItem);
    return messageBoxHTML;
}

// form data를 json 형식으로 변경하여 전달하는 함수
function trans_form_data_to_json(formData){
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });
    return JSON.stringify(jsonData);
}

// message를 websocket을 통해 보내는 함수
function send_message() {
    let send_message_data = new FormData(document.getElementById('send_message'));
    let room_num = send_message_data.get('room_number');

    if (send_message_data.get('send_text')){
        send_message_data.append('message', 'send_message');
        send_message_data = trans_form_data_to_json(send_message_data);
        socket.send(send_message_data);
        document.querySelector('.chat--footer__text').value = '';
    }
}


// user의 상태가 변경되었을 때 적용 함수
function add_user_status_event() {
    document.querySelector('.activeSet').addEventListener('change', function(e) {
        let send_data = JSON.stringify({'message':'change_user_status','changed_status': e.target.value});
        socket.send(send_data);
    });
}


// 메세지를 보내는 함수
function add_event() {
    document.getElementById('send_message').addEventListener('submit', function(e) {
        e.preventDefault();
        send_message();
    });
    document.querySelector('.chat--footer__text').addEventListener('keydown', function(e) {
        if (e.key === 'Enter'){
            e.preventDefault();
            send_message();
        }
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