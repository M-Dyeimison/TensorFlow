import tensorflow as tf

#creating a tensor of all ones
tf.ones([10,7])

#creating a tensor of all zeros
tf.zeros(shape=(10,7))

#turning NumPy arrays into tensors
import numpy as np
numpy_A = np.arange(1, 25, dtype=np.int32) #create a NumPy array
numpy_A

A = tf.constant(numpy_A, shape=(2,3,4))
B = tf.constant(numpy_A)
A, B
A.ndim
