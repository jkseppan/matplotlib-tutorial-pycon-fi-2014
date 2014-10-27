#with style.context('fivethirtyeight'):
with plt.xkcd():
    plot([3,1,4,1,5,9,2,6,5,3])
    xlim([-0.5, 9.5])
    ylim([0, 9.5])
    ax = gca()
    #children = ax.get_children()
    #line = children[2]
    #line.set_solid_joinstyle('miter')
    setp(ax, xlabel='hello')
    ax.set_ylabel('world', size=15)
    ax.yaxis.set_tick_params(labelsize=20)
