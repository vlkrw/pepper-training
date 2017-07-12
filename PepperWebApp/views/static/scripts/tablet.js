$( document ).ready(function() {
  setNavbarButtonActive("#navbarTablet");
  setupListeners();
});

function setupListeners(){
  $('#imageInput').change(function() {
    $('#imageForm').submit();
  });

  $("#buttonShow").click(() => {
    postToServer("logo");
  });

  $("#buttonHide").click(() => {
    postToServer("");
  });

  loadImages();
}

function loadImages(){
  $.get("/imagenames", ((jsonResponse) => {
    var imagenames = JSON.parse(jsonResponse);
    imagenames.forEach(imageName => {
      $("#images").append('<div class="card"><img class="card-img-top" src="/' + imageName + '" alt="Card image cap"><a id="buttonShow" class="btn btn-raised btn-primary btn-sm">Anzeigen</span><div class="ripple-container"></div></a><a id="buttonDelete" class="btn btn-raised btn-danger btn-sm">Löschen</span><div class="ripple-container"></div></a></div>');
    });
  }));
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
