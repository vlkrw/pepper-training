var config = {};

config.web = {};
config.web.port = "8080";

config.pepper = {};
config.pepper.ip = "192.168.1.100"

config.resources = {};
config.resources.path = __dirname + "/saved_files";
config.resources.textpath = __dirname + "/saved_files/text";
config.resources.imagespath = __dirname + "/saved_files/images";

module.exports = config;
