MY_VAR := ${shell python -c 'from image_intensities import VERSION as v; print(v)'}

clean:
	rm -rf *.so *.egg-info build *.png *.log *.svg
	rm -f compiled_cython.c pure_python.c

upload: clean
	python setup.py sdist
	@echo UPLOADING VERSION $(MY_VAR)
	twine upload dist/image_intensities-${MY_VAR}.tar.gz
