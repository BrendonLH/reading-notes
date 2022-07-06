# Data Visualization

## Seaborn
Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. -seaborn.com

## MapPlotLib
- example of adding some color to the visual
  when creating the plot we can specify the color used, this will allow us to differentiate the data shown.
    > plt.plot(x, y, color = 'red)

- the spines are the lines that show us the range of our data. this is like the x and y axis lines. These can be changed and moved to other places
    > ax = plot.gca()
      ax.spines['right'].set_color('none')
      ax.spines['top'].set_color('none')
      ax.xaxis.set_ticks_position('bottom')
      ax.spines['bottom'].set_position(('data',0))
      ax.yaxis.set_ticks_position('left')
      ax.spines['left'].set_position(('data',0))

## Things I want to know more about
- am I going to have to learn sines and cosines again? I hated it back in high school and I don't imagine ill enjoy it now.