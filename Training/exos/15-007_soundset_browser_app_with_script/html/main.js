var session = null;

document.addEventListener("DOMContentLoaded", function(event) {

    QiSession(function (s) {
        console.log("connected!");
        session = s;

        // Subscribe to the ColorChosen event to change the background every time it is raised
        session.service("ALMemory").then(function(mem) {
            mem.subscriber("ColorsDemo/ColorChosen").then( function (sub) {
                sub.signal.connect(colorCallback);
            });
        });

    }, function () {
        console.log("disconnected");
    });

});

function raiseEvent(value) {
    console.log("Choosing color: ", value);
    session.service("ALMemory").then(function (mem) {
        mem.raiseEvent("ColorsDemo/ColorChosen", value);
    });
}

function colorCallback(color) {
    console.log("a new color has been selected:", color);
    document.querySelector("body").style.backgroundColor = color;
}