# Gaussianize
Computing means and standard deviations on distributions with severe skew
and kurtosis can be dangerous, especially when these metrics are being
compared to make algorithmic decisions. The process of Gaussianizing
 a distribution can be used to transform distributions to their normal
 counterpart and back. Gaussianization is available in the R LambertW package
 but there was no good alternative for Python. I lifted some code from a few
  different tutorials and cobbled this together to fit my needs.
