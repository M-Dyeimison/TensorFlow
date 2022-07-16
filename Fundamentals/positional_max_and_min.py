import tensorflow as tf

#create a new tensor for finding positional minimum and maximum
tf.random.set_seed(42)
F = tf.random.uniform(shape=[50])
F

#find the positional maximum
tf.argmax(F)

#index of our largeste value position
F[tf.argmax(F)]


#find the max value of F
tf.reduce_max(F)

#check for equality
assert F[tf.argmax(F)] == tf.reduce_max(F) #assert returns error if the statement is false
F[tf.argmax(F)] == tf.reduce_max(F)

#find the positonal minimum
tf.argmin(F)

#find the minimum using the positional minimum index
F[tf.argmin(F)]
