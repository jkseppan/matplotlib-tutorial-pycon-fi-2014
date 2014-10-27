print style.available
with style.context('fivethirtyeight'):
    plot([3,1,4,1,5,9,2,6,5,3])
    xlim([-0.5, 9.5])
    ylim([0, 9.5])
