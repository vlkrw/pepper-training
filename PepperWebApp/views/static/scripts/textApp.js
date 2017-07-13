$( document ).ready(function() {
  setNavbarButtonActive("#navbarText");
  setupListeners();
  loadValues();
});

function loadValues(){
  getVolume().then((data) => $("#volumetext").text("Lautstärke: " + data));

  getSavedText().then((text) => {
    if(text.length == 0){
      return;
    }

    textArray = JSON.parse(text);

    while($(".text").length < textArray.length){
      addNewTextCard();
    }

    $( ".text" ).each(function( index ) {
      $(this).find("textarea").val(textArray[index]);
    });
  });
}

function getVolume(){
  return new Promise(function (fulfill, reject){
    $.get("/volume", ((data) => fulfill(data)));
  }).catch(err => {
    console.error(err.stack);
    return err;
  });
}

function getSavedText(){
  return new Promise(function (fulfill, reject){
    $.get("/text", ((data) => fulfill(data)));
  }).catch(err => {
    console.error(err.stack);
    return err;
  });
}

function setupListeners(){
  $('.container').on('click', '.buttonPlay', function() {
    var textToSay = $(this).parent().siblings("textarea").val();
    if(textToSay.length == 0){
      alert("Bitte zuerst einen Text eingeben!");
      return;
    }

    say(textToSay);
  });

  $('.container').on('click', '.buttonRemove', function() {
    var button = $(this);
    BootstrapDialog.show({
        title: 'Bild löschen',
        message: 'Soll dieser Text wirklich gelöscht werden?',
        buttons: [{
          label: 'Ja',
          action: function(dialog) {
            dialog.close();
            var cardAbove = button.parent().parent().prev();
            var cardUnder = button.parent().parent().next();
            if(cardAbove.hasClass("text") || cardUnder.hasClass("text")){
              button.parent().parent().remove();
            }else{
              button.parent().siblings("textarea").val("");
            }
          }
        }, {
          label: 'Nein',
          action: function(dialog) {
              dialog.close();
          }
        }]
    });
  });

  $('.container').on('click', '.buttonMoveUp', function() {
    var cardAbove = $(this).parent().parent().prev();
    if(cardAbove.hasClass("text")){
      cardAbove.before($(this).parent().parent());
    }
  });

  $('.container').on('click', '.buttonMoveDown', function() {
    var cardUnder = $(this).parent().parent().next();
    if(cardUnder.hasClass("text")){
      cardUnder.after($(this).parent().parent());
    }
  });

  $("#buttonAddText").click(function() {
    addNewTextCard();
  });

  $("#buttonSave").click(function() {
    var text = [];
    $( ".text" ).each(function( index ) {
      text.push($(this).find("textarea").val());
    });
    postToServer("/text", JSON.stringify(text)).then(() => {
      $("#save_alert").css('display', 'block');
      setTimeout(function(){$("#save_alert").fadeOut(500)}, 2000);
    });
  });

  $("#buttonVup").click(() => changeVolume(10));
  $("#buttonVdown").click(() => changeVolume(-10));
}

function addNewTextCard(){
  $(".text:last").clone().insertAfter(".text:last");
  $(".text:last textarea").val("");
}

function say(textToSay){
  var data = {};
  data.text = textToSay;
  data.animated = $('#animationCheckbox').is(':checked');

  postToServer("/say", JSON.stringify(data));
}

function changeVolume(changeValue){
  getVolume().then((volume)=>{
    var data = {};
    data.value = parseInt(volume) + changeValue;
    postToServer("/volume", JSON.stringify(data)).then(loadValues);
  });
}

function postToServer(url, data){
  return new Promise(function (fulfill, reject){
    $.ajax({
       type: 'POST',
       data: data,
       contentType: 'application/json',
       url: url,
       success: fulfill
     });
   });
}
