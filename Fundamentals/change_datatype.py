import tensorflow as tf

#create a new tensor with default datatype (flaot32)
B = tf.constant([2.3, 7.4])
B.dtype

C = tf.constant([1, 2])
C.dtype

#change float32 to float16 reduce precision
D = tf.cast(B, dtype=tf.float16)
D, D.dtype


#change from int32 to float32
E = tf.cast(C, dtype=tf.float32)
E, E.dtype

E_float16 = tf.cast(E, dtype=tf.float16)
E_float16, E_float16.dtype
