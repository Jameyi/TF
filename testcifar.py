#-*- coding:utf-8 -*-
import pickle as p
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as plimg
from PIL import Image

def load_CIFAR_batch(filename):
    with open(filename,'rb') as f:
        datadict = p.load(f)
        X = datadict['data']
        Y = datadict['labels']
        X = X.reshape(10000,3,32,32)
        Y = np.array(Y)
        return X,Y

def load_CIFAR_Labels(filename):
    with open(filename,'rb') as f:
        lines = [x for x in f.readlines()]
        print(lines)

if __name__ == "__main__":
    load_CIFAR_Labels("/home/shiyanlou/tf/cifar_data/cifar-10-batches-py/batches.meta")
    imgX,imgY = load_CIFAR_batch("/home/shiyanlou/tf/cifar_data/cifar-10-batches-py/data_batch_1")
    print imgX.reshape
    print "Saving Image..."
    for i in xrange(imgX.shape[0]):
        imgs = imgX[i-1]
        if i < 100:
            img0 = imgs[0]
            img1 = imgs[1]
            img2 = imgs[2]
            i0 = Image.fromarray(img0)
            i1 = Image.fromarray(img1)
            i2 = Image.fromarray(img2)
            img = Image.merge("RGB",(i0,i1,i2))
            name = "img" + str(i)
            img.save("/home/shiyanlou/tf/testdata/images/" + name,"png")
            for j in xrange(imgs.shape[0]):
                img = imgs[j-1]
                name = "img" + str(i) + str(j) + ".png"
                print "Saving Image..." + name
                plimg.imsave("/home/shiyanlou/tf/testdata/image/" + name,img)
                print "Saving Completed!"

