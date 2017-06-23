$( document ).ready(function() {
  setNavbarButtonActive("#navbarMovement");
  setupListeners();
});

function setupListeners(){
  $("#buttonLeft").click(() => postToServer("headleft"));
  $("#buttonRight").click(() => postToServer("headright"));
  $("#buttonUp").click(() => postToServer("headup"));
  $("#buttonDown").click(() => postToServer("headdown"));
  $("#buttonTurnRight").click(() => postToServer("turnright"));
  $("#buttonTurnLeft").click(() => postToServer("turnleft"));
  $("#buttonMoveForward").click(() => postToServer("moveforward"));
  $("#buttonMoveBackward").click(() => postToServer("movebackward"));
}

function postToServer(direction){
  var currentLocation = String(window.location);
  var data = {};
  data.movement = direction;

  $.ajax({
     type: 'POST',
     contentType: 'application/json',
     data: JSON.stringify(data),
     url: currentLocation.substring(0, currentLocation.indexOf('/')) + "movement"
   });
}
