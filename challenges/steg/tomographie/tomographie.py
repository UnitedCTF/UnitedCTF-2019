import numpy as np
from PIL import Image

im = Image.open('flag.png')
im = im.convert('L') # convert to black and white

pix = np.array(im)
h, _ = pix.shape
pix = pix[..., np.newaxis] # create Z axis
pix = np.repeat(pix, h, axis=2) # extrude image on the Z axis

frames = []
for i, layer in enumerate(np.rollaxis(pix, 0)):
    im = Image.fromarray(layer)
    frames.append(im)

frames[0].save('ct_scan.gif', format='GIF', append_images=frames[1:], save_all=True, duration=50, loop=1)
