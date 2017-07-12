var buttonIds = ["#navbarText", "#navbarMovement", "#navbarLed", "#navbarTablet"];

function setNavbarButtonActive(id){
  buttonIds.forEach((buttonId) => {
    $(buttonId).removeClass("active");
  });
  $(id).addClass("active");
}
