import numpy as np
from yapybrot import Mandelbrot
from PIL import Image

"""
Static Image 1
"""
mand = Mandelbrot(cmap='Greens')

# Override the palette so it ends in solid black
mand.palette[-1, :] = np.array([0, 0, 0, 255])

xc = -0.74
yc = 0.15
size = 0.01

buffer = mand.calculate(xmin=xc-size,
                        xmax=xc+size,
                        ymin=yc-size,
                        ymax=yc+size)

im = Image.fromarray(buffer.astype('uint8'))
im.save('static1.png')

"""
Static Image 2
"""
mand = Mandelbrot(xmin=-1.402, xmax=-1.400, ymin=-0.001, ymax=0.001,
                  cmap='ocean')

buffer = mand.calculate()
im = Image.fromarray(buffer.astype('uint8'))
im.save('static2.png')


"""
Static Image 3
"""

# Increase the number of iterations since we're zooming in
mand = Mandelbrot(cmap='prism', max_iter=1500)

xc = -0.743643135
yc = 0.131825963
size = 0.00001

buffer = mand.calculate(xmin=xc-size,
                        xmax=xc+size,
                        ymin=yc-size,
                        ymax=yc+size)

buffer = mand.calculate()
im = Image.fromarray(buffer.astype('uint8'))
im.save('static3.png')
