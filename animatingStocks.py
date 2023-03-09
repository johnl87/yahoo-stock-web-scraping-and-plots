import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style



style.use('fivethirtyeight')
fig = plt.figure()
#number of figures, add more figures, axn where n is the figure number
#2 x 2 plot
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

def animate(i):
    df = pd.read_csv('stock data.csv')
    #get the stock value from second column and on wards using notation
    ys = df.iloc[1:, 2].values      #y-axis
    xs = list(range(1,len(ys)+1))   #x-axis
    ax1.clear()
    ax1.plot(xs, ys) #(x,y)
    ax1.set_title('MSFT', fontsize = 12)
    
    ys = df.iloc[1:, 3].values      #y-axis
    ax2.clear()
    ax2.plot(xs, ys) #(x,y)
    ax2.set_title('AAPL', fontsize = 12)
    
    ys = df.iloc[1:, 4].values      #y-axis
    ax3.clear()
    ax3.plot(xs, ys) #(x,y)
    ax3.set_title('S&P 500', fontsize = 12)
    
    ys = df.iloc[1:, 5].values      #y-axis
    ax4.clear()
    ax4.plot(xs, ys) #(x,y)
    ax4.set_title('NASDAQ', fontsize = 12)

#(figures, animate function, interval in ms - 1000 ms = 1 seconds)    
ani = animation.FuncAnimation(fig, animate, interval = 100, cache_frame_data=False)

#tight layout for plots
plt.tight_layout()
#showing the plots
plt.show()    