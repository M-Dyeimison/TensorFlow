import tensorflow as tf

some_list = [1, 2, 3, 4]
some_list[:2]
some_list2 = tf.constant([[1,2,3,4], [5,6,7,8]], shape=[2,2,1,2])
some_list2
some_list2[:, :, :1, :1]
some_list2.shape

rank_4_tensor = tf.zeros(shape=[2,3,4,5])

#indexing
rank_4_tensor[:2, :2, :2, :2]

some_list[:1]

#get the first element from each dimesion from each index except for the final one
rank_4_tensor[:1, :1, :1]

rank_4_tensor[:1, :1, :, :1]

#create rank 2 tensor
rank_2_tensor = tf.constant([[10,7], [3,4]])
rank_2_tensor.ndim

some_list, some_list[-1]

#get the last item of each of row of our rank 2 tensor
rank_2_tensor[:, -1]
