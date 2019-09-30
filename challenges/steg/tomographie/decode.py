import numpy as np
from PIL import Image, ImageSequence

im = Image.open("ct_scan.gif")

frames = []
for frame in ImageSequence.Iterator(im):
    frames.append(np.array(frame))

frames = np.array(frames) # 3d numpy array from gif

new_frames = []
for layer in np.rollaxis(frames, 2): # iterate over horizontal axis
    i = Image.fromarray(layer)
    new_frames.append(i)

new_frames[0].save('decoded.gif', format='GIF', append_images=new_frames[1:], save_all=True, duration=50, loop=1)
