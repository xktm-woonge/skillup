const alerts = document.querySelectorAll('[id^="alert--"]');

alerts.forEach(el => {
  const typeName = el.id.split("--")[1];
  el.addEventListener("click", function(target) {

    console.log(typeName);

    if(typeName == "add_Friend") {
      swal("친구 추가", "이메일 입력", {
        content: {
          element: "input",
          attributes: {
            placeholder: "example@domain.com",
            type: "email",
          },
        },
        buttons: {
          cancel: true,
          confirm: "보내기",
        },
        //closeOnClickOutside: false,
      }).then((value) => {
        if (value) {
          // 데이터처리 웹소켓 추가
          swal(`${value}\n 위 이메일에 친구 신청을 보냈습니다.`);
        }
      });
    } else if(typeName == "withdrawal") {
      swal("탈퇴", "탈퇴하시겠습니까?", "error", {
        buttons: ["취소", "네"],
        dangerMode: true,
      }).then((value) => {
        if (value) {
          // 데이터처리 웹소켓 추가
          swal(`안녕히 가세요...`);
        }
      });
    } else if(typeName == "Delete_all") {
      swal("전체 삭제", "전체 삭제하시겠습니까?", "warning", {
        buttons: ["취소", "네"],
        dangerMode: true,
      }).then((value) => {
        if (value) {
          // 데이터처리 웹소켓 추가
          swal(`삭제했습니다.`);
        }
      });
    }

  })
})