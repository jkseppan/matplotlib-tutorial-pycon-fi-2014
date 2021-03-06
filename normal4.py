fig, (ax1, ax2) = subplots(nrows=2, gridspec_kw=dict(hspace=0.4))

x = linspace(-4, 4, 300)
pdf = norm.pdf(x)
cdf = norm.cdf(x)
idx = 170

def setup_axis(ax):
    ax.set_xlim(-4.5, 4.5)
    ax.set_xticks(range(-4, 5))
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
ax1.fill_between(x[:idx], pdf[:idx], color='g')
ax1.set_ylim(-0.05, 0.45)
ax1.set_ylabel('density', size=20)
ax1.spines['left'].set_bounds(0, max(pdf))
ax1.spines['bottom'].set_bounds(-4, 4)

ax2.plot(x, norm.cdf(x), 'g', lw=2)
ax2.grid(linestyle=':')
ax2.set_ylim(-0.05, 1.05)
ax2.set_ylabel('cumulative', size=20)
ax2.set_yticks(norm.cdf([-2,-1,0,1,2]))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax2.spines['left'].set_bounds(0, 1)
ax2.spines['bottom'].set_bounds(-4, 4)
vline=ax2.vlines(x[idx-1], 0, 2.65, lw=2, linestyle='--')
vline.set_clip_on(False)
ax2.hlines(cdf[idx-1], -5, x[idx-1], lw=2, linestyle='--')

ax1.text(0.1, 0.7, r'$\frac{1}{\sqrt{2\pi}}e^{\frac{-x^2}{2}}$',
         fontsize=30, transform=ax1.transAxes)
