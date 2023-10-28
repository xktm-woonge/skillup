function goBack(){
    window.history.back();
}
function submitEmailData(){
    // email 값 전송
    var emailData = new FormData(document.getElementById('register_email'));
    console.log(emailData.get('email'));

    if (emailData.get('email')){
        // REST API
        fetch('/register/sendEmail_api/',{
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

    if (emailCertNum.get('cert_num')){
        // 인증 번호 REST API
        fetch('/register/confirmCertNum_api/',{
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
    
    if (emailData.get('email')){
        fetch('/register/confirmEmail_api/',{
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
        fetch('/register/addUser_api/',{
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
                alert('인증이 완료되지 않았습니다. 인증을 진행해주세요.')
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
    let lenLabel = document.getElementById("pw_len");
    let regLabel = document.getElementById("pw_reg");
    let regClassList = [userpw, lenLabel, regLabel];

    if (userpw.value === ''){
        regClassList.forEach(regClass => {
            regClass.classList.remove('checker_fail','checker_pass');
            regClass.classList.add('checker_none');
        });
        return false
    }
    else if (!regExpPW.test(userpw.value)){
        userpw.classList.add('checker_fail');
        userpw.classList.remove('checker_pass', 'checker_none');
        regLabel.classList.add('checker_fail');
        regLabel.classList.remove('checker_pass','checker_none');
        if (userpw.value.length > 7 && userpw.value.length <17){
            lenLabel.classList.add('checker_pass');
            lenLabel.classList.remove('checker_fail', 'checker_none');
        } else{
            lenLabel.classList.add('checker_fail');
            lenLabel.classList.remove('checker_pass', 'checker_none');
        }
        return false
    }
    else if (regExpPW.test(userpw.value)){
        regClassList.forEach(regClass =>{
            regClass.classList.add('checker_pass');
            regClass.classList.remove('checker_fail', 'checker_none');
        })
        return true
    }
}
function pwIsSame(){
    let userpw = document.getElementById("regi_pw_input");
    let userpwcheck = document.getElementById("regi_pw_conf_input");
    let sameLabel = document.getElementById("pw_same");

    if (userpwcheck.value === ''){
        userpwcheck.classList.remove('checker_fail','checker_pass');
        sameLabel.classList.remove('checker_fail', 'checker_pass');
        sameLabel.classList.add('checker_none');
        return false
    }
    else if (userpw.value === userpwcheck.value){
        [userpwcheck, sameLabel].forEach(regClass =>{
            regClass.classList.add('checker_pass');
            regClass.classList.remove('checker_fail', 'checker_none');
        })
        return true
    }
    else{
        [userpwcheck, sameLabel].forEach(regClass =>{
            regClass.classList.add('checker_fail');
            regClass.classList.remove('checker_pass', 'checker_none');
        })
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
window.addEventListener('DOMContentLoaded', function(e){
    document.getElementById('able_login').style.display = 'none'
})