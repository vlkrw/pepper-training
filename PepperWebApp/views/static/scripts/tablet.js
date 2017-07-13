$( document ).ready(function() {
  setNavbarButtonActive("#navbarTablet");
  setupListeners();
  loadImages();
});

function setupListeners(){
  $('#imageInput').change(function() {
    $('#imageForm').submit();
  });

  $("#buttonHide").click(() => {
    postToServer("", "showimage");
  });

  $('.container').on('click', '.buttonShow', function() {
    postToServer($(this).siblings("img").attr("src"), "showimage");
  });

  $('.container').on('click', '.buttonDelete', function() {
    var button = $(this);
    BootstrapDialog.show({
        title: 'Bild löschen',
        message: 'Soll dieses Bild wirklich gelöscht werden?',
        buttons: [{
          label: 'Ja',
          action: function(dialog) {
            dialog.close();
            postToServer(button.siblings("img").attr("src"), "removeimage");
            button.parent().remove();            
          }
        }, {
          label: 'Nein',
          action: function(dialog) {
              dialog.close();
          }
        }]
    });
  });
}

function loadImages(){
  $.get("/imagenames", ((jsonResponse) => {
    var imagenames = JSON.parse(jsonResponse);
    imagenames.forEach(imageName => {
      $("#images").append('<div class="card"><img class="card-img-top" src="/' + imageName + '" alt="Card image cap"><a id="buttonShow" class="btn btn-raised btn-primary btn-sm buttonShow">Anzeigen</span><div class="ripple-container"></div></a><a id="buttonDelete" class="btn btn-raised btn-danger btn-sm buttonDelete">Löschen</span><div class="ripple-container"></div></a></div>');
    });
  }));
}

function postToServer(name, url){
  var currentLocation = String(window.location);
  var data = {};
  data.name = name;

  $.ajax({
     type: 'POST',
     contentType: 'application/json',
     data: JSON.stringify(data),
     url: currentLocation.substring(0, currentLocation.indexOf('/')) + url
   });
}
