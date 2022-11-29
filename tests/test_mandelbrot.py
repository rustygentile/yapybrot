import numpy as np
import pytest
import yapybrot as m


@pytest.mark.unit
def test_mandel():

    w = 4
    h = 4

    xc = -0.74
    yc = 0.15
    size = 0.01

    mandel = m.Mandelbrot(width=w,
                          height=h,
                          pallette_name='twilight')

    res = mandel.calculate(xmin=xc-size,
                           xmax=xc+size,
                           ymin=yc-size,
                           ymax=yc+size)

    expected = np.array(
        [[[179, 198, 206],
          [176, 196, 205],
          [173, 195, 204],
          [173, 195, 204]],

         [[167, 192, 202],
          [101, 129, 189],
          [147, 180, 198],
          [82, 27, 120]],

         [[122, 159, 194],
          [225, 216, 225],
          [124, 161, 194],
          [105, 137, 190]],

         [[225, 216, 226],
          [225, 216, 226],
          [225, 216, 226],
          [225, 216, 226]]]
    ).astype(int)

    np.testing.assert_array_equal(res, expected)
