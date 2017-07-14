var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var utils = require('./utils/utils');
var config = require('./config');

app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use('/', express.static(__dirname + '/views/static'));
app.use('/', express.static(__dirname + '/node_modules'));
app.use('/', express.static(config.resources.imagespath));
app.use(require('./controllers'));

app.listen(config.web.port, function () {
  console.log('Pepper app listening on ' + utils.getIp());
});
