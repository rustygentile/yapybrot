import numpy as np
import pytest
import yapybrot as ypb


class TestMandelbrots:
    @pytest.fixture
    def mandelbrot(self):
        m = ypb.Mandelbrot()
        m.width = 4
        m.height = 4
        m.xmin = -0.75
        m.xmax = -0.76
        m.ymin = 0.14
        m.ymax = 0.16
        return m

    def test_result(self, mandelbrot):
        result = mandelbrot.calculate()
        expected = np.array(
            [[[77, 23, 111, 255],
              [76, 22, 108, 255],
              [76, 22, 107, 255],
              [75, 21, 106, 255]],
             [[79, 25, 115, 255],
              [77, 23, 111, 255],
              [76, 22, 109, 255],
              [76, 22, 108, 255]],
             [[80, 26, 117, 255],
              [79, 25, 114, 255],
              [78, 24, 112, 255],
              [77, 23, 111, 255]],
             [[81, 26, 118, 255],
              [79, 25, 115, 255],
              [79, 25, 114, 255],
              [78, 24, 113, 255]]])

        np.testing.assert_array_equal(result, expected)

    def test_update_palette_by_keyword(self, mandelbrot):
        mandelbrot.calculate(cmap='hsv', max_iter=100)
        assert mandelbrot.palette[0, 0] == 255
        assert mandelbrot.palette.shape == (100, 4)

    def test_update_palette_by_attr(self, mandelbrot):
        mandelbrot.cmap = 'hot'
        mandelbrot.max_iter = 50
        assert mandelbrot.palette[0, 0] == 10
        assert mandelbrot.palette.shape == (50, 4)

    def test_user_palette(self, mandelbrot):
        mandelbrot.palette = np.ones((256, 4))
        assert mandelbrot.cmap == 'user'

    def test_smoothing(self, mandelbrot):
        res1 = mandelbrot.calculate()
        res2 = mandelbrot.calculate(smoothing=False)
        diff = res1 - res2
        assert np.max(diff) == 2
        assert np.min(diff) == -1
