

/* Abbrechen Popup */
window.onload = function() {
    popupOffL();
}

function popupOnA() {
    document.getElementById("overlayAbbrechen").style.display = "block";
}

function popupOffA(){
    document.getElementById("overlayAbbrechen").style.display = "none";
}

function popupOnL(){
    document.getElementById("overlayLoeschen").style.display = "block";
}

function popupOffL(){
    document.getElementById("overlayLoeschen").style.display = "none";
}

function popupOnS(){
    document.getElementById("overlaySpeichern").style.display = "block";
}

function popupOffS(){
    document.getElementById("overlaySpeichern").style.display = "none";
}

function deleteDataAndClose(){

}
