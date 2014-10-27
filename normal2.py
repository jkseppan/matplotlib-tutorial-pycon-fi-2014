fig, (ax1, ax2) = subplots(nrows=2, gridspec_kw=dict(hspace=0.4))

x = linspace(-4, 4, 300)
pdf = norm.pdf(x)
cdf = norm.cdf(x)

def setup_axis(ax):
    ax.set_xlim(-4.5, 4.5)
    ax.xaxis.set_tick_params(labelsize=14, direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_tick_params(labelsize=14, direction='out')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_position(('outward', 10))
    ax.spines['left'].set_position(('outward', 10))

setup_axis(ax1); setup_axis(ax2)
ax1.plot(x, norm.pdf(x), lw=2)
ax1.set_ylim(-0.05, 0.45)
ax2.plot(x, norm.cdf(x), 'g', lw=2)
ax2.set_ylim(-0.05, 1.05)
