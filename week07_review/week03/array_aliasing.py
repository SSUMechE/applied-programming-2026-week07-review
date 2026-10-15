from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class UnsafeConfiguration:
    values: np.ndarray

source = np.array([0.0, 0.0])
q = UnsafeConfiguration(source)
source[0] = 99.0
print(q.values)
