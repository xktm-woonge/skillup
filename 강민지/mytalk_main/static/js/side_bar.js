const NOTICES = document.querySelector(".side_bar--body.notice");
const NOTICE_TYPE = NOTICES.querySelectorAll(".notice--type");
const NOTICE_ICONS = NOTICES.querySelectorAll(".system img, .danger img");

//if (NOTICES)
  NOTICE_ICONS.forEach((e) => {
    e.classList.add("icon");
    e.alt = "System Type Icon";
  });