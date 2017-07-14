var express = require('express');
var router = express.Router();

var utils = require('./../utils/utils');

router.get('/leds', function (req, res) {
  res.render('pages/leds');
});

router.post('/leds', function (req, res) {
  console.log("LEDs");

  switch(req.body.leds){
    case "animation":
      utils.executeQicliCommand("ALLeds.rasta 5");
      break;
    case "eyeanimation":
      utils.executeQicliCommand("ALLeds.randomEyes 5");
      break;
    case "reset":
      utils.executeQicliCommand("ALLeds.reset AllLeds");
      break;
    case "red":
      utils.executeQicliCommand("ALLeds.fadeRGB AllLeds red 1");
      break;
    case "green":
      utils.executeQicliCommand("ALLeds.fadeRGB AllLeds green 1");
      break;
    case "blue":
      utils.executeQicliCommand("ALLeds.fadeRGB AllLeds blue 1");
      break;
    case "eyesred":
      utils.executeQicliCommand("ALLeds.fadeRGB FaceLeds red 1");
      break;
    case "eyesgreen":
      utils.executeQicliCommand("ALLeds.fadeRGB FaceLeds green 1");
      break;
    case "eyesblue":
      utils.executeQicliCommand("ALLeds.fadeRGB FaceLeds blue 1");
      break;
  }
  res.end();
});

module.exports = router;
