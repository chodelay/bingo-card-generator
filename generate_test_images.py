from PIL import Image
import random

IMG_W = 190
IMG_H = 165
INPUT_DIR = 'input'

for x in range(0, 75):
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    im = Image.new(mode='RGB', size=(IMG_W, IMG_H))
    im.paste((r, g, b), [0, 0, im.size[0], im.size[1]])
    im.save(f'{INPUT_DIR}/test_{x}.png')
