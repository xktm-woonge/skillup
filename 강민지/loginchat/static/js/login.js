// 로그인 실패 
function loginFail(message){
    alert(message);
}

// 아이디 중복 확인
function idOverlapCheck() {
    console.log('구현중');
}

// 아이디 정규식 확인
function idCheck() {
    const regExpID = /^[a-z]+[a-z0-9]{5,19}$/g;
    const regExpEng = /^[a-z]$/g;
    let userid = document.getElementById('userID');
    let sendIdMessage = document.getElementById('verifyID');
    let message, result;

    if (userid.value == '') {
        result = 'none';
        message = '영문으로 시작하는 영문, 숫자 조합 6~20자리';
    }
    else if (regExpID.test(userid.value)){
        result = 'pass';
        message = '아이디 적합성 확인';
    }
    else if(userid.value.length === 1 && !regExpEng.test(userid.value)){
        result = 'fail';
        message = '아이디는 영문으로 시작해야 합니다.';
        console.log(regExpEng.lastIndex);
    }
    else{
        result = 'fail';
        message = '영문으로 시작하는 영문, 숫자 조합 6~20자리';
    }
    userid.className = 'input-' + result + '-box';
    sendIdMessage.className = 'input-' + result + '-text';
    sendIdMessage.innerHTML = message;
}

// 비밀번호 정규식 확인
function pwCheck() {
    const regExpPW = /^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]).{8,16}$/g;
    let userpw = document.getElementById('userPW');
    let sendPWMessage = document.getElementById('verifyPW');
    let message, result;
    
    if (userpw.value == ''){
        result = 'none';
        message = '영문, 숫자, 특수 문자가 포함 8~16자리';
    }
    else if (regExpPW.test(userpw.value)){
        result = 'pass';
        message = '비밀번호 성공!';
    }
    else if (userpw.value.length < 8){
        result = 'fail';
        message = '비밀번호가 너무 짧습니다.';
    }
    else if (userpw.value.length > 16){
        result = 'fail';
        message = '비밀번호가 너무 깁니다.';
    }
    else{
        result = 'fail';
        message = '영문, 숫자, 특수 문자가 포함 되어야 합니다.';
    }
    userpw.className = 'input-' + result + '-box';
    sendPWMessage.className = 'input-' + result + '-text';
    sendPWMessage.innerHTML = message;
}

// 비밀번호 확인
function pwIsSame(){
    let userpw = document.getElementById('userPW');
    let confirmpw = document.getElementById('confirmPW');
    let sendConfMessage = document.getElementById('isSame');
    let message, result;

    if(confirmpw.value == ''){
        result = 'none';
        message = '';
    }
    else if (userpw.value != confirmpw.value){
        result = 'fail';
        message = '비밀번호가 다릅니다.';
    }
    else{
        result = 'pass';
        message = '비밀번호가 같습니다.';
    }
    confirmpw.className = 'input-' + result + '-box';
    sendConfMessage.className = 'input-' + result + '-text';
    sendConfMessage.innerHTML = message;
}

// 이름 정규식 확인
function nameCheck(){
    const regExpName = /^[a-zA-Zㄱ-힣][a-zA-Zㄱ-힣]{1,19}$/;
    let userName = document.getElementById('userName');
    let sendNameMessage = document.getElementById('verifyName');
    let message, result;

    if (userName.value == ''){
        result = 'none';
        message = '이름을 입력해주세요.';
    }
    else if (regExpName.test(userName.value)){
        result = 'pass';
        message = ''
    }
    else if (userName.value.length < 2 || userName.value.length > 20){
        result = 'fail';
        message = '이름은 2~20글자 사이';
    }
    else {
        result = 'fail';
        message = '영문 및 한글만 사용 가능합니다.';
    }
    
    userName.className = 'input-' + result + '-box';
    sendNameMessage.className = 'input-' + result + '-text';
    sendNameMessage.innerHTML = message;
}

// 이메일 정규식 확인
function emailCheck(){
    const regExpEmail = /^([0-9a-zA-Z-_\.])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;
    let useremail = document.getElementById('userEmail');
    let sendEmailMessage = document.getElementById('verifyEmail');
    let message, result;

    if (useremail.value == ''){
        result = 'none';
        message = '이메일 주소를 입력해주세요.';
    }
    else if (regExpEmail.test(useremail.value)){
        result = 'pass';
        message = '이메일 주소 확인 완료';
    }
    else {
        result = 'fail';
        message = '이메일 주소를 정확하게 입력해주세요.';
    }

    useremail.className = 'input-' + result + '-box';
    sendEmailMessage.className = 'input-' + result + '-text';
    sendEmailMessage.innerHTML = message;
}

// 클래스 변경
function changeToFail(arrLen, targetclass){
    for(let i = 0; i < arrLen; i++){
        document.getElementsByClassName('input-none-'+ targetclass)[0].className = 'input-fail-' + targetclass;
    }
}

// 회원 가입 폼 정상 작성 확인
// 이벤트 삭제 필요
function verifyInput(){
    const submitbtn = document.getElementById('signup-form');
    let noneBox = document.getElementsByClassName('input-none-box');
    let noneText = document.getElementsByClassName('input-none-text');
    
    function stopsubmit(e){
        if (document.getElementsByClassName('input-pass-box').length < 5){
            e.preventDefault();
        }
        if (noneBox.length > 0){
            changeToFail(noneBox.length, 'box');
            changeToFail(noneText.length, 'text');
        }
    }
    // submitbtn.removeEventListener("submit", stopsubmit);
    submitbtn.addEventListener("submit", stopsubmit, {once:true});
    document.getElementsByClassName('input-fail-box').title = 'ddd';
}