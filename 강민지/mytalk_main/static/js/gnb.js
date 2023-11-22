const gnbButtons = document.querySelectorAll("#gnb .btn");
const gnbSides = document.querySelectorAll("#side_bar .side_bar--tab");
const notices = document.querySelector(".side_bar--body.notice");
const noticeIcons = notices.querySelectorAll(".system img, .danger img");
const dropdownButtons = document.querySelectorAll(".side_bar--header__btn");
const dropdownInnerButtons = document.querySelectorAll(".side_bar--header__dropdown li");

gnbButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const clickedClass = this.classList;
    const sideBarId = document.getElementById("side_bar_" + this.id);

    if (!clickedClass.contains("active")) {
      removeActiveClass(gnbButtons);
      removeActiveClass(gnbSides);
      closeDropdowns();
      clickedClass.add("active");
      sideBarId.classList.add("active");
    }
  });
});

noticeIcons.forEach((icon) => {
  icon.classList.add("icon");
  icon.alt = "System Type Icon";
});


dropdownButtons.forEach((el) => {
  el.addEventListener("click", function () {
    el.nextElementSibling.classList.toggle("active");
  });
});

dropdownInnerButtons.forEach(el => {
  el.addEventListener("click", function(){
    closeDropdowns();
  })
})

function removeActiveClass(elements) {
  elements.forEach((el) => el.classList.remove("active"));
}

function closeDropdowns() {
  dropdownButtons.forEach((el) => {
    el.nextElementSibling.classList.remove("active");
  });
}
