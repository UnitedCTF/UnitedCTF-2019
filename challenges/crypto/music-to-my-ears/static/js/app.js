let chosenNotes = [];

function setStatus(status, state) {
    let statusElement = document.querySelector(".status");
    let color = "rgb(245, 210, 10)";

    if(state == "error" || state == "toojazzy") {
        color = "rgb(255, 0, 0)";
    } else if(state == "jazzy") {
        color = "rgb(0, 255, 0)";
    }

    statusElement.innerHTML = status;
    statusElement.style.color = color;
}

function reset() {
    chosenNotes = [];
    setStatus("", "notjazzy");
    document.querySelector("#nowplaying").innerHTML = "";
    document.querySelector("#notes").innerHTML = "";
    window.removeEventListener("mousedown", playNote);
    window.addEventListener("mousedown", playNote);
}

function playNote(e) {
    let noteElement = e.srcElement;
    let noteNumber = noteElement.getAttribute("data-key");
    let noteName = noteElement.getAttribute("data-note");
    let noteOctave = noteElement.getAttribute("data-octave");
    let fullNoteName = noteName + noteOctave;

    if(!noteNumber) {
        return;
    }

    if(chosenNotes.indexOf(fullNoteName) != -1) {
        setStatus("Select a different note!", "error");
        return;
    }

    chosenNotes.push(fullNoteName);
    const audio = document.querySelector(`audio[data-key="${noteNumber}"]`);
    audio.currentTime = 0;
    audio.play();

    document.querySelector("#nowplaying").innerHTML = chosenNotes.join(",");
    document.querySelector("#notes").setAttribute("value", chosenNotes.join(","));

    if(chosenNotes.length < 6) {
        setStatus("Not jazzy enough!", "notjazzy");
    } else if(chosenNotes.length == 6) {
        setStatus("Sooooooooo jazzy!", "jazzy");
    } else if(chosenNotes.length > 6) {
        setStatus("Way too jazzy!", "toojazzy");
    }

    if(chosenNotes.length == 9) {
        window.removeEventListener("mousedown", playNote);
    }
}

function removeTransition(e) {
    if (e.propertyName !== "transform") return;
    this.classList.remove("playing");
}

function hintsOn(e, index) {
    e.setAttribute("style", "transition-delay:" + index * 50 + "ms");
}

function setup() {
    const notes = ["A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab"];
    const positions = [0, 7, 10, 20, 27, 30, 37, 40, 50, 57, 60, 67];

    // I'm not a good web developer :)
    let keysHTML = "";
    let soundsHTML = "";

    for(var i = 0; i < 88; i++) {
        let noteNumber = i + 1;
        let noteClass = (notes[i % 12].length == 1 ? "key" : "key sharp");
        let notePosition = Math.floor(i / 12) * 17.5 + positions[i % 12] / 4;

        let noteOctave = Math.floor((noteNumber - 4) / 12) + 1;
        let keyHTML = `<div data-key="${noteNumber}" class="${noteClass}" data-note="${notes[i % 12]}" data-octave="${noteOctave}" style="left: ${notePosition}%"></div>\n`;
        keysHTML += keyHTML;

        let audioHTML = `<audio data-key="${noteNumber}" src="static/sounds/${noteNumber}.wav"></audio>`;
        soundsHTML += audioHTML;
    }
    
    document.querySelector(".keys").innerHTML = keysHTML;
    document.querySelector(".sounds").innerHTML = soundsHTML;
}

function encrypt() {
    document.querySelector("#wrap").submit();
}

setup();

const keys = document.querySelectorAll(".key");
const hints = document.querySelectorAll(".hints");

hints.forEach(hintsOn);

// keys.forEach(key => key.addEventListener("transitionend", removeTransition));

window.addEventListener("mousedown", playNote);
