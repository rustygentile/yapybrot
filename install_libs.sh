# Options:
# -m,     build on manylinux for python versions 3.8, 3.9, 3.10
# [none], build only for current active python version

mflag=0
while getopts "m" flag
do
    case "${flag}" in
    m)    mflag=1;;
    esac
done

CPP_LIBS="pybind11 xtl xtensor xtensor-python"  

if [ $mflag == 1 ]
then
	for PV in "cp38-cp38 3.8" "cp39-cp39 3.9" "cp310-cp310 3.10"
	do
		PY_VER=( $PV )
	
		# Install python libraries
		/opt/python/${PY_VER[0]}/bin/python -m pip install -r requirements.txt
	
		# Build the C++ libraries
		for CPP_LIB in $CPP_LIBS
		do
			mkdir ./bin/python${PY_VER[1]}/
			mkdir lib/$CPP_LIB/build && cd $_
			cmake \
				-DPYTHON_EXECUTABLE:FILEPATH=/opt/python/${PY_VER[0]}/bin/python \
				-DPYTHON_INCLUDE_DIR:PATH=/opt/python/${PY_VER[0]}/include/python${PY_VER[1]} \
				-DCMAKE_INSTALL_PREFIX=../../../bin/python${PY_VER[1]}/ ..
			make install
			cd ../../..
			rm -r lib/$CPP_LIB/build
		done
	done
else
	for CPP_LIB in $CPP_LIBS
	do
		mkdir lib/$CPP_LIB/build && cd $_
		cmake -DCMAKE_INSTALL_PREFIX=../../../bin/ ..
		make install
		cd ../../..
		rm -r lib/$CPP_LIB/build
	done
fi
