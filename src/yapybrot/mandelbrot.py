from _yapybrot import _mandelbrot
import matplotlib as mpl
import numpy as np


class Mandelbrot:
    """
    Attributes:
    -----------
        width : float
            Width of image in pixels (default 500)
        height : float
            Height of image in pixels (default 500)
        xmin : float
            Minimum value of the real component and left coordinate of the
            view (default -2)
        xmax : float
            Maximum value of the real component and right coordinate of the
            view (default 0.5)
        ymin : float
            Minimum value of the imaginary component and bottom coordinate of
            the view (default -1.12)
        ymax : float
            Maximum value of the imaginary component and top coordinate of the
            view (default 1.12)
        max_iter : int
            Maximum iterations (default 256)
        cmap : str
            Matplotlib colormap name to use as a palette. See:
            https://matplotlib.org/stable/gallery/color/colormap_reference.html
        palette : numpy array {max_iter, 4}, int
            Set of RGBA values for a given number of iterations (default set
            by cmap)
        smoothing : bool
            Use color smoothing (default True)

    Methods:
    --------
        calculate(**kwargs):
            Returns the resulting Mandelbrot as an integer numpy array.
            Attributes can be set using **kwargs.
    """
    def __init__(self, **kwargs):
        self.width = 500
        self.height = 500
        self.xmin = -2
        self.xmax = .5
        self.ymin = -1.12
        self.ymax = 1.12
        self.max_iter = 256
        self.cmap = 'twilight_shifted'
        self.smoothing = True
        self._set_args(**kwargs)

    def __setattr__(self, key, value):
        # Set the intended attribute without recursion
        super(Mandelbrot, self).__setattr__(key, value)

        # Update the palette, in addition, if 'cmap' or 'max_iter' is set
        if key == 'cmap' or key == 'max_iter':
            try:
                mmap = mpl.colormaps[self.cmap]
                miter = self.max_iter
                new_palette = (mmap(np.linspace(0, 1, miter)) * 255)\
                    .astype(int)
                super(Mandelbrot, self).__setattr__('palette', new_palette)

            except AttributeError:
                pass

        # Update 'cmap' if the user changes the palette
        if key == 'palette':
            super(Mandelbrot, self).__setattr__('cmap', 'user')

    def _set_args(self, **kwargs):
        """
        Update attributes based on keyword arguments
        """
        for key, value in kwargs.items():
            if key in self.__dict__.keys():
                setattr(self, key, value)
            else:
                raise AttributeError

    def calculate(self, **kwargs):
        """
        Parameters:
        -----------
            Any Mandelbrot class attributes as keyword arguments

        Returns:
        --------
            numpy array {height, width, 4}, int
                Resulting mandelbrot image as a numpy array
        """
        self._set_args(**kwargs)
        return _mandelbrot(
            self.width,
            self.height,
            self.xmin,
            self.xmax,
            self.ymin,
            self.ymax,
            self.max_iter,
            self.palette,
            self.smoothing
        )
