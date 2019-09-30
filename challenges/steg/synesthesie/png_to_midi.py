import sys
from PIL import Image
from mido import Message, MidiFile, MidiTrack

notes = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number, C major
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
track.append(Message('program_change', program=0, time=0))

if len(sys.argv) != 2:
    print("Usage: python png_to_midi.py <image>")
    sys.exit(1)

im = Image.open(sys.argv[1])

# Get a set of all colors used in the image
colors = {rgb for count, rgb in im.getcolors()}

if len(colors) > len(notes):
    print("Too many colors")
    print("try imageMagick=> convert <image> -colors 8 <out image>")
    sys.exit(1)

colors_to_note = { rgb: notes[n] for n, rgb in enumerate(colors)}

width, height = im.size
note_length = 120
for x in range(height):
    for y in range(width):
        rgb = im.getpixel((y,x))
        note = colors_to_note[rgb]
        track.append(Message('note_on', note=note, time=0))
        track.append(Message('note_off', note=note, time=note_length))

mid.save('flag.mid')
