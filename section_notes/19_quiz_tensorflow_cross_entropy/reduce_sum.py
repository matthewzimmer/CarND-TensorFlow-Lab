import tensorflow as tf

x = tf.reduce_sum([1, 2, 3, 4, 5])

tf.initialize_all_variables()
with tf.Session() as sess:
    output = sess.run(x)
    print(output)
