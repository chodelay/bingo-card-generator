# Bingo card generator

# Prerequisites
 - Install Python 3.7 or above (ensure you add to PATH during install)
 - Open command line and navigate to project directory
 - run ```pip3 install -r requirements.txt```
 - Replace test images in input directory with files including one freespace.png for center space.

# Usage
*In project directory:*

```python generate.py [n]```

 - **n**: optional argument to produce **n** images, otherwise produces 5

## Config variables
*See top of generate.py*
| Name | Default | Purpose |
| ---- | ------- | ------- |
| CELL_W | 190 | Width of each cell (final image will have width of 5x this) |
| CELL_H | 165 | Height of each cell (final image will have height of 5x this) |
| INPUT_DIR | input | Directory of input files (freespace image should be here) |
| OUTPUT_DIR | output | Directory for output files |
| OUTPUT_PREFIX | 190 | Prefix for output files (will be numbered according to existing prefixes) |
| FREESPACE_IMG_NAME | 190 | File name of the free space image (relative to input dir) |