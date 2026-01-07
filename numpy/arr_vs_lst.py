import numpy as np
import timeit

list_time = timeit.timeit(
    '[i**5 for i in range(1, 10)]',
    number=1_000_000
)

numpy_time = timeit.timeit(
    'np.arange(1, 10) ** 5',
    globals=globals(),
    number=1_000_000
)

print("List comprehension time:", list_time)
print("NumPy time:", numpy_time)
