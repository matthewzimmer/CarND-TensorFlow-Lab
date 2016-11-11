# Solution is available in the other "solution.py" tab
import numpy as np
import math

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)
    """
      S(yi) = e^yi / Σj e^yi
    """
    # return np.exp(x) / np.sum(np.exp(x), axis=0)
    return [math.exp(x_i) / sum([math.exp(float(y_i)) for y_i in x]) for x_i in x]

logits = [3.0, 1.0, 0.2]
# logits = [1., 2., 3.]
print(softmax(logits))
