const selectorBtn = document.querySelector("#friend_selector");
const checkedNum = document.querySelector(".group--selector .profile span");
const chatName = document.querySelector(".group--selector input");
const startBtn = document.querySelector(".btn--start");

selectorBtn.addEventListener("click", function () {
  checkboxToggle();
  checkedNum.textContent = "+ 0";
});
startBtn.addEventListener("click", function(){
	const chatConv = document.querySelectorAll("input:checked");
	let is_send = true;
	if (chatConv.length == 1){
		socket.send(JSON.stringify({"message":"enter_chat_from_friends", "friend_name":chatConv[0].id}))
	} else {
		let userNames = []
		chatConv.forEach((user)=>{
			if (user.id == "TED"){
				swal("", "CHATBOT과는 그룹 채팅을 할 수 없습니다.", "warning");
				user.checked = false;
				is_send = false;
			} else{
				userNames.push(user.id);
			}
		})
		if(is_send && chatConv.length != 1){
			socket.send(JSON.stringify({"message":"make_group_chat", "users":userNames}));
		}
	}
	if(is_send) {checkboxToggle();}
});


function checkboxToggle() {
	const checkboxes = document.querySelectorAll(".group--checkbox");
	checkboxes.forEach((checkbox) => {
		checkbox.disabled = !checkbox.disabled;
		if (checkbox.disabled) {checkbox.checked = false;}
		checkbox.addEventListener("change", function(){
			countChecked();	
		});
	});
	
	document.querySelector(".side_bar--tab.active .group--selector").classList.toggle('active');
	const startBtn = document.querySelector(".btn--start");
}

function countChecked() {
  const checkedCount = document.querySelectorAll(":checked").length -1;
  checkedNum.textContent = "+ " + checkedCount;
}