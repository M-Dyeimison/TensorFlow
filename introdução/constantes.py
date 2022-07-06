import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
valor1 = tf.constant(2)
valor2 = tf.constant(5)
type(valor1)
print(valor1)
print(valor2)
soma = valor1 + valor2
type(soma)
print(soma)

with tf.Session() as sess:
    s = sess.run(soma)
    print(s)
