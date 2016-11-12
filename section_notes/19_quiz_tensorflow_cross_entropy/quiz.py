# Solution is available in the other "solution.py" tab
import tensorflow as tf

"""

  tf.reduce_sum() - https://www.tensorflow.org/api_docs/python/math_ops.html#reduce_sum
  tf.log() - https://www.tensorflow.org/api_docs/python/math_ops.html#log

"""
def run():
    softmax_data = [0.7, 0.2, 0.1]
    one_hot_encod_label = [1.0, 0.0, 0.0]

    softmax = tf.placeholder(tf.float32)
    one_hot_encod = tf.placeholder(tf.float32)

    # ToDo: Calculate cross entropy
    cross_entropy = -tf.reduce_sum(tf.mul(one_hot_encod, tf.log(softmax)))

    with tf.Session() as sess:
        # TODO: Feed softmax and one_hot_encod data
        output = sess.run(cross_entropy, feed_dict={softmax: softmax_data, one_hot_encod: one_hot_encod_label})

    return output

print(run())