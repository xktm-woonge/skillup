let side_bar_class = Array.from(document.getElementsByClassName('side_bar--tab'))
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


function set_profile_pic() {
    const userImgs = document.querySelectorAll(".profile");
    userImgs.forEach(function(userImg) {
        let profilePictureUrl = userImg.dataset.image || 'profile_basic.png';
        userImg.style.background = `url('../static/img/${profilePictureUrl}') center / cover`;
    });
}

function add_user_edit_event(){
    document.querySelector('.user--cover__edit').addEventListener('click', function(e){
        e.preventDefault();
        document.querySelector('.user--status_message').disabled = false;
    })
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
        document.querySelector(".side_bar--body.room").innerHTML +=page_data.chatting_room_list;
        document.querySelector(".side_bar--body.notice").innerHTML = page_data.notice_data;
        document.querySelector(".setting--user").innerHTML = page_data.curr_user_data;
        set_profile_pic();
        add_user_edit_event();
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
