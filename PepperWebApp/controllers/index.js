var express = require('express');
var router = express.Router();

router.use(require("./settingsController"));
router.use(require("./textAppController"));
router.use(require("./movementController"));
router.use(require("./ledController"));
router.use(require("./tabletController"));

module.exports = router;
