import tensorflow as tf

#create a new tensor
H = tf.range(1, 10)

#square it
tf.square(H)

#find the squareroot
tf.sqrt(tf.cast(H, dtype=tf.float32))

#find the log
tf.math.log(tf.cast(H, dtype=tf.float32))
