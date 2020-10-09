MY_VAR := ${shell python -c 'from image_intensities.version import VERSION as v; print(v)'}

clean:
	rm --verbose -rf **/*.so **/*.egg-info build **/*.png **/*.log **/*.svg
	rm --verbose -rf image_intensities/{{compiled_cython,pure_python,_native_code/_image_intensities}.{c,so,*.so,o},lib,image_intensities/_native_code/{jpeg,png,intensities}.o}
	cd image_intensities/_native_code && make clean

upload: clean
	python setup.py sdist
	@echo UPLOADING VERSION $(MY_VAR)
	twine upload dist/image_intensities-${MY_VAR}.tar.gz

install:
	cd image_intensities/image_intensities && make
