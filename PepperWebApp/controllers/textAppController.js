var express = require('express');
var router = express.Router();
var jsonfile = require('jsonfile');
var path = require('path');
var utils = require('./../utils/utils');
var config = require('./../config');

var pathToTextFile = path.resolve(config.resources.textpath, 'text.json')

router.get('/', function (req, res) {
  res.render('pages/index');
});

router.post('/say', function (req, res) {
  var text = req.body.text;
  if(req.body.animated){
    console.log("Saying with animation: " + text);
    utils.executeQicliCommand('ALAnimatedSpeech.say "'+ text + '"');
  }else{
    console.log("Saying " + text);
    utils.executeQicliCommand('ALTextToSpeech.say "'+ text + '"');
  }
  res.end();
});

router.post('/text', function (req, res) {
  var text = req.body;

  jsonfile.writeFile(pathToTextFile, text, function (err) {
    console.error(err)
  })
  res.end();
});

router.get('/text', function (req, res) {
  jsonfile.readFile(pathToTextFile, function(err, obj) {
    res.end(JSON.stringify(obj));
  })
});

module.exports = router;
