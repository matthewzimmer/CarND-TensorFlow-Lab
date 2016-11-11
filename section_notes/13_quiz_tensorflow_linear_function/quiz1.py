# Solution is available in the other "solution.py" tab
import tensorflow as tf


def run():
    output = None

    x = tf.Variable([1, 2, 3, 4])

    # ToDo: Create operation to initalize all variables
    init = tf.initialize_all_variables()
    with tf.Session() as sess:
        # ToDo: Initialize all variables
        sess.run(init)
        output = sess.run(x)

    return output
print(run())