
window.addEventListener("DOMContentLoaded", function () {

  const GNB = document.querySelectorAll("#gnb .btn");
  const GNB_SIDES = document.querySelectorAll("#side_bar .side_bar--tab");

  /*** side_bar on/off ***/
  GNB.forEach((e) =>
    e.addEventListener("click", function () {
      const CLICKED_CLASS = this.classList;
      if (!CLICKED_CLASS.contains("active")) {
        GNB.forEach((el) => el.classList.remove("active"));
        GNB_SIDES.forEach((el) => el.classList.remove("active"));
        CLICKED_CLASS.add("active");
        document.getElementById("side_bar_" + this.id).classList.add("active");
      }
    })
  );
  
});

const NOTICES = document.querySelector(".side_bar--body.notice");
const NOTICE_TYPE = NOTICES.querySelectorAll(".notice--type");
const NOTICE_ICONS = NOTICES.querySelectorAll(".system img, .danger img");

//if (NOTICES)
NOTICE_ICONS.forEach((e) => {
  e.classList.add("icon");
  e.alt = "System Type Icon";
});