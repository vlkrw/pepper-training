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

app.post('/say', function (req, res) {
  console.log("Saying " + req.body);
  executeQicliCommand('call ALAnimatedSpeech.say "'+ req.body[0] + '"');
  res.end();
});

app.post('/movement', function (req, res) {
  console.log("Moving: " + req.body.movement);

  switch(req.body.movement){
    case "headleft":
      executeQicliCommand('call ALMotion.changeAngles HeadYaw 0.5 0.2');
      break;
    case "headright":
      executeQicliCommand('call ALMotion.changeAngles HeadYaw -0.5 0.2');
      break;
    case "headdown":
      executeQicliCommand('call ALMotion.changeAngles HeadPitch 0.05 0.05');
      break;
    case "headup":
      executeQicliCommand('call ALMotion.changeAngles HeadPitch -0.05 0.05');
      break;
    case "turnleft":
      executeQicliCommand('call ALMotion.moveTo 0.0 0.0 0.5 1.0');
      break;
    case "turnright":
      executeQicliCommand('call ALMotion.moveTo 0.0 0.0 -0.5 1.0');
      break;
    case "moveforward":
      executeQicliCommand('call ALMotion.moveTo 0.1 0.0 0.0 1.0');
      break;
    case "movebackward":
      executeQicliCommand('call ALMotion.moveTo -0.1 0.0 0.0 1.0');
      break;
  }
  res.end();
});

app.post('/leds', function (req, res) {
  console.log("LEDs");

  switch(req.body.leds){
    case "animation":
      executeQicliCommand("call ALLeds.rasta 5");
      break;
    case "eyeanimation":
      executeQicliCommand("call ALLeds.randomEyes 5");
      break;
    case "reset":
      executeQicliCommand("call ALLeds.reset AllLeds");
      break;
    case "red":
      executeQicliCommand("call ALLeds.fadeRGB AllLeds red 1");
      break;
    case "green":
      executeQicliCommand("call ALLeds.fadeRGB AllLeds green 1");
      break;
    case "blue":
      executeQicliCommand("call ALLeds.fadeRGB AllLeds blue 1");
      break;
    case "eyesred":
      executeQicliCommand("call ALLeds.fadeRGB FaceLeds red 1");
      break;
    case "eyesgreen":
      executeQicliCommand("call ALLeds.fadeRGB FaceLeds green 1");
      break;
    case "eyesblue":
      executeQicliCommand("call ALLeds.fadeRGB FaceLeds blue 1");
      break;
  }
  res.end();
});

app.listen(3000, function () {
  console.log('Pepper app listening on port 3000!');
});

function getBatteryCharge(){
  return executeQicliCommand("call ALBattery.getBatteryCharge");
}

function executeQicliCommand(command){
  return executeCommand("qicli " + command + " --qi-url " + pepperIP);
}

function executeCommand(command){
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return error;
    }
    return stdout;
  });
}
