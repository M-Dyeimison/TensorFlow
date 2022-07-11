import tensorflow as tf

#shuffle the tensor
not_shuffled = tf.constant([[1,8],[3,5],[2,6],[3,2]])
not_shuffled.ndim
not_shuffled

#shuffle the non suffled tensor
tf.random.shuffle(not_shuffled)
tf.random.shuffle(not_shuffled, seed=42)

#reproduceble shuffle
tf.random.set_seed(42)
tf.random.shuffle(not_shuffled, seed=(42))

