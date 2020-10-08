MY_VAR := ${shell python -c 'from image_intensities.version import VERSION as v; print(v)'}

clean:
	rm --verbose -rf **/*.so **/*.egg-info build **/*.png **/*.log **/*.svg
	rm --verbose -rf image_intensities/compiled_cython.{c,*.so} image_intensities/pure_python.{c,*.so} image_intensities/image_intensities/lib

upload: clean
	python setup.py sdist
	@echo UPLOADING VERSION $(MY_VAR)
	twine upload dist/image_intensities-${MY_VAR}.tar.gz

install:
	cd image_intensities/image_intensities && make
