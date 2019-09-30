#!/usr/bin/env python3
import base64
from flask import Flask, render_template, request

import encryption

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def frequency(n, t = 440):
    return (2 ** (1 / 12)) ** (n - 49) * t

def get_note_number(note):
    notes = ["A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab"]
    octave = int(note[-1])
    note = note[: -1]
    index = notes.index(note)

    return (octave - 1) * 12 + (index - 3) % 12 + 4

@app.route("/encrypt", methods = ["POST"])
def encrypt():
    tuning = int(request.form.get("tuning"))
    notes = request.form.get("notes").split(",")
    message = request.form.get("message")

    if len(notes) != 6:
        return "You need to use exactly 6 notes!"
    
    if tuning < 320 or tuning > 2100:
        return "Bad tuning!"

    notes = [get_note_number(note) for note in notes]
    frequencies = [frequency(note, tuning) for note in notes]
    ciphertext = encryption.encrypt(message, frequencies)
    print(notes)
    print(tuning)
    print(frequencies)

    return base64.b64encode(ciphertext)
