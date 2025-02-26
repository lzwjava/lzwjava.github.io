---
layout: post  
title: "PyTorch"  
audio: false
---

### torch functions

*   `torch.Tensor`: A multi-dimensional array containing elements of a single data type.
*   `torch.tensor`: Constructs a tensor with data and properties.
*   `torch.zeros`: Returns a tensor filled with zeros.
*   `torch.ones`: Returns a tensor filled with ones.
*   `torch.arange`: Returns a 1-D tensor of evenly spaced values.
*   `torch.linspace`: Returns a 1-D tensor of evenly spaced values over a specified interval.
*   `torch.rand`: Returns a tensor filled with random numbers from a uniform distribution on the interval [0, 1).
*   `torch.randn`: Returns a tensor filled with random numbers from a normal distribution with mean 0 and variance 1.
*   `torch.empty`: Returns a tensor with uninitialized data.
*   `torch.full`: Creates a tensor of specified size filled with a specified value.
*   `torch.eye`: Returns a 2-D tensor with ones on the diagonal and zeros elsewhere.

### Tensor operations

*   `torch.add`: Adds two tensors element-wise.
*   `torch.sub`: Subtracts two tensors element-wise.
*   `torch.mul`: Multiplies two tensors element-wise.
*   `torch.div`: Divides two tensors element-wise.
*   `torch.matmul`: Performs matrix multiplication.
*   `torch.pow`: Raises each element of a tensor to a power.
*   `torch.exp`: Calculates the exponential of each element of a tensor.
*   `torch.log`: Calculates the natural logarithm of each element of a tensor.
*   `torch.sqrt`: Calculates the square root of each element of a tensor.
*   `torch.abs`: Calculates the absolute value of each element of a tensor.
*   `torch.neg`: Negates each element of a tensor.
*   `torch.round`: Rounds each element of a tensor to the nearest integer.
*   `torch.floor`: Returns the floor of each element of a tensor.
*   `torch.ceil`: Returns the ceiling of each element of a tensor.
*   `torch.clamp`: Clamps all elements in input into the range [ min, max ].
*   `torch.sum`: Returns the sum of all elements in the input tensor.
*   `torch.mean`: Returns the mean of all elements in the input tensor.
*   `torch.std`: Returns the standard deviation of all elements in the input tensor.
*   `torch.var`: Returns the variance of all elements in the input tensor.
*   `torch.max`: Returns the maximum value of all elements in the input tensor.
*   `torch.min`: Returns the minimum value of all elements in the input tensor.
*   `torch.argmax`: Returns the index of the maximum value of all elements in the input tensor.
*   `torch.argmin`: Returns the index of the minimum value of all elements in the input tensor.
*   `torch.sort`: Sorts the elements of the input tensor along a given dimension.
*   `torch.topk`: Returns the k largest elements of the input tensor along a given dimension.
*   `torch.reshape`: Returns a tensor with the same data and number of elements as input, but with the specified shape.
*   `torch.transpose`: Returns a view of the input tensor with its dimensions swapped.
*   `torch.squeeze`: Returns a tensor with all the dimensions of input of size 1 removed.
*   `torch.unsqueeze`: Returns a new tensor with a dimension of size one inserted at the specified position.
*   `torch.cat`: Concatenates the given tensors in the given dimension.
*   `torch.stack`: Concatenates a sequence of tensors along a new dimension.
*   `torch.chunk`: Splits a tensor into a specific number of chunks.
*   `torch.split`: Splits a tensor into chunks of a specific size.

### Neural network modules

*   `torch.nn.Module`: Base class for all neural network modules.
*   `torch.nn.Linear`: Applies a linear transformation to the incoming data.
*   `torch.nn.Conv2d`: Applies a 2D convolution over an input signal composed of several input planes.
*   `torch.nn.MaxPool2d`: Applies a 2D max pooling over an input signal.
*   `torch.nn.ReLU`: Applies the rectified linear unit function element-wise.
*   `torch.nn.Sigmoid`: Applies the sigmoid function element-wise.
*   `torch.nn.Tanh`: Applies the hyperbolic tangent function element-wise.
*   `torch.nn.BatchNorm2d`: Applies Batch Normalization over a 4D input.
*   `torch.nn.Dropout`: During training, randomly zeroes some of the elements of the input tensor with probability p.
*   `torch.nn.Embedding`: A simple lookup table that stores embeddings of a fixed dictionary and size.

### Loss functions

*   `torch.nn.MSELoss`: Creates a criterion that measures the mean squared error (squared L2 norm) between each element in the input and target.
*   `torch.nn.CrossEntropyLoss`: This criterion computes the cross entropy loss between input and target.
*   `torch.nn.BCELoss`: Creates a criterion that measures the Binary Cross Entropy between the target and the output.
*   `torch.nn.L1Loss`: Creates a criterion that measures the mean absolute error (MAE) between each element in the input and target.

### Optimizers

*   `torch.optim.SGD`: Implements stochastic gradient descent (optionally with momentum).
*   `torch.optim.Adam`: Implements Adam algorithm.
*   `torch.optim.RMSprop`: Implements RMSprop algorithm.

### Autograd

*   `torch.autograd.grad`: Computes and returns the sum of gradients of outputs with respect to the inputs.

### Utilities

*   `torch.device`: Represents the device on which a torch.Tensor is or will be allocated.
*   `torch.cuda.is_available`: Returns True if CUDA is available.
*   `torch.save`: Saves a tensor to disk.
*   `torch.load`: Loads a tensor from disk.

### Other

*   `torch.no_grad`: Context-manager that disables gradient calculation.
*   `torch.set_grad_enabled`: Enable or disable grad, depending on its argument.

