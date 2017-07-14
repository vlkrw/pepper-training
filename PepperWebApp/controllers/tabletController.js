var express = require('express');
var router = express.Router();

var fs = require("fs");
var multer = require('multer');
var utils = require('./../utils/utils');
var config = require('./../config');

router.get('/tablet', function (req, res) {
  res.render('pages/tablet');
});

router.get('/imagenames', function (req, res) {
  var imagenames = [];
  fs.readdirSync(config.resources.imagespath).forEach(file => {
    imagenames.push(file);
  });

  res.send(JSON.stringify(imagenames));
});

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, config.resources.imagespath);
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
})
const upload = multer({storage: storage, fileFilter: function (req, file, cb) {
  if (!file.originalname.toLowerCase().match(/\.(jpg|jpeg|png|gif)$/)) {
      return cb(new Error('Only image files are allowed!'));
  }
  cb(null, true);
}});

router.post('/image', upload.single("image"), function(req, res) {
  res.redirect('back');
});

router.post("/showimage", function(req, res){
  var name = req.body.name;
  if(name == ""){
    utils.executeQicliCommand("ALTabletService.hideImage");
  }else{
    utils.executeQicliCommand("ALTabletService.showImage 'http://" + utils.getIp() + name + "'");
  }
});

router.post("/removeimage", function(req, res){
  var name = req.body.name;

  fs.stat(config.resources.imagespath + name, function (err, stats) {
    if(err) return console.log(err);

    fs.unlinkSync(config.resources.imagespath + name,function(err){
      res.end();
      if(err) return console.log(err);
    });
  });
});

module.exports = router;
