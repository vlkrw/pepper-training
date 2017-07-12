$( document ).ready(function() {
  setNavbarButtonActive("#navbarLed");
  setupListeners();
});

function setupListeners(){
  $("#buttonAnimation").click(() => postToServer("animation"));
  $("#buttonEyeAnimation").click(() => postToServer("eyeanimation"));
  $("#buttonReset").click(() => postToServer("reset"));
  $("#buttonRed").click(() => postToServer("red"));
  $("#buttonGreen").click(() => postToServer("green"));
  $("#buttonBlue").click(() => postToServer("blue"));
  $("#buttonEyesRed").click(() => postToServer("eyesred"));
  $("#buttonEyesGreen").click(() => postToServer("eyesgreen"));
  $("#buttonEyesBlue").click(() => postToServer("eyesblue"));
}

function postToServer(type){
  var currentLocation = String(window.location);
  var data = {};
  data.leds = type;

  $.ajax({
     type: 'POST',
     contentType: 'application/json',
     data: JSON.stringify(data),
     url: currentLocation.substring(0, currentLocation.indexOf('/')) + "leds"
   });
}
