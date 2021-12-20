# %%
import numpy as np
with open('input.txt') as f:
    data = f.read()
data = data.replace('#', '1').replace('.', '0')
enhance, image = data.split('\n\n')
enhance = [x for x in enhance]

image = [[y for y in x] for x in image.splitlines()]
image = np.array(image)
image

# %%
def enhance_image(im: np.ndarray, enhance = enhance):
    im = np.pad(im, 2, 'edge')
    new_image = im.copy()
    Y, X = im.shape
    for y in range(1, Y-1):
        for x in range(1, X-1):
            window = im[y-1:y+2, x-1:x+2].reshape(-1)
            index =int("".join(window),2)
            new_image[y, x] = enhance[index]
    return new_image[1:-1, 1:-1]

passes = 50
enhanced_image = np.pad(image, 1)
for _ in range(passes):
    enhanced_image = enhance_image(enhanced_image)
np.sum(enhanced_image == '1')



# %%
import numpy as np
from scipy.ndimage import convolve
with open('input.txt') as f:
    algo, _, *image = f.read().splitlines()

algo = np.array([int(p=="#") for p in algo])
image = np.pad([[int(p=="#") for p in row]
                for row in image], (51,51))

bin2dec = 2**np.arange(9).reshape(3,3)

for i in range(50):
    image = algo[convolve(image, bin2dec)]
    if i+1 in (2, 50): print(image.sum())

# %%
