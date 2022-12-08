CPP_LIBS="pybind11 xtl xtensor xtensor-python"  

for PY_VER in "cp38-cp38 3.8" "cp39-cp39 3.9" "cp310-cp310 3.10"
do
	# Install python libraries
	/opt/python/${PY_VER[0]}/bin/python -m pip install -r requirements.txt
	
	# Build the C++ libraries
	for CPP_LIB in $CPP_LIBS
	do
		mkdir lib/$CPP_LIB/build && cd $_
		cmake \
			-DPYTHON_EXECUTABLE:FILEPATH=/opt/python/${PY_VER[0]}/bin/python \
			-DPYTHON_INCLUDE_DIR:PATH=/opt/python/${PY_VER[0]}/include/python${PY_VER[1]} \
			-DCMAKE_INSTALL_PREFIX=../../../bin/ ..
		make install
		cd ../../..
		rm -r lib/$CPP_LIB/build
	done
done
