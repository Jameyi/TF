#-*- coding:utf-8 -*-
import pickle,pprint
from PIL import Image
import numpy as np
import os
import matplotlib.image as plimg

class DictSave(object):
    def __init__(self,filenames):
        self.filenames = filenames
        self.arr = []
        self.all_arr = []
        print

    def image_input(self,filenames):
        for filename in filenames:
            self.arr = self.read_file(filename)
            if self.all_arr == []:
                self.all_arr = self.arr
            else:
                self.all_arr = np.concatenate((self.all_arr,self.arr))

    def read_file(self,filename):
        im = Image.open(filename)
        r,g,b = im.split()
        r_arr = plimg.pil_to_array(r)
        g_arr = plimg.pil_to_array(g)
        b_arr = plimg.pil_to_array(b)

        r_arr1 = r_arr.reshape(1024)
        g_arr1 = g_arr.reshape(1024)
        b_arr1 = b_arr.reshape(1024)

        arr = np.concatenate((r_arr1,g_arr1,b_arr1))
        return arr

    def pickle_save(self,arr):
        print "Saving..."

        contact = {'data' : arr}
        f = open('contact','w')
        pickle.dump(contact,f)
        f.close()
        print "Save done!"
        print contact # contact is a dictionary

if __name__ == "__main__":
    filenames = [os.path.join("./testdata/images/","img%d" % i) for i in xrange(0,100)]

    ds = DictSave(filenames)
    ds.image_input(ds.filenames)
    ds.pickle_save(ds.all_arr)
    print "The final array size:" + str(ds.all_arr.shape)
