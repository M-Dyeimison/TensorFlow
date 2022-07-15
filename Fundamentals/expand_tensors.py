import tensorflow as tf

#create rank 2 tensor
rank_2_tensor = tf.constant([[10,7], [3,4]])

#add new dimension to our rank 2 tensor
rank_3_tensor = rank_2_tensor[..., tf.newaxis]
rank_3_tensor

#alternative to tf.newaxis
tf.expand_dims(rank_2_tensor, axis=-1) #-1 means expand the final axis

#expand the 0 axis
tf.expand_dims(rank_2_tensor, axis=0)

#expand the middle axis
tf.expand_dims(rank_2_tensor, axis=1)
