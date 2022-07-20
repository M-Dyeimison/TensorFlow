import tensorflow as tf

#create a list of indices
some_list = [0,1,2,3]

#one hot encode our list of indices
tf.one_hot(some_list, depth=4)

#specify custom values for one hot encoding
tf.one_hot(some_list, depth=4, on_value="yo i love deep learnig", off_value="i also like to dance")
