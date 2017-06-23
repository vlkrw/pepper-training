var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var exec = require('child_process').exec;
var pepperIP = "10.0.137.152";

app.use(bodyParser.json());
app.set('view engine', 'ejs');
app.use('/', express.static(__dirname + '/views/static'));
app.use('/', express.static(__dirname + '/node_modules'));

app.get('/', function (req, res) {
  res.render('pages/index');
});

app.get('/movement', function (req, res) {
  res.render('pages/movement');
});

app.get('/leds', function (req, res) {
  res.render('pages/leds');
});

app.get('/volume', function (req, res) {
  executeQicliCommand("ALAudioDevice.getOutputVolume").then((result) => res.end(result));
});

app.post('/volume', function (req, res) {
  var volume = parseInt(req.body.value);
  if (volume > 100){
    volume = 100;
  }else if(volume < 0){
    volume = 0;
  }
  console.log("Setting Volume to " + volume);
  executeQicliCommand("ALAudioDevice.setOutputVolume " + volume).then(() => res.end());
});

app.get('/battery', function (req, res) {
  executeQicliCommand("ALBattery.getBatteryCharge").then((result) => res.end(result));
});

app.post('/say', function (req, res) {
  var text = req.body.text;
  if(req.body.animated){
    console.log("Saying with animation: " + text);
    executeQicliCommand('ALAnimatedSpeech.say "'+ text + '"');
  }else{
    console.log("Saying " + text);
    executeQicliCommand('ALTextToSpeech.say "'+ text + '"');
  }
  res.end();
});

app.post('/movement', function (req, res) {
  console.log("Moving: " + req.body.movement);

  switch(req.body.movement){
    case "headleft":
      executeQicliCommand('ALMotion.changeAngles HeadYaw 0.5 0.2');
      break;
    case "headright":
      executeQicliCommand('ALMotion.changeAngles HeadYaw -0.5 0.2');
      break;
    case "headdown":
      executeQicliCommand('ALMotion.changeAngles HeadPitch 0.05 0.05');
      break;
    case "headup":
      executeQicliCommand('ALMotion.changeAngles HeadPitch -0.05 0.05');
      break;
    case "turnleft":
      executeQicliCommand('ALMotion.moveTo 0.0 0.0 0.5 1.0');
      break;
    case "turnright":
      executeQicliCommand('ALMotion.moveTo 0.0 0.0 -0.5 1.0');
      break;
    case "moveforward":
      executeQicliCommand('ALMotion.moveTo 0.1 0.0 0.0 1.0');
      break;
    case "movebackward":
      executeQicliCommand('ALMotion.moveTo -0.1 0.0 0.0 1.0');
      break;
    case "shakehand":
      executeQicliCommand('HandShakeService.giveHand');
      break;
    case "autonomousability":
      var state = req.body.value ? 1 : 0;
      executeQicliCommand("ALAutonomousLife.setAutonomousAbilityEnabled All " + state);
      break;
  }
  console.log(req.body.movement);
  res.end();
});

app.post('/leds', function (req, res) {
  console.log("LEDs");

  switch(req.body.leds){
    case "animation":
      executeQicliCommand("ALLeds.rasta 5");
      break;
    case "eyeanimation":
      executeQicliCommand("ALLeds.randomEyes 5");
      break;
    case "reset":
      executeQicliCommand("ALLeds.reset AllLeds");
      break;
    case "red":
      executeQicliCommand("ALLeds.fadeRGB AllLeds red 1");
      break;
    case "green":
      executeQicliCommand("ALLeds.fadeRGB AllLeds green 1");
      break;
    case "blue":
      executeQicliCommand("ALLeds.fadeRGB AllLeds blue 1");
      break;
    case "eyesred":
      executeQicliCommand("ALLeds.fadeRGB FaceLeds red 1");
      break;
    case "eyesgreen":
      executeQicliCommand("ALLeds.fadeRGB FaceLeds green 1");
      break;
    case "eyesblue":
      executeQicliCommand("ALLeds.fadeRGB FaceLeds blue 1");
      break;
  }
  res.end();
});

app.listen(3000, function () {
  console.log('Pepper app listening on port 3000!');
});

function executeQicliCommand(command){
  return executeCommand("qicli call " + command + " --qi-url " + pepperIP);
}

function executeCommand(command){
  return new Promise(function (fulfill, reject){
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        reject(error);
        return;
      }
      fulfill(stdout);
    });
  }).catch(err => {
    console.error(err.stack);
    return err;
  });
}
