function userLogin() {
    var loginUserData = new FormData(
        document.getElementById("send_login_user_info")
    );
    // console.log(loginUserData.get("email") + loginUserData.get("password"));

    fetch("/login_api/", {
        method: "POST",
        body: loginUserData,
    })
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Error:" + response.status);
        }
    })
    .then(function (data) {
        if (data.message === "Success") {
            window.location.href = "/main";
        } else if (data.message === "Error" && data.error === "login_fail") {
            alert("이메일 또는 비밀번호가 맞지 않습니다.");
        }
    });
}

document
    .getElementById("send_login_user_info")
    .addEventListener("submit", function (e) {
        e.preventDefault();
        userLogin();
    });


window.addEventListener("DOMContentLoaded", function (e) {
    const VISION_CHECK = document.getElementById("vision");
    const PASSWORD_INPUT = document.querySelector('input[name="password"]');
    const VISION_ICONS = document.querySelectorAll(".vision__icon");

    VISION_ICONS.forEach((el) => {
        el.addEventListener("click", function () {
            VISION_CHECK.checked
                ? (PASSWORD_INPUT.type = "password")
                : (PASSWORD_INPUT.type = "text");
        });
    });
});
