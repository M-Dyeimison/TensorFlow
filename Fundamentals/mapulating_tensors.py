import tensorflow as tf

#you can add values to a tensor using the addition operator
tensor = tf.constant([[10,7],[3,4]])
tensor + 10

#original tensor is unchanged
tensor


#multiplication
tensor * 10

#subtraction
tensor - 10

#we can use the tensorflow build-in function too
tf.multiply(tensor, 10)
tensor
