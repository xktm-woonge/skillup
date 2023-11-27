const alerts = document.querySelectorAll('[id^="alert--"]');
const regExpEmail = /^([0-9a-zA-Z-_\.])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;

function openEmailSwal(){
	swal("친구 추가", "이메일 입력", {
		content: {
			element: "input",
			attributes: {
				placeholder: "example@domain.com",
				type: "email",
			},
		}
	})
	.then((value) => {
		print(value);
		if(value){
			if (!regExpEmail.test(value)) {
				swal("", "올바른 이메일 주소를 입력하세요.","error", {
					buttons: ["취소", "재입력"],
				})
				.then((isRetry) => {
					if (isRetry) {
						openEmailSwal();
					}
				});
			} else {
				userEmailConform(value);
			}
		}
	})
}

alerts.forEach(el => {
	const typeName = el.id.split("--")[1];
	el.addEventListener("click", function(target) {

		console.log(typeName);
		if (typeName == "add_Friend") {
			openEmailSwal();
		} else if(typeName == "withdrawal") {
			swal("탈퇴", "탈퇴하시겠습니까?", "error", {
				buttons: ["취소", "네"],
				dangerMode: true,
			}).then((value) => {
				if (value) {
				// 데이터처리 웹소켓 추가
				swal(`지금 버전에서는 탈퇴 기능을 지원하지 않습니다.`);
				}
			});
		} else if(typeName == "Delete_all") {
			swal("전체 삭제", "전체 삭제하시겠습니까?", "warning", {
				buttons: ["취소", "네"],
				dangerMode: true,
			}).then((value) => {
				if (value) {
				swal(`삭제했습니다.`);
				deleteNoticeAll();
				}
			});
		} else if (typeName == "Accept_all") {
			userCount = document.querySelectorAll(".notice--group.friends").length;
			swal("전체 수락", `${userCount}명의 친구 신청을 수락하시겠습니까?`, {
			  buttons: ["취소", "네"],
			}).then((value) => {
				if (value) {
					swal(`수락했습니다.`);
					acceptFriendAll();
				}
			});
		} else if (typeName == "Accept") {
			swal("친구 신청 수락 완료");
		} else if (typeName == "Add_comment") {
			changeSideBar("friends");
			checkboxToggle();
		} else {
			swal("typeName");
		}
	})
})
function deleteNoticeAll(){
  const notices = document.querySelectorAll(".notice--group:not(.friends)");
	notices.forEach(function(notice){
		let noticeNum = findNumInClassName(notice.classList);
		socket.send(JSON.stringify({"message":"delete_notice", "noti_num":noticeNum}));
	})
}

function acceptFriendAll(){
	const friendsRequest = document.querySelectorAll(".notice--group.friends");
	friendsRequest.forEach(function(notice){
		let friendNotiNum = findNumInClassName(notice.classList);
		socket.send(JSON.stringify({"message": "accept_friend", "noti_num": friendNotiNum}));
	})
}