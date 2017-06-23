var buttonIds = ["#navbarText", "#navbarMovement", "#navbarLed"];

function setNavbarButtonActive(id){
  buttonIds.forEach((buttonId) => {
    $(buttonId).removeClass("active");
  });
  $(id).addClass("active");
}
