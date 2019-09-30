import sys
from PIL import Image
from mido import Message, MidiFile, MidiTrack

colors = [(0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255)]

if len(sys.argv) != 2:
    print("Usage: python midi_to_png.py <midi file>")
    sys.exit(1)

mid = MidiFile(sys.argv[1])

notes = []
for msg in mid:
    if msg.type == 'note_on':
        notes.append(msg.note)

unique_notes = set(notes)

if len(unique_notes) > len(colors):
    print("Not enough colors!")
    sys.exit(1)

notes_to_colors = {note:colors[n] for n, note in enumerate(unique_notes)}

im = Image.new("RGB", (40,8))

for n, note in enumerate(notes):
    color = notes_to_colors[note]
    im.putpixel((n%40, n//40), color)

im.save("result.png")
