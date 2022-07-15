import tensorflow as tf

tensor = tf.constant([[10,7],[3,4]])

#matrix multiplication in tensorflow
print(tensor)
tf.matmul(tensor, tensor)
print(tensor)


matrix1 = tf.constant([[1,2,5],[7,2,1],[3,3,3]])
matrix1
matrix2 = tf.constant([[3,5],[6,7],[1,8]])
matrix2
tf.matmul(matrix1, matrix2)

#matriz multiplication with python operator "@"
tensor@tensor

#reshape tensor
matrix3 = tf.constant([[1,2,3],[4,5,6]])
matrix3
tf.matmul(matrix1, matrix3)
tf.reshape(matrix3, [3,2])

#try to multiplicate matrix1 by reshaped matrix2
matrix1@tf.reshape(matrix3, [3,2])
matrix1.shape, matrix1@tf.reshape(matrix3, [3,2])

#try using tf.matmul
tf.matmul(matrix1, tf.reshape(matrix3, [3,2]))


#using transpose
matrix3, tf.transpose(matrix3), tf.reshape(matrix3, [3,2])


#try matrix multiplication with transpose rathar tha reshape
tf.matmul(matrix1, tf.transpose(matrix3))
