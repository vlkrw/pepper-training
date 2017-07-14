var exec = require('child_process').exec;
var os = require('os');
var config = require('./../config');

module.exports = {
  executeQicliCommand: function(command){
    return new Promise(function (fulfill, reject){
      exec("qicli call " + command + " --qi-url " + config.pepper.ip, (error, stdout, stderr) => {
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
  },

  getIp: function (){
    var ifaces = os.networkInterfaces();
    var ip = "unknown ip";

    var ifnames = Object.keys(ifaces).filter(function(ifname){
      return ifname.indexOf("dapter") == -1 && ifname.indexOf("irtual") == -1;
    });

    ifnames.forEach(function (ifname) {
      var interfaces = ifaces[ifname].filter(function(iface){
        return 'IPv4' == iface.family && iface.internal == false;
      });

      if(interfaces.length > 0){
        ip = interfaces[0].address + ":" + config.web.port;
      }
    });

    return ip;
  }
};
