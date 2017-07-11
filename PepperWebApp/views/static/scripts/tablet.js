$( document ).ready(function() {
  setNavbarButtonActive("#navbarTablet");
  setupListeners();
});

function setupListeners(){
  $("#buttonShow").click(() => {
    postToServer("logo");
  });

  $("#buttonHide").click(() => {
    postToServer("");
  });
}

function postToServer(name){
  var currentLocation = String(window.location);
  var data = {};
  data.name = name;

  $.ajax({
     type: 'POST',
     contentType: 'application/json',
     data: JSON.stringify(data),
     url: currentLocation.substring(0, currentLocation.indexOf('/')) + "image"
   });
}
