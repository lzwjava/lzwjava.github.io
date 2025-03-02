---
layout: post  
title: "NumPy"
audio: false
---

### Array creation routines

*   `np.empty`: Return a new array of given shape and type, without initializing entries.
*   `np.empty_like`: Return a new array with the same shape and type as a given array.
*   `np.eye`: Return a 2-D array with ones on the diagonal and zeros elsewhere.
*   `np.identity`: Return the identity array.
*   `np.ones`: Return a new array of given shape and type, filled with ones.
*   `np.ones_like`: Return an array of ones with the same shape and type as a given array.
*   `np.zeros`: Return a new array of given shape and type, filled with zeros.
*   `np.zeros_like`: Return an array of zeros with the same shape and type as a given array.
*   `np.full`: Return a new array of given shape and type, filled with fill\_value.
*   `np.full_like`: Return a full array with the same shape and type as a given array.
*   `np.array`: Create an array.
*   `np.asarray`: Convert the input to an array.
*   `np.asanyarray`: Convert the input to an ndarray, but pass ndarray subclasses through.
*   `np.ascontiguousarray`: Return a contiguous array in memory (C order).
*   `np.asfortranarray`: Return a contiguous array in memory (Fortran order).
*   `np.copy`: Return an array copy of the given object.
*   `np.frombuffer`: Interpret a buffer as a 1-dimensional array.
*   `np.from_dlpack`: Create a NumPy array from a PyCapsule object (DLPack).
*   `np.fromfile`: Construct an array from data in a text or binary file.
*   `np.fromfunction`: Construct an array by executing a function over each coordinate.
*   `np.fromiter`: Create a new 1-dimensional array from an iterable object.
*   `np.fromstring`: A new 1-D array initialized from text data in a string.
*   `np.loadtxt`: Load data from a text file.
*   `np.genfromtxt`: Load data from a text file, with missing values handled as specified.
*   `np.savetxt`: Save an array to a text file.
*   `np.save`: Save an array to a binary file in NumPy `.npy` format.
*   `np.savez`: Save several arrays into a single file in uncompressed `.npz` format.
*   `np.savez_compressed`: Save several arrays into a single file in compressed `.npz` format.

### Array manipulation routines

*   `np.reshape`: Gives a new shape to an array without changing its data.
*   `np.ravel`: Return a contiguous flattened array.
*   `np.transpose`: Permute the dimensions of an array.
*   `np.swapaxes`: Interchange two axes of an array.
*   `np.moveaxis`: Move axes of an array to new positions.
*   `np.broadcast_to`: Broadcast an array to a new shape.
*   `np.broadcast_arrays`: Broadcast any number of arrays against each other.
*   `np.expand_dims`: Expand the shape of an array.
*   `np.squeeze`: Remove single-dimensional entries from the shape of an array.
*   `np.concatenate`: Join a sequence of arrays along an existing axis.
*   `np.stack`: Join a sequence of arrays along a new axis.
*   `np.hstack`: Stack arrays in sequence horizontally (column wise).
*   `np.vstack`: Stack arrays in sequence vertically (row wise).
*   `np.dstack`: Stack arrays in sequence depth wise (along third dimension).
*   `np.column_stack`: Stack 1-D arrays as columns into a 2-D array.
*   `np.row_stack`: Stack arrays in sequence vertically (row wise).
*   `np.split`: Split an array into multiple sub-arrays.
*   `np.array_split`: Split an array into multiple sub-arrays.
*   `np.hsplit`: Split an array into multiple sub-arrays horizontally (column-wise).
*   `np.vsplit`: Split an array into multiple sub-arrays vertically (row-wise).
*   `np.dsplit`: Split an array into multiple sub-arrays along the 3rd axis (depth-wise).
*   `np.tile`: Construct an array by repeating A the number of times given by reps.
*   `np.repeat`: Repeat elements of an array.
*   `np.delete`: Return a new array with sub-arrays along an axis deleted.
*   `np.insert`: Insert values along the given axis before the given indices.
*   `np.append`: Append values to the end of an array.
*   `np.resize`: Return a new array with the specified shape.
*   `np.trim_zeros`: Trim the leading and/or trailing zeros from a 1-D array or sequence.
*   `np.unique`: Find the unique elements of an array.

### Array indexing routines

*   `np.take`: Take elements from an array along an axis.
*   `np.choose`: Construct an array from an index array and a set of arrays to choose from.
*   `np.searchsorted`: Find indices where elements should be inserted to maintain order.
*   `np.count_nonzero`: Counts the number of non-zero values in the array ``a``.
*   `np.nonzero`: Return the indices of the elements that are non-zero.
*   `np.where`: Return elements chosen from `x` or `y` depending on `condition`.
*   `np.indices`: Return an array representing the indices of a grid.
*   `np.ix_`: Construct an open mesh from multiple sequences.
*   `np.diag_indices`: Return the indices to access the main diagonal of an array.
*   `np.diag_indices_from`: Return the indices to access the main diagonal of an n-dimensional array.
*   `np.mask_indices`: Return the indices to access (n_arrays, n_elements) with a mask.
*   `np.tril_indices`: Return the indices for the lower-triangle of an (n, n) array.
*   `np.tril_indices_from`: Return the indices for the lower-triangle of arr.
*   `np.triu_indices`: Return the indices for the upper-triangle of an (n, n) array.
*   `np.triu_indices_from`: Return the indices for the upper-triangle of arr.

### Array type routines

*   `np.dtype`: Create a data type object.
*   `np.can_cast`: Returns True if cast between data types can occur safely.
*   `np.result_type`: Returns the type that results from applying the NumPy type promotion rules to the arguments.
*   `np.min_scalar_type`: Return the data type with the smallest size and smallest scalar kind to which an array can be safely cast.
*   `np.promote_types`: Returns the data type with the smallest size and smallest scalar kind which can hold both type1 and type2.
*   `np.common_type`: Return a scalar type common to input arrays.
*   `np.obj2sctype`: Return the scalar dtype or NumPy equivalent of Python type of an object.

### Array set routines

*   `np.unique`: Find the unique elements of an array.
*   `np.intersect1d`: Find the intersection of two arrays.
*   `np.union1d`: Find the union of two arrays.
*   `np.setdiff1d`: Find the set difference of two arrays.
*   `np.setxor1d`: Find the set exclusive-or of two arrays.
*   `np.in1d`: Test whether each element of an array is also present in a second array.

### Array sorting, searching, and counting routines

*   `np.sort`: Return a sorted copy of an array.
*   `np.argsort`: Returns the indices that would sort an array.
*   `np.lexsort`: Perform an indirect stable sort using a sequence of keys.
*   `np.searchsorted`: Find indices where elements should be inserted to maintain order.
*   `np.partition`: Return a partitioned copy of an array.
*   `np.argpartition`: Perform an indirect partition along the given axis.
*   `np.argmax`: Returns the indices of the maximum values along an axis.
*   `np.argmin`: Returns the indices of the minimum values along an axis.
*   `np.max`: Return the maximum along a given axis.
*   `np.min`: Return the minimum along a given axis.
*   `np.maximum`: Element-wise maximum of array elements.
*   `np.minimum`: Element-wise minimum of array elements.
*   `np.nanargmax`: Returns the indices of the maximum values in the specified axis ignoring NaNs.
*   `np.nanargmin`: Returns the indices of the minimum values in the specified axis ignoring NaNs.
*   `np.nanmax`: Return the maximum of an array or maximum along an axis, ignoring any NaNs.
*   `np.nanmin`: Return the minimum of an array or minimum along an axis, ignoring any NaNs.
*   `np.count_nonzero`: Counts the number of non-zero values in the array ``a``.
*   `np.nonzero`: Return the indices of the elements that are non-zero.
*   `np.where`: Return elements chosen from `x` or `y` depending on `condition`.

### Array mathematics routines

*   `np.add`: Add arguments element-wise.
*   `np.subtract`: Subtract arguments element-wise.
*   `np.multiply`: Multiply arguments element-wise.
*   `np.divide`: Divide arguments element-wise.
*   `np.floor_divide`: Return the largest integer smaller or equal to the division of the inputs.
*   `np.true_divide`: Returns a true division of the inputs, element-wise.
*   `np.mod`: Return element-wise remainder of division.
*   `np.remainder`: Return element-wise remainder of division.
*   `np.divmod`: Return element-wise quotient and remainder simultaneously.
*   `np.positive`: Numerical positive, element-wise.
*   `np.negative`: Numerical negative, element-wise.
*   `np.power`: First array elements raised to powers from second array, element-wise.
*   `np.float_power`: Treat elements of arrays as floating points, element-wise.
*   `np.remainder`: Return element-wise remainder of division.
*   `np.modf`: Return the fractional and integral parts of an array, element-wise.
*   `np.angle`: Return the angle of the complex argument.
*   `np.real`: Return the real part of the complex argument.
*   `np.imag`: Return the imaginary part of the complex argument.
*   `np.conj`: Return the complex conjugate, element-wise.
*   `np.convolve`: Returns the discrete, linear convolution of two one-dimensional sequences.
*   `np.gcd`: Returns the greatest common divisor of ``|x1|`` and ``|x2|``
*   `np.lcm`: Returns the lowest common multiple of ``|x1|`` and ``|x2|``

### Array bitwise routines

*   `np.bitwise_and`: Compute the bit-wise AND of two arrays element-wise.
*   `np.bitwise_or`: Compute the bit-wise OR of two arrays element-wise.
*   `np.bitwise_xor`: Compute the bit-wise XOR of two arrays element-wise.
*   `np.invert`: Compute bit-wise inversion, or bit-wise NOT, element-wise.
*   `np.left_shift`: Shift the bits of an integer to the left.
*   `np.right_shift`: Shift the bits of an integer to the right.

### Array string operations

*   `np.char.add`: Return element-wise string concatenation for two arrays of str or unicode.
*   `np.char.multiply`: Return (a * i), that is string multiple of i copies of a , for each element.
*   `np.char.mod`: Return (a % i), that is pre-Python 2.6 string formatting (interpolation), for each element in a.
*   `np.char.capitalize`: Return a copy of `a` with only the first character of each element capitalized.
*   `np.char.lower`: Return an array with the elements converted to lowercase.
*   `np.char.upper`: Return an array with the elements converted to uppercase.
*   `np.char.title`: For each element in `a`, return a titlecased version of the string: words start with uppercase characters, all remaining cased characters are lowercase.
*   `np.char.split`: For each element in `a`, return a list of the words in the string, using sep as the delimiter string.
*   `np.char.splitlines`: For each element in `a`, return a list of the lines in the element, breaking at line boundaries.
*   `np.char.strip`: For each element in `a`, return a copy with the leading and trailing characters removed.
*   `np.char.lstrip`: For each element in `a`, return a copy with the leading characters removed.
*   `np.char.rstrip`: For each element in `a`, return a copy with the trailing characters removed.
*   `np.char.join`: Return a string which is the concatenation of the strings in the sequence seq.
*   `np.char.replace`: For each element in `a`, return a copy of the string with all occurrences of substring old replaced by new.
*   `np.char.encode`: Calls `str.encode` element-wise.
*   `np.char.decode`: Calls `str.decode` element-wise.

### Array trigonometric functions

*   `np.sin`: Trigonometric sine, element-wise.
*   `np.cos`: Cosine element-wise.
*   `np.tan`: Compute tangent element-wise.
*   `np.arcsin`: Inverse sine, element-wise.
*   `np.arccos`: Trigonometric inverse cosine, element-wise.
*   `np.arctan`: Trigonometric inverse tangent, element-wise.
*   `np.arctan2`: Element-wise arc tangent of ``x1/x2`` choosing the quadrant correctly.
*   `np.hypot`: Given the "legs" of a right triangle, return its hypotenuse.
*   `np.degrees`: Convert angles from radians to degrees.
*   `np.radians`: Convert angles from degrees to radians.
*   `np.unwrap`: Unwrap by changing deltas between values to 2\*pi complement.
*   `np.deg2rad`: Convert angles from degrees to radians.
*   `np.rad2deg`: Convert angles from radians to degrees.

### Array hyperbolic functions

*   `np.sinh`: Hyperbolic sine, element-wise.
*   `np.cosh`: Hyperbolic cosine, element-wise.
*   `np.tanh`: Compute hyperbolic tangent element-wise.
*   `np.arcsinh`: Inverse hyperbolic sine element-wise.
*   `np.arccosh`: Inverse hyperbolic cosine, element-wise.
*   `np.arctanh`: Inverse hyperbolic tangent element-wise.

### Array rounding

*   `np.around`: Evenly round to the given number of decimals.
*   `np.rint`: Round elements of the array to the nearest integer.
*   `np.fix`: Round to nearest integer towards zero.
*   `np.floor`: Return the floor of the input, element-wise.
*   `np.ceil`: Return the ceiling of the input, element-wise.
*   `np.trunc`: Return the truncated value of the input, element-wise.

### Array sums and products

*   `np.sum`: Sum of array elements over a given axis.
*   `np.prod`: Return the product of array elements over a given axis.
*   `np.nansum`: Return the sum of array elements over a given axis treating Not a Numbers (NaNs) as zero.
*   `np.nanprod`: Return the product of array elements over a given axis treating Not a Numbers (NaNs) as one.
*   `np.cumsum`: Return the cumulative sum of the elements along a given axis.
*   `np.cumprod`: Return the cumulative product of elements along a given axis.
*   `np.nancumsum`: Return the cumulative sum of the elements along a given axis treating Not a Numbers (NaNs) as zero.
*   `np.nancumprod`: Return the cumulative product of the elements along a given axis treating Not a Numbers (NaNs) as one.
*   `np.diff`: Calculate the n-th discrete difference along the given axis.
*   `np.ediff1d`: The differences between consecutive elements of an array.
*   `np.gradient`: Return the gradient of an N-dimensional array.
*   `np.cross`: Return the cross product of two (arrays of) vectors.
*   `np.trapz`: Integrate along the given axis using the composite trapezoidal rule.

### Array exponents and logarithms

*   `np.exp`: Calculate the exponential of all elements in the input array.
*   `np.expm1`: Calculate ``exp(x) - 1`` for all elements in the array.
*   `np.log`: Natural logarithm, element-wise.
*   `np.log1p`: Return the natural logarithm of one plus the input array, element-wise.
*   `np.log2`: Base-2 logarithm of `x`.
*   `np.log10`: Return the base 10 logarithm of the input array, element-wise.
*   `np.logaddexp`: Logarithm of the sum of exponentials of inputs.
*   `np.logaddexp2`: Logarithm of the sum of exponentials of inputs in base-2.

### Array other special functions

*   `np.i0`: Modified Bessel function of the first kind, order 0.
*   `np.sinc`: Return the sinc function.

### Array floating point routines

*   `np.signbit`: Returns element-wise True where signbit is set (less than zero).
*   `np.copysign`: Change the sign of x1 to that of x2, element-wise.
*   `np.frexp`: Decompose elements into mantissa and twos exponent.
*   `np.ldexp`: Returns x1 * 2**x2, element-wise.
*   `np.nextafter`: Return the next floating-point value after x1 towards x2, element-wise.
*   `np.spacing`: Return the distance between x and the nearest adjacent number.

### Array rational routines

*   `np.lcm`: Returns the lowest common multiple of ``|x1|`` and ``|x2|``
*   `np.gcd`: Returns the greatest common divisor of ``|x1|`` and ``|x2|``

### Array handling missing data

*   `np.isnan`: Test element-wise for NaN and return result as a boolean array.
*   `np.isinf`: Test element-wise for positive or negative infinity.
*   `np.isposinf`: Test element-wise for positive infinity.
*   `np.isneginf`: Test element-wise for negative infinity.
*   `np.isfinite`: Test element-wise for finiteness (not infinity or not Not a Number).
*   `np.nan_to_num`: Replace NaN with zero and infinity with large finite numbers (positive numbers with max, negative numbers with min).
*   `np.real_if_close`: If complex input returns a real array if complex parts are close to zero.
*   `np.nanargmin`: Returns the indices of the minimum values in the specified axis ignoring NaNs.
*   `np.nanargmax`: Returns the indices of the maximum values in the specified axis ignoring NaNs.
*   `np.nansum`: Return the sum of array elements over a given axis treating Not a Numbers (NaNs) as zero.
*   `np.nanprod`: Return the product of array elements over a given axis treating Not a Numbers (NaNs) as one.
*   `np.nancumsum`: Return the cumulative sum of the elements along a given axis treating Not a Numbers (NaNs) as zero.
*   `np.nancumprod`: Return the cumulative product of the elements along a given axis treating Not a Numbers (NaNs) as one.
*   `np.nanmean`: Compute the arithmetic mean along the specified axis, ignoring NaNs.
*   `np.nanmedian`: Compute the median along the specified axis, while ignoring NaNs.
*   `np.nanpercentile`: Compute the q-th percentile of the data along the specified axis, while ignoring nan values.
*   `np.nanquantile`: Compute the q-th quantile of the data along the specified axis, while ignoring nan values.
*   `np.nanstd`: Compute the standard deviation along the specified axis, while ignoring NaNs.
*   `np.nanvar`: Compute the variance along the specified axis, while ignoring NaNs.

### Array linear algebra

*   `np.dot`: Dot product of two arrays.
*   `np.linalg.solve`: Solve a linear matrix equation, or system of linear scalar equations.
*   `np.linalg.eig`: Compute the eigenvalues and right eigenvectors of a square array.
*   `np.linalg.inv`: Compute the (multiplicative) inverse of a matrix.
*   `np.linalg.det`: Compute the determinant of an array.
*   `np.linalg.norm`: Matrix or vector norm.
*   `np.trace`: Return the sum along diagonals of the array.
*   `np.linalg.qr`: Compute the qr factorization of a matrix.
*   `np.linalg.svd`: Singular Value Decomposition.
*   `np.linalg.cholesky`: Cholesky decomposition.

### Array statistics

*   `np.mean`: Compute the arithmetic mean along the specified axis.
*   `np.average`: Compute the weighted average along the specified axis.
*   `np.std`: Compute the standard deviation along the specified axis.
*   `np.var`: Compute the variance along the specified axis.
*   `np.median`: Compute the median along the specified axis.
*   `np.percentile`: Compute the q-th percentile of the data along the specified axis.
*   `np.quantile`: Compute the q-th quantile of the data along the specified axis.
*   `np.corrcoef`: Pearson product-moment correlation coefficients.
*   `np.cov`: Estimate a covariance matrix, given data and weights.
*   `np.histogram`: Compute the histogram of a set of data.
*   `np.histogram2d`: Compute the bi-dimensional histogram of two data samples.
*   `np.histogramdd`: Compute the N-dimensional histogram of some sample(s).
*   `np.bincount`: Count number of occurrences of each value in array of non-negative ints.
*   `np.digitize`: Return the indices of the bins to which each value in input array belongs.

### Array mathematical constants

*   `np.pi`: Mathematical constant, the ratio of a circle's circumference to its diameter.
*   `np.e`: Mathematical constant, base of natural logarithms.

### Array logic functions

*   `np.all`: Test whether all array elements along a given axis evaluate to True.
*   `np.any`: Test whether any array elements along a given axis evaluate to True.
*   `np.array_equal`: True if two arrays have the same shape and elements, False otherwise.
*   `np.array_equiv`: Returns True if input arrays are shape consistent and all elements equal.
*   `np.greater`: Return the truth value of (x1 > x2) element-wise.
*   `np.greater_equal`: Return the truth value of (x1 >= x2) element-wise.
*   `np.less`: Return the truth value of (x1 < x2) element-wise.
*   `np.less_equal`: Return the truth value of (x1 <= x2) element-wise.
*   `np.equal`: Return (x1 == x2) element-wise.
*   `np.not_equal`: Return (x1 != x2) element-wise.
*   `np.logical_and`: Compute the truth value of x1 AND x2 element-wise.
*   `np.logical_or`: Compute the truth value of x1 OR x2 element-wise.
*   `np.logical_not`: Compute the truth value of NOT x element-wise.
*   `np.logical_xor`: Compute the truth value of x1 XOR x2, element-wise.

### Array comparison

*   `np.isclose`: Returns a boolean array where two arrays are equal within a tolerance.
*   `np.allclose`: Returns True if two arrays are element-wise equal within a tolerance.

### Array random sampling

*   `np.random.rand`: Create an array of the given shape and populate it with random samples from a uniform distribution over ``[0, 1)``.
*   `np.random.randn`: Return a sample (or samples) from the "standard normal" distribution.
*   `np.random.randint`: Return random integers from `low` (inclusive) to `high` (exclusive).
*   `np.random.random`: Return random floats in the half-open interval [0.0, 1.0).
*   `np.random.choice`: Generates a random sample from a given 1-D array
*   `np.random.seed`: Seed the generator.

### Array Input and output

*   `np.save`: Save an array to a binary file in NumPy ``.npy`` format.
*   `np.load`: Load arrays or pickled objects from ``.npy``, ``.npz`` or pickled files.
*   `np.savetxt`: Save an array to a text file.
*   `np.loadtxt`: Load data from a text file.
*   `np.genfromtxt`: Load data from a text file, with missing values handled as specified.

### Array Fourier Transform

*   `np.fft.fft`: Compute the one-dimensional discrete Fourier Transform.
*   `np.fft.ifft`: Compute the one-dimensional inverse discrete Fourier Transform.
*   `np.fft.fft2`: Compute the 2-D discrete Fourier Transform
*   `np.fft.ifft2`: Compute the 2-D inverse discrete Fourier Transform.
*   `np.fft.fftn`: Compute the N-dimensional discrete Fourier Transform.
*   `np.fft.ifftn`: Compute the N-dimensional inverse discrete Fourier Transform.

### Array reshaping

*   `np.reshape`: Gives a new shape to an array without changing its data.
*   `np.ravel`: Return a contiguous flattened array.

### Array joining and splitting

*   `np.concatenate`: Join a sequence of arrays along an existing axis.
*   `np.stack`: Join a sequence of arrays along a new axis.
*   `np.split`: Split an array into multiple sub-arrays.

### Array indexing

*   `np.where`: Return elements chosen from `x` or `y` depending on `condition`.
*   `np.take`: Take elements from an array along an axis.

### Array data type

*   `np.dtype`: Create a data type object.

### Array memory layout

*   `np.ascontiguousarray`: Return a contiguous array in memory (C order).

### Array broadcasting

*   `np.broadcast_to`: Broadcast an array to a new shape.

### Array masked array operations

*   `np.ma.masked_array`: An array class with possibly masked values.

### Array polynomial functions

*   `np.polyfit`: Least squares polynomial fit.
*   `np.polyval`: Evaluate a polynomial at specific values.

### Array window functions

*   `np.hanning`: Return the Hanning window.

### Array datetime support

*   `np.datetime64`: A generic date/time representation.

### Array performance enhancements

*   `np.vectorize`: Define a vectorized function.

### Array miscellaneous

*   `np.copy`: Return an array copy of the given object.
*   `np.meshgrid`: Return coordinate matrices from coordinate vectors.

