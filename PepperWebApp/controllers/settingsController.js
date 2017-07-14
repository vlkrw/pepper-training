var express = require('express');
var router = express.Router();

var utils = require('./../utils/utils');

router.get('/volume', function (req, res) {
  utils.executeQicliCommand("ALAudioDevice.getOutputVolume").then((result) => res.end(result.match(/\d+/)[0]));
});

router.post('/volume', function (req, res) {
  var volume = parseInt(req.body.value);
  if (volume > 100){
    volume = 100;
  }else if(volume < 0){
    volume = 0;
  }
  console.log("Setting Volume to " + volume);
  utils.executeQicliCommand("ALAudioDevice.setOutputVolume " + volume).then(() => res.end());
});

router.get('/battery', function (req, res) {
  utils.executeQicliCommand("ALBattery.getBatteryCharge").then((result) => res.end(result.match(/\d+/)[0]));
});

module.exports = router;
