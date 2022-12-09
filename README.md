# YAPyBrot 

Yet Another Python Mandelbrot - a mixed language (Python & C++) project using continuous integration 

## Quickstart

```
pip install yapybrot
```

See [examples](./examples) for usage. 

## Installing from Source 

Prerequisites: 

* Python >= 3.8 
* CMake 

### Option 1 - Via Conda

```
conda env create -f environment.yml
conda activate yapybrotenv
pip install .
```

### Option 2 - Build C++ Libraries from Source

```
pip install -r requirements.txt
./install_libs.sh
pip install .
```

## Gallery 

![](./examples/zoom.gif)
