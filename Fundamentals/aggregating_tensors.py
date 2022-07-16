import tensorflow as tf
import numpy as np

D = tf.constant([-7, -10])

#getting the absolute value
tf.abs(D)

#create a random tensor with values between 0 and 100 of size 50
E = tf.constant(np.random.randint(0, 100, size=50))
E

#find the minimum
tf.reduce_min(E)

#find the maximum
tf.reduce_max(E)

#find the mean
tf.reduce_mean(E)

#find the sum
tf.reduce_sum(E)

E_float16 = tf.cast(E, dtype=tf.float16)

#find the variance
tf.math.reduce_variance(E_float16)

#find the standard deviation
tf.math.reduce_std(E_float16)
