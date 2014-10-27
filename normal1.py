fig, (ax1, ax2) = subplots(nrows=2)
x = linspace(-4, 4, 300)
ax1.plot(x, norm.pdf(x))
ax2.plot(x, norm.cdf(x))
