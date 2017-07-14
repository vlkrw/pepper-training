var express = require('express');
var router = express.Router();

var utils = require('./../utils/utils');

router.get('/movement', function (req, res) {
  res.render('pages/movement');
});

router.post('/movement', function (req, res) {
  console.log("Moving: " + req.body.movement);

  switch(req.body.movement){
    case "headleft":
      utils.executeQicliCommand('ALMotion.changeAngles HeadYaw 0.5 0.2');
      break;
    case "headright":
      utils.executeQicliCommand('ALMotion.changeAngles HeadYaw -0.5 0.2');
      break;
    case "headdown":
      utils.executeQicliCommand('ALMotion.changeAngles HeadPitch 0.05 0.05');
      break;
    case "headup":
      utils.executeQicliCommand('ALMotion.changeAngles HeadPitch -0.05 0.05');
      break;
    case "turnleft":
      utils.executeQicliCommand('ALMotion.moveTo 0.0 0.0 0.5 1.0');
      break;
    case "turnright":
      utils.executeQicliCommand('ALMotion.moveTo 0.0 0.0 -0.5 1.0');
      break;
    case "moveforward":
      utils.executeQicliCommand('ALMotion.moveTo 0.1 0.0 0.0 1.0');
      break;
    case "movebackward":
      utils.executeQicliCommand('ALMotion.moveTo -0.1 0.0 0.0 1.0');
      break;
    case "shakehand":
      utils.executeQicliCommand('HandShakeService.giveHand');
      break;
    case "autonomousability":
      var state = req.body.value ? 1 : 0;
      utils.executeQicliCommand("ALAutonomousLife.setAutonomousAbilityEnabled All " + state);
      break;
  }
  console.log(req.body.movement);
  res.end();
});

module.exports = router;
