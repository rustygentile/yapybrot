#include "pybind11/pybind11.h"

#include "xtensor/xmath.hpp"
#include "xtensor/xarray.hpp"
#include "xtensor/xbuilder.hpp"
#include "xtensor/xview.hpp"

#define FORCE_IMPORT_ARRAY
#include "xtensor-python/pyarray.hpp"
#include "xtensor-python/pyvectorize.hpp"

#include <iostream>
#include <numeric>
#include <cmath>
#include <algorithm>

namespace py = pybind11;

xt::pyarray<int> mandelbrot(int width, int height,
                            double xmin, double xmax,
                            double ymin, double ymax,
                            int max_iter,
                            xt::pyarray<int> palette,
                            bool smoothing)
{

    int channels = 4;
    xt::pyarray<int> mandel = xt::empty<int>({height, width, channels});
    xt::pyarray<int> color1 = xt::empty<int>({channels});
    xt::pyarray<int> color2 = xt::empty<int>({channels});
    xt::pyarray<double> colorAvg = xt::empty<double>({channels});

    double x, y, x0, y0, x2, y2, logZn, nu, iterations;
    int iter;
    
    for (int i = 0; i < width; i++) {
        for (int j = 0; j < height; j++) {

            x = 0;
            y = 0;
            x2 = 0;
            y2 = 0;
            x0 = xmin + i * (xmax - xmin) / (width);
            y0 = ymin + j * (ymax - ymin) / (height);

            iter = 0;
            while (iter < max_iter - 1) {
                if (x2 + y2 > 4){
                    break;
                }
                y = 2 * x * y + y0;
                x = x2 - y2 + x0;
                x2 = x * x;
                y2 = y * y;
                iter++;
            }

            if ((iter < max_iter - 1) && smoothing) {
                logZn = log(x2 + y2) / 2;
                nu = log(logZn / log(2)) / log(2);

                iterations = std::min(iter + 1. - nu, max_iter - 2.);
                iterations = std::max(0., iterations);

                color1 = xt::view(palette, floor(iterations), xt::all());
                color2 = xt::view(palette, floor(iterations) + 1, xt::all());
                colorAvg = color1 + (color2 - color1) * (iterations - floor(iterations));

                for (int k = 0; k < channels; k++) {
                    mandel(height - j - 1, i, k) = xt::cast<int>(colorAvg)(k);
                }
            }

            else {
                xt::view(mandel, height - j - 1, i, xt::all()) = xt::view(palette, iter, xt::all());
            }
        }
    }
    return mandel;
}

PYBIND11_MODULE(_yapybrot, m)
{
    xt::import_numpy();
    m.def("_mandelbrot", &mandelbrot, "Plot a Mandelbrot of a given width and height");
}