
window.addEventListener('resize', function () { 
    "use strict";
    window.location.reload(); 
});



/* Vollbild Popup */

function popupOnV()
{
    document.getElementById("overlayVollbild").style.display = "block";
}

function popupOffV()
{
    document.getElementById("overlayVollbild").style.display = "none";
}

function popupOnS()
{
    document.getElementById("overlaySchritte").style.display = "block";
}

function popupOffS()
{
    document.getElementById("overlaySchritte").style.display = "none";
}

function popupOnF() {
    document.getElementById("overlayFragezeichen").style.display = "block";
}

function popupOffF() {
    document.getElementById("overlayFragezeichen").style.display = "none";
}


/* Fortschrittsanzeige berechnen */

function fortschritt(seitennummer, anzahlseitengesamt) {

    var svg = document.getElementById("fortschrittsanzeige");
    var polygondunkel = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
    var polygonhell = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
   
    svg.appendChild(polygondunkel);
    svg.appendChild(polygonhell);

    var neigung = 30;
    var breite = svg.clientWidth - neigung;
    var hoehe = 30;
    var breitedunkel = (seitennummer/anzahlseitengesamt)*breite;


    var arraydunkel = arr = [   [ 0, hoehe ], 
                                [ breitedunkel, hoehe ],
                                [ breitedunkel + neigung, 0 ], 
                                [ neigung, 0]
                            ];

    var arrayhell = arr =   [   [ breitedunkel , hoehe ], 
                                [ breite, hoehe ],
                                [ breite + neigung, 0 ], 
                                [ breitedunkel + neigung, 0]
                            ];


    for (value of arraydunkel) {
        var point = svg.createSVGPoint();
        point.x = value[0];
        point.y = value[1];
        polygondunkel.points.appendItem(point);
        /* svg.fill = '#A65756'; */
    }

    polygondunkel.setAttribute ('fill', '#A65756');

    for (value of arrayhell) {
        var point = svg.createSVGPoint();
        point.x = value[0];
        point.y = value[1];
        polygonhell.points.appendItem(point);
    }

    polygonhell.setAttribute ('fill', '#D9B4B4');

}

var steps = []

var currentStep = 0;

function showNextStep() {

    var content = document.getElementById("vorzurueck");

    content.innerHTML = "";

    var nextStep = steps[currentStep];

    content.innerHTML = nextStep;

    currentStep++;

    if(currentStep >= steps.length) {
        document.getElementById("img")
    }
}
