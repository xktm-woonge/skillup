const selectorBtn = document.querySelector("#friend_selector");
const checkedNum = document.querySelector(".group--selector .profile span");
const startBtn = document.querySelector(".btn--start");

selectorBtn.addEventListener("click", function () {
  checkboxToggle();
  checkedNum.textContent = "+ 0";
});
startBtn.addEventListener("click", checkboxToggle);

function checkboxToggle() {
  const checkboxes = document.querySelectorAll(".group--checkbox");
  checkboxes.forEach((checkbox) => {
    checkbox.disabled = !checkbox.disabled;
    if (checkbox.disabled) {checkbox.checked = false;}
    checkbox.addEventListener("change", countChecked);
  });
  
  document.querySelector(".side_bar--tab.active .group--selector").classList.toggle('active');

  const startBtn = document.querySelector(".btn--start");
}

function countChecked() {
  const checkedCount = document.querySelectorAll(":checked").length -1;
  checkedNum.textContent = "+ " + checkedCount;
}

