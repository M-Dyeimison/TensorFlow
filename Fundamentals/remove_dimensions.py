import tensorflow as tf


tf.random.set_seed(42)
G = tf.constant(tf.random.uniform(shape=[50]), shape=(1,1,1,1,50))
G
G.shape
G_squeezed = tf.squeeze(G)
G_squeezed, G_squeezed.shape
