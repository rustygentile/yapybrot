# YAPyBrot 

Yet Another Python Mandelbrot - a mixed language (Python & C++) project using continuous integration 

## Quickstart

```
pip install yapybrot
```

See the [examples](./examples) for usage. 

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

### Option 2 - Build C++ Libraries from Source (Linux only)

```
pip install -r requirements.txt
./install_libs.sh
pip install .
```

## Gallery 

<p float="left">
  <img src="./examples/static1.png" width="300" />
  <img src="./examples/static2.png" width="300" /> 
  <img src="./examples/static3.png" width="300" />
</p>

<p float="left">
  <img src="./examples/zoom1.gif" width="450" />
  <img src="./examples/zoom2.gif" width="450" /> 
</p>
