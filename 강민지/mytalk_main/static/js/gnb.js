/** side_bar on/off  */
window.addEventListener("DOMContentLoaded", function () {
  const gnbButtons = document.querySelectorAll("#gnb .btn");
  const gnbSides = document.querySelectorAll("#side_bar .side_bar--tab");
  const notices = document.querySelector(".side_bar--body.notice");
  const noticeIcons = notices.querySelectorAll(".system img, .danger img");

  gnbButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const clickedClass = this.classList;
      const sideBarId = document.getElementById("side_bar_" + this.id);
      //const activeDrop = sideBarId.querySelector(".side_bar--header--btn");

      if (!clickedClass.contains("active")) {
        removeActiveClass(gnbButtons);
        removeActiveClass(gnbSides);
        clickedClass.add("active");
        sideBarId.classList.add("active");
      }

      //console.log(sideBarId, activeDrop);

      //activeDrop.addEventListener("click", toggleNextSiblingDisplayNone);
    });
  });

  noticeIcons.forEach((icon) => {
    icon.classList.add("icon");
    icon.alt = "System Type Icon";
  });
});

function removeActiveClass(elements) {
  elements.forEach((el) => el.classList.remove("active"));
}

function toggleNextSiblingDisplayNone(event) {
  const dropdownButtons = document.querySelectorAll(".side_bar--header--btn");
  console.log(dropdownButtons);
  event.currentTarget.nextElementSibling?.classList.toggle("displayNone");
}
