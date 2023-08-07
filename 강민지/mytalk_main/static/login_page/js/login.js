function userLogin(){
    var loginUserData = new FormData(document.getElementById('send_login_user_info'));
    console.log(loginUserData.get('email')+loginUserData.get('password'));

    // if (loginUserData.get('email') === ''){
    //     alert('이메일을 입력해주세요.')
    // } else if(loginUserData.get('password') === ''){
    //     alert('비밀 번호를 입력해주세요.')
    // } if{
        fetch('/login_api/',{
            method:'POST',
            body:loginUserData,
        })
        .then(function(response){
            if(response.ok){
                return response.json();
            } else{
                throw new Error('Error:'+response.status);
            }
        })
        .then(function(data){
            if (data.message === 'Success'){
                window.location.href = '/main'
            } else if((data.message === 'Error')&& (data.error === 'login_fail')){
                alert('이메일 또는 비밀번호가 맞지 않습니다.')
            }
        })
    // }
}

document.getElementById('send_login_user_info').addEventListener('submit', function(e){
    e.preventDefault();
    userLogin();
})