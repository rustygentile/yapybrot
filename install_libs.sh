libs="pybind11 xtl xtensor xtensor-python"  
for lib in $libs
do
	mkdir lib/$lib/build && cd $_
	cmake -DCMAKE_INSTALL_PREFIX=../../../bin/ ..
	make install
	cd ../../..
	rm -r lib/$lib/build
done