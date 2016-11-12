import tensorflow as tf

# The tf.reduce_sum() function takes an array of numbers and sums them together.
#
#   https://www.tensorflow.org/api_docs/python/math_ops.html#reduce_sum
#
x = tf.reduce_sum([1, 2, 3, 4, 5])

tf.initialize_all_variables()
with tf.Session() as sess:
    output = sess.run(x)
    print(output)
