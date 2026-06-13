## ML Algorithm Blueprint

A structured comment block for implementing ML algorithms from scratch.

```python
"""
# GOAL
What the algorithm learns or computes in plain language.

# MATH
Core formula or update rule. e.g. w = w - lr * dL/dw

# INPUT / OUTPUT
Input types and shapes. Expected output type and shape.

# STEPS
1. Initialize weights/centroids/parameters
2. Forward pass / compute predictions
3. Compute loss / distance / objective
4. Update parameters / assignments
5. Repeat until convergence or n_iterations

# HYPERPARAMETERS
e.g. learning_rate, n_iterations, n_clusters, threshold, tolerance

# DIMENSIONS
e.g. X: (n_samples, n_features), w: (n_features,), y: (n_samples,)

# COMPLEXITY
time: O(?)
space: O(?)

# EDGE CASES
Non-convergence, learning rate too large, division by zero, singular matrix, empty input.
"""
```