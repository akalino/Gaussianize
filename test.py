from gaussianize import Gaussianize
import numpy as np


def run_tests():
    x = np.hstack([np.random.standard_cauchy(size=(1000, 2)), np.random.normal(size=(1000, 2))])
    out = Gaussianize()
    out.fit(x)
    y = out.transform(x)
    x_prime = out.normal_to_observed(y)  # Recover the initial distribution
    print(np.allclose(x_prime, x))

if __name__ == '__main__':
    run_tests()

