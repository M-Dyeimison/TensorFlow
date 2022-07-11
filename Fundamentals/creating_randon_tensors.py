import tensorflow as tf

random_1 = tf.random.Generator.from_seed(42)
random_1 = random_1.normal(shape=(3,2))
random_1

random_2 = tf.random.Generator.from_seed(42)
random_2 = random_2.normal(shape=(3,2))
random_2

#check if the two tensors are equal
random_1, random_2, random_1 == random_2
