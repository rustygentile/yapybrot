libs="pybind11 xtl xtensor xtensor-python"  
for lib in $libs
do
	mkdir lib/$lib/build && cd $_
	cmake -DPYTHON_EXECUTABLE:FILEPATH=/opt/python/cp310-cp310/bin/python \
	-DPYTHON_EXECUTABLE:FILEPATH=/opt/python/cp310-cp310/bin/python \
	-DPYTHON_INCLUDE_DIR:PATH=/opt/python/cp310-cp310/include/python3.10 \
	-DCMAKE_INSTALL_PREFIX=../../../bin/ ..
	make install
	cd ../../..
	rm -r lib/$lib/build
done