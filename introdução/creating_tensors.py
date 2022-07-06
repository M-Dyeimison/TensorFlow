import tensorflow as tf
print(tensorflow.__version__)

#creating tensors
scalar = tf.constant(7)
scalar

#number of dimensions
scalar.ndim

#creating a vector
vector = tf.constant([10,11,12])
vector

#check num of dimensions
vector.ndim

#creating matrix
matrix = tf.constant([[1,0],[0,1]])
matrix

#check num of dimensions
matrix.ndim

#creating matrix with set type
another_matrix = tf.constant([[1.,0.],[0.,1.],[1.,0.]], dtype=tf.float16)
another_matrix

#check num of dimensions
another_matrix.ndim

#matrix with more dimensions
tensor = tf.constant([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])
tensor

#check num of dimensions
tensor.ndim

