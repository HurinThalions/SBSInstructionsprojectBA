function loadAnleitungData1() {
  let counter = 0;

  // Alle Listelemente aus views.py werden geholt
  let elements = document.querySelectorAll("li");

  // container in dem die daten geladen werden wird geholt
  let container = document.getElementById("schritt-details");

  // Laden der Daten aus dem context von views.py in lesbarem Format
  let jsondata = JSON.parse(
    document.getElementById("schritte-json").textContent
  );
  let kompdata = JSON.parse(
    document.getElementById("komponenten-json").textContent
  );

  // Listenelement wird geladen
  let firstElement = elements[counter];
  let firstIndex = firstElement.dataset.index;
  let firstData = jsondata[firstIndex];

  // anzeigen des elements
  addEinzelschritt(container, firstData);
  addKomponenten(container, firstData);

  // Alle Elemente werden geladen und angezeigt
  elements.forEach((element) => {
    let index = element.dataset.index;
    let data = jsondata[index];
    element.addEventListener("load", function () {
      removeContainerChildren(container);
      addEinzelschritt(container, data);
      addKomponenten(container, data);
    });
  });

  // Einzelner Schritt wird geholt und auf die Seite geladen
  function addEinzelschritt(container, data) {
    let einzelschrittElement = document.createElement("div");
    einzelschrittElement.classList.add("einzelschritt");

    let schrittbenennungElement = document.createElement("h1");
    let benennungText = document.createTextNode("Schritt " + counter + ": " + data.schrittbenennung);
    schrittbenennungElement.appendChild(benennungText);
    schrittbenennungElement.classList.add("schrittbenennung");

    let beschreibungUberschriftElement = document.createElement("h2");
    let beschreibungUberschriftText = document.createTextNode("Beschreibung:");
    beschreibungUberschriftElement.appendChild(beschreibungUberschriftText);

    let beschreibungBoxElement = document.createElement("div");
    beschreibungBoxElement.classList.add("beschreibung-box");

    let beschreibungElement = document.createElement("p");
    let beschreibungText = document.createTextNode(data.beschreibung);
    beschreibungElement.appendChild(beschreibungText);
    beschreibungElement.classList.add("beschreibung");

    beschreibungBoxElement.appendChild(beschreibungUberschriftElement);
    beschreibungBoxElement.appendChild(beschreibungElement);

    let schrittBildElement = document.createElement("img");
    schrittBildElement.setAttribute("src", "/media/" + data.schrittbild);
    schrittBildElement.classList.add("rechteZelle");
    console.log(data.schrittbild);

    einzelschrittElement.appendChild(schrittbenennungElement);
    einzelschrittElement.appendChild(beschreibungBoxElement);
    einzelschrittElement.appendChild(schrittBildElement);

    container.innerHTML = "";
    container.appendChild(einzelschrittElement);
  }

  // Komponenten, die zum aktuellen Schritt gehören, werden geholt und auf der Seite geladen
  function addKomponenten(container, data) {
    // ID des aktuellen Anleitungsschritts
    let anleitungsschrittId = data.id;
    let komponentenContainer = document.createElement("div");

    // Leeren des Containers bevor neue Komponenten hinzugefügt werden
    komponentenContainer.innerHTML = "";

    // Komponenten werden anhand des ForeignKeys gefiltert
    let komponenten = kompdata.filter(
      (komponente) => komponente.anleitungsschritt_id === anleitungsschrittId
    );

    // Komponenten werden auf die Seite geladen
    if (komponenten.length > 0) {
      let komponentenUberschriftElement = document.createElement("h2");
      let komponentenUberschriftText = document.createTextNode("Komponenten:");
      komponentenUberschriftElement.appendChild(komponentenUberschriftText);
      komponentenContainer.appendChild(komponentenUberschriftElement);

      komponenten.forEach((komponente) => {
        let komponenteElement = document.createElement("div");
        komponenteElement.classList.add("komponente");

        let komponenteBeschreibung = document.createElement("p");
        komponenteBeschreibung.textContent = komponente.kompbeschreibung;
        komponenteBeschreibung.classList.add("kompbeschreibung");
        komponenteElement.appendChild(komponenteBeschreibung);

        let komponenteBildElement = document.createElement("img");
        komponenteBildElement.setAttribute("src", "/media/" + komponente.kompbild);
        komponenteBildElement.classList.add("kompbild");

        komponenteElement.appendChild(komponenteBildElement);
        komponentenContainer.appendChild(komponenteElement);
      });
    }

    container.appendChild(komponentenContainer);
  }

  // Entfernen des Anleitungsschritts und der Komponenten
  function removeContainerChildren(container) {
    while (container.firstChild) {
      container.removeChild(container.firstChild);
    }
  }

  // Laden der naechsten Anleitungsschritts
  function nextAnleitungsschritt() {
    counter++;

    // Wenn letzter Schritt erreicht wird, wird eine neue Seite geladen
    if (counter >= elements.length) {
      window.location.pathname = "SBSInstructionsproject/anleitungfertig";
      return;
    }

    // naechtses Element wird geholt
    let nextElement = elements[counter];
    let nextIndex = nextElement.dataset.index;
    let nextData = jsondata[nextIndex];

    // naechtes Element wird geladen
    removeContainerChildren(container);
    addEinzelschritt(container, nextData);
    addKomponenten(container, nextData);
  }

  // Button der geklickt wird, um zu dem naechsten Anleitungsschritt zu kommen
  let buttonElementnaechster = document.getElementById("buttonkleinrechts");
  buttonElementnaechster.addEventListener("click", nextAnleitungsschritt);

  function previousAnleitungsschritt() {
    counter--;
    if (counter < 0) {
      // Popup für Anleitung Abbrechen? -> Ja/Nein
      // wenn ja -> window.location.pathname = "SBSInstructionsproject/Startbildschirm";
      // wenn nein -> counter = 0;
    }
    let previousElement = elements[counter];
    let previousIndex = previousElement.dataset.index;
    let previousData = jsondata[previousIndex];
    removeContainerChildren(container);
    addEinzelschritt(container, previousData);
    addKomponenten(container, previousData);
  }

  // Button der geklickt wird, um zu dem vorherigem Anleitungsschritt zu kommen
  let buttonElementzurueck = document.getElementById("buttonkleinlinks");
  buttonElementzurueck.addEventListener("click", previousAnleitungsschritt);
}

loadAnleitungData1();
