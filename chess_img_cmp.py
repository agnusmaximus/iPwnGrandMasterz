import os
import sys
from PIL import *
from PIL import Image
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
import numpy
import image_similarity
import ssim
import math
import operator

def get(dir, piece_name):
    data = imread(dir + piece_name)
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    return (data-data.mean()) / data.std()

def cmp2(dir1, dir2, piece1, piece2):
    return ssim.compute_ssim(Image.open(dir1+piece1), Image.open(dir2+piece2))

def cmp(dir1, dir2, piece1, piece2):
    h1 = Image.open(dir1+piece1).histogram()
    h2 = Image.open(dir2+piece2).histogram()

    rms = math.sqrt(reduce(operator.add,
        map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return 1 / (rms + 1)


if __name__ == "__main__":
    d = 'piece_images/'
    for i in range(8):
        for j in range(8):
            target_name = str(i)+str(j)
            bests = []
            for k in range(8):
                for l in range(8):
                    cur = str(k)+str(l)
                    score = cmp(d, d, target_name, cur)
                    bests.append((cur, score))
            bests.sort(key=lambda x:x[1], reverse=True)
            print(target_name, bests)
