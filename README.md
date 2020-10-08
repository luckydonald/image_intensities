# image_intensities
Python implementation of the great [derpibooru/image_intensities](https://github.com/derpibooru/image_intensities/tree/8aa43674f61f77cfc756c23556b6ae45e1b210b1).

```python
from image_intensities import rgb_luma_from_filename, Luma

luma = rgb_luma_from_filename('/path/to/image.png')

# returns something like
luma == Luma(nw=0.42, ne=0.44, sw=0.58, se=0.69)
```
