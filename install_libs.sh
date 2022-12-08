pip install -r requirements.txt

PYPATH=$(which python)

libs="pybind11 xtl xtensor xtensor-python"  
for lib in $libs
do
	mkdir lib/$lib/build
	cd lib/$lib/build
	cmake -DCMAKE_INSTALL_PREFIX=../../../bin/ -DPYTHON_EXECUTABLE:FILEPATH=$PYPATH ..
	make install
	cd ../../..
	rm -r lib/$lib/build
done