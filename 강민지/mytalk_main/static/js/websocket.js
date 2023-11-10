let socket = new WebSocket("ws://localhost:8000/ws/main/"); // ws:// 이후의 주소는 routing.py 의 경로


// 웹소켓 통신으로 변경할 함수


// user의 상태가 변경되었을 때 적용 함수
function add_user_status_event() {
    document.querySelector('.activeSet').addEventListener('change', function(e) {
        let changed_status = {'changed_status': e.target.value};
        fetch('/main/user_active_set_api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,  // CSRF 토큰을 헤더에 추가
            },
            body: JSON.stringify(changed_status),
        })
        .then(function(response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error: ' + response.status);
            }
        })
        .then(function(data) {
            console.log(data);  // 성공적으로 처리된 응답 데이터
            // 원하는 추가 동작 수행
        })
        .catch(function(error) {
            console.error('Request failed', error); // 요청 실패 시 오류 처리
        });
    });
}

// 메세지를 보내는 함수
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
            document.getElementById(`room_num_${room_num}`).querySelector('.room__status').textContent = data.last_message;
            if(!data.is_chatbot_conv){conv_chatbot(send_message_data, room_num)};
        })
    }
}

// 챗봇에게 메세지를 받는 함수
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
        document.getElementById(`room_num_${roomnum}`).querySelector('.room__status').textContent = data.last_message;
    })
}