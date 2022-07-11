import tensorflow as tf
import numpy as np

#creating a tensor of rank 4 (4 dimensions)
rank_4_tensor = tf.zeros(shape=[2,3,4,5])
rank_4_tensor
rank_4_tensor[0]
rank_4_tensor.shape, rank_4_tensor.ndim, tf.size(rank_4_tensor)

#getting various atributes fro the tensor
print("Data type of every element: ", rank_4_tensor.dtype)
print("Number of dimensions (rank): ", rank_4_tensor.ndim)
print("Shape of the tensor: ", rank_4_tensor.shape)
print("Number of elements along the 0 axis: ", rank_4_tensor.shape[0])
print("Number of elements along the last axis: ", rank_4_tensor.shape[-1])
print("Total number of elements in our tensor: ", tf.size(rank_4_tensor))
print("Total number of elements in our tensor: ", tf.size(rank_4_tensor).numpy())