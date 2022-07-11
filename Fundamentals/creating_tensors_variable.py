import tensorflow as tf

#creating chageble and unchengeble tensors
changeble_tensor = tf.Variable([10,34])
constant_tensor = tf.constant([11,35])
changeble_tensor, constant_tensor


#trying changing a variable in the changeble_tensor
changeble_tensor[0] = 44
changeble_tensor

#trying changing a variable in the unchangeble tensor
constant_tensor[0] = 22
constant_tensor

#actually changing the value with .assign()
changeble_tensor[0].assign(44)
changeble_tensor

#trying to chage the unchegeble tensor
constant_tensor[0].assign(22)
