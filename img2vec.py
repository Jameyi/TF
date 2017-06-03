# encoding utf-8
"""

"""

from __future__ import print_function
import numpy as np
import PIL.Image as Image
import pickle as p
import matplotlib.pyplot as pyplot

class Operation(object):
    image_base_path = "./images/"
    data_base_path = "./data/"

    def image_to_array(self,filenames):
        """

        """
        n = filenames.__len__() # get counts of the images
        result = np.array([])
        print("Starting convert image to array......")
        for i in range(n):
            #print(self.image_base_path + filenames[i])
            image = Image.open(self.image_base_path + filenames[i])
            r,g,b = image.split() #
            #
            r_arr = np.array(r).reshape(1024)
            g_arr = np.array(g).reshape(1024)
            b_arr = np.array(b).reshape(1024)
            #
            image_arr = np.concatenate((r_arr,g_arr,b_arr))
            result = np.concatenate((result,image_arr))

        # change 1 dim array to 2 dim array of count*3072
        result = result.reshape((n,3072))
        # result.shape should be (n,3072)
        print(result.shape) 
        print("Covert success! Starting saving to document......")
        file_path = self.data_base_path + "data2.bin"
        with open(file_path,mode='wb') as f:
            p.dump(result,f)
        print("Save success!")
    
    def array_to_image(self,filename):
        """

        """
        with open(self.data_base_path + filename,mode='rb') as f:
            arr = p.load(f)
        rows = arr.shape[0]
        arr = arr.reshape(rows,3,32,32)
        for index in range(rows):
            a = arr[index]
            # get RGB Channel
            r = Image.fromarray(a[0]).covert('L')
            g = Image.fromarray(a[1]).covert('L')
            b = Image.fromarray(a[2]).covert('L')
            image = Image.merge("RGB",(r,g,b))
            # show image
            pyplot.imshow(image)
            pyplot.show()
            image.save(self.image_base_path + "result" + str(index) + ".png",'png')

if __name__ == "__main__":
    my_operator = Operation()
    images = []
    for j in range(5):
        images.append("img" + str(j))
    my_operator.image_to_array(images)
#    my_operator.array_to_image("data2.bin")



