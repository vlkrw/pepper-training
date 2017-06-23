$( document ).ready(function() {
  setNavbarButtonActive("#navbarText");
  setupListeners();
});

function setupListeners(){
  var currentLocation = String(window.location);
  $( "#buttonStart" ).click(function() {
    var textToSay = $("#text").val();
    if(textToSay.length == 0){
      alert("Bitte zuerst einen Text eingeben!");
      return;
    }

    textArray = [textToSay];

    $.ajax({
       type: 'POST',
       data: JSON.stringify(textArray),
       contentType: 'application/json',
       url: currentLocation.substring(0, currentLocation.indexOf('/')) + "say"
     });
  });
}
