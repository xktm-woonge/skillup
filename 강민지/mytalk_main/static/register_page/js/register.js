function goBack(){
    window.history.back();
}
function submitEmailData(){
    // email 값 전송
    var emailData = new FormData(document.getElementById('register_email'));
    console.log(emailData.get('email'));

    if (emailData.get('email')){
        // REST API
        fetch('/register/send-email/',{
            method:'POST',
            body:emailData
        })
        .then(function(response){
            if(response.ok){
                return response.json();
            } else{
                throw new Error('Error:'+response.status);
            }
        })
        .then(function(data){
            if (data.message === 'Success') {
                alert('이메일을 확인하여 인증 번호를 입력해주세요.');
            } else {
                if (data.error === 'email_duplicate'){
                    alert('이미 가입 된 이메일입니다.');
                } else{
                    alert('이메일 전송에 실패했습니다.');
                }
            }
        })
        .catch(function(error){
            alert('Error:'+error.message);
        })
    } else {
        alert('이메일을 입력하세요.')
    }
}

function disableFormInputs(formId) {
    var form = document.getElementById(formId);
    var inputs = form.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].disabled = true;
    }
}


function confirmEmailCertification(){
    // 입력된 인증 번호 가져오기
    var emailCertNum = new FormData(document.getElementById('register_cert_num'));
    console.log(emailCertNum.get('cert_num'));

    if (emailCertNum.get('cert_num')){
        // 인증 번호 REST API
        fetch('/register/confirm-cert-num/',{
            method:'POST',
            body:emailCertNum
        })
        .then(function(response){
            if(response.ok){
                return response.json();
            } else{
                throw new Error('Error:'+response.status);
            }
        })
        .then(function(data){
            if (data.message === 'Success') {
                disableFormInputs('register_email');
                disableFormInputs('register_cert_num');
                alert('인증번호 확인이 완료되었습니다.');
            } else {
                alert('인증번호 확인에 실패했습니다.');
            }
        })
        .catch(function(error){
            alert('Error:'+error.message);
        })
    } else {
        alert('인증 번호를 입력하세요.')
    }
}

function confirmCurrentEmail(){
    var emailData = new FormData(document.getElementById('register_email'));
    console.log(emailData.get('email'));
    
    if (emailData.get('email')){
        fetch('/register/confirm-email/',{
            method:'POST',
            body:emailData
        })
        .then(function(response){
            if(response.ok){
                return response.json();
            } else{
                throw new Error('Error:'+response.status);
            }
        })
        .then(function(data){
            if (data.message === 'Success') {
                confirmEmailCertification();
            } else {
                alert('이메일이 변경되었습니다. 인증 번호를 재전송 해주세요.');
            }
        })
        .catch(function(error){
            alert('Error:'+error.message);
        })
    } else{
        alert('이메일을 재입력 후 인증 번호를 재전송 해주세요');
    }
}
function addUserInfo(){
    var passwordData = new FormData(document.getElementById('send_user_info'));

    if (pwCheck() && pwIsSame()){
        fetch('/register/add-user/',{
            method:'POST',
            body:passwordData,
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
                alert('회원 가입이 완료되었습니다.')
                window.location.href = '/'
            } else if((data.message === 'Error')&& (data.error === 'cert_error')){
                alert('인증이 완료되지 않았습니다.')
            }
        })
    } else{
        alert('비밀번호를 확인하세요.')
    }
}
function emailCheck(){
    const regExpEmail = /^([0-9a-zA-Z-_\.])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;
    let userEmail = document.querySelector(".email_input");

    if (userEmail.value == ''){
        alert('이메일을 입력해주세요.');
    }
    else if (!regExpEmail.test(userEmail.value)){
        alert('유효한 이메일을 입력해주세요.');
    }
    else {
        submitEmailData();
    }
}

function pwCheck() {
    const regExpPW = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_]).{8,16}$/;
    let userpw = document.getElementById("regi_pw_input");
    let lenLabel = document.getElementById("len_label");
    let regLabel = document.getElementById("reg_label");

    if (userpw.value === ''){
        userpw.classList.remove('fail-box','pass-box');
        lenLabel.classList.remove('fail-txt','pass-txt');
        regLabel.classList.remove('fail-txt','pass-txt');
        return false
    }
    else if (!regExpPW.test(userpw.value)){
        userpw.classList.add('fail-box');
        userpw.classList.remove('pass-box');
        regLabel.classList.add('fail-txt');
        regLabel.classList.remove('pass-txt');
        if (userpw.value.length > 7 && userpw.value.length <17){
            lenLabel.classList.add('pass-txt');
            lenLabel.classList.remove('fail-txt');
        } else{
            lenLabel.classList.add('fail-txt');
            lenLabel.classList.remove('pass-txt');
        }
        return false
    }
    else if (regExpPW.test(userpw.value)){
        userpw.classList.add('pass-box');
        lenLabel.classList.add('pass-txt');
        regLabel.classList.add('pass-txt');
        userpw.classList.remove('fail-box');
        lenLabel.classList.remove('fail-txt');
        regLabel.classList.remove('fail-txt');
        return true
    }
}
function pwIsSame(){
    let userpw = document.getElementById("regi_pw_input");
    let userpwcheck = document.getElementById("regi_pw_conf_input");

    if (userpwcheck.value === ''){
        userpwcheck.classList.remove('fail-box','pass-box');
        return false
    }
    else if (userpw.value === userpwcheck.value){
        userpwcheck.classList.add('pass-box');
        userpwcheck.classList.remove('fail-box');
        return true
    }
    else{
        userpwcheck.classList.add('fail-box');
        userpwcheck.classList.remove('pass-box');
        return false
    }
}

document.getElementById('register_email').addEventListener('submit', function(e){
    e.preventDefault();
    emailCheck();
});

document.getElementById('register_cert_num').addEventListener('submit', function(e){
    e.preventDefault();
    confirmCurrentEmail();
});
document.getElementById('send_user_info').addEventListener('submit', function(e){
    e.preventDefault();
    addUserInfo();
});