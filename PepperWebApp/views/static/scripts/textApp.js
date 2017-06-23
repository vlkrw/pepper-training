$( document ).ready(function() {
  setNavbarButtonActive("#navbarText");
  setupListeners();
  loadValues();
});

function loadValues(){
  getVolume().then((data) => $("#volumetext").text("Lautstärke: " + data));
}

function getVolume(){
  return new Promise(function (fulfill, reject){
    $.get("/volume", ((data) => fulfill(data)));
  }).catch(err => {
    console.error(err.stack);
    return err;
  });
}

function setupListeners(){
  $("#buttonStart").click(function() {
    var textToSay = $("#text").val();
    if(textToSay.length == 0){
      alert("Bitte zuerst einen Text eingeben!");
      return;
    }

    var data = {};
    data.text = textToSay;
    data.animated = $('#animationCheckbox').is(':checked');

    postToServer("/say", JSON.stringify(data));
  });

  $("#buttonVup").click(() => changeVolume(10));
  $("#buttonVdown").click(() => changeVolume(-10));
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
