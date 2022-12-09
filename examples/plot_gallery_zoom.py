import numpy as np
from yapybrot import Mandelbrot
from PIL import Image
import time


# Center point
xc = -0.74364085
yc = 0.13182733

# Start and ending window sizes
size0 = 1e-2
size1 = 5e-6

# Set the decay factor by experimentation
frames = 700
k = 1.5 * 5 / frames

mand = Mandelbrot(max_iter=1000)
images = []

start = time.time()
for i in range(frames):
    size = (size0 - size1) * np.exp(-k * i) + size1

    if (i + 1) % 10 == 0:
        end = time.time()
        print(f'Rendering frame: {i + 1}... size={size}  avg time={(end - start) / 10}')
        start = time.time()

    buffer = mand.calculate(xmin=xc - size, xmax=xc + size,
                            ymin=yc - size, ymax=yc + size)

    im = Image.fromarray(buffer.astype('uint8'))
    images.append(im)

print('Saving gif...')
images[0].save('zoom2.gif', save_all=True, append_images=images[1:],
               optimize=False, duration=30, loop=0)
