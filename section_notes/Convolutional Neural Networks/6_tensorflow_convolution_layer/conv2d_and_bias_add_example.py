import tensorflow as tf

k_output = 64
input = tf.placeholder(tf.float32, shape=[None, 10, 10, 3])
weight = tf.Variable(tf.truncated_normal([5, 5, 3, k_output]))
bias = tf.Variable(tf.zeros(k_output))

# Apply Convolution
conv_layer = tf.nn.conv2d(input, weight, strides=[1, 2, 2, 1], padding='SAME')
# Add bias
conv_layer = tf.nn.bias_add(conv_layer, bias)
conv_layer = tf.nn.relu(conv_layer)

print(conv_layer)