import pickle as p
import os
import tensorflow as tf

filename = os.path.join("/home/shiyanlou/tf/cifar_data/cifar-10-batches-py/data_batch_1")
#print(filename)
X = None
Y = None

with open(filename,'rb') as f:
    datadict = p.load(f)
    X = datadict['data']
    Y = datadict['labels']
#    print("data.Xarray size:",X.shape)
    X = X.reshape(100,-1)

valuequeue = tf.train.input_producer(X,shuffle=False)
valuelabel = tf.train.input_producer(Y,shuffle=False)


value = valuequeue.dequeue()
print(value)
label = valuelabel.dequeue()
print(label)
"""
#result.label = tf.string_to_number(label,tf.int32)
#image = tf.reshape(value,[result.depth,result.height,result.width])
#result.uint8image = tf.transpose(image,[1,2,0])
"""
