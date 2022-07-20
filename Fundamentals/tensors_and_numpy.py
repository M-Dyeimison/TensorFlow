import tensorflow as tf
import numpy as np

#create a tensor directly from a numpy array
J = tf.constant(np.array([3.,7.,10.]))
J

#convert tensor back to numpy array
np.array(J), type(np.array(J))

#convert tensor J to a numpy array
J.numpy(), type(J.numpy())

J = tf.constant([3.])
J.numpy()[0]


#the default type of each are slightly different
numpy_J = tf.constant(np.array([3.,7.,10.]))
tensor_J = tf.constant([3.,7.,10.])
numpy_J.dtype, tensor_J.dtype
