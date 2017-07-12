$( document ).ready(function() {
  $.get("/battery", ((data) => $("#batteryIndicator").text(data + "%")));
});
