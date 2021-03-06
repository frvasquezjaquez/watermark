# watermark
Python script to add a watermark or logo to images

### Requirements
Pillow:
```
pip install pillow
```

[Pillow Docs](https://python-pillow.github.io/)

### Usage
This script allows you to add a watermark or logo to images in a specified folder. The script takes three arguments:

1. The folder with the images you want to watermark
2. The path of the logo to add
3. The position you want to place the logo (optional)

These are the valid positions:

- topleft
- topright
- bottomleft
- bottomright
- center (if no position is specified, this will be the default)

Any other position will result in an error.

To use watermark.py without specifying a position:


```
python watermark.py  './images' 'logo.png'
```

To use watermark.py and specify a position:

```
python watermark.py  './images' 'logo.png' bottomright
```

### Adapting
If you want to save your watermarked images as new files instead of saving over the existing files, simply add a prefix to any image.save() lines:

```
image.save(path + '/fancy_new_prefix_' + filename)
```

### Ideas for future improvements
- allow custom positioning
- adjust watermarks to be semi-transparent

RUN Modified command

find [image folder] -type d -exec python watermark.py {} logo.png centralized \;

