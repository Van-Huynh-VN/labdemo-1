import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

wine_reviews=pd.read_csv(r"C:\Users\DELL\Downloads\winemag-data-130k-v2.csv")

# Numpy
df = pd.DataFrame(np.random.randn(50, 3), index = pd.date_range("10/08/2021", periods=50), columns=list("XYZ"))
df.plot()
plt.show()

import seaborn as sns
iris=sns.load_dataset('iris')

# Scatter plot

# Pandas
iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset')
# create a figure and axis
fig, ax = plt.subplots()

# scatter the sepal_length agains the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

# seaborn
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)


# create color dictionary
colors = {
    'setosa':'r',
    'versicolor':'g',
    'virginica':'b'
}
#create a figure and axis
fig, ax = plt.subplots()
# plot each data-point
for i in range(len(iris['sepal_length'])):
    ax.scatter(
        iris['sepal_length'][i],
        iris['sepal_width'][i],
        color=colors[iris['species'][i]])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

#seaborn
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)


# Line chart

# Pandas
iris.drop(['species'], axis=1).plot.line(title='Iris Dataset')

# Matplotlib
columns = iris.columns.drop(['species'])
x_data = range(0, iris.shape[0])
fig, ax = plt.subplots()
for column in columns:
    ax.plot(x_data, iris[column])
ax.set_title('Iris Dataset')
ax.legend()

# Seaborn
sns.lineplot(data=iris.drop(['species'], axis=1))


# Bar chart

# Pandas
wine_reviews['points'].value_counts().sort_index().plot.bar()

wine_reviews['points'].value_counts().sort_index().plot.barh()

# Matplotlib
fig, ax = plt.subplots()
data = wine_reviews['points'].value_counts()
points = data.index
frequency = data.values

ax.bar(points, frequency)
ax.set_title('Wine Reviews Score')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')

# seaborn
sns.countplot(wine_reviews['points']) # chay se dung may


# Histogram

# Pandas
wine_reviews['points'].plot.hist()

# Matplotlib
fig, ax = plt.subplots()
ax.hist(wine_reviews['points'])

ax.set_title('Wine Reviews Scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')

# seaborn
sns.distplot(wine_reviews['points'], bins=10, kde=False)


# heatmap matplotlib
corr = iris.corr(numeric_only=True)
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alligment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over date dimension and create text annotations
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")

#heatmapseaborn
sns.heatmap(iris.corr(numeric_only=True), annot=True)


# Mutilple histogram
iris.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20)

#seaborn
sns.distplot(wine_reviews['points'], bins=10, kde=True)

#boxplot
up = wine_reviews[(wine_reviews['points']>=95) & (wine_reviews['price']<1000)]
sns.boxplot(x='points', y='price', data=up)

# Matplotlib - Histogram

# Thiết lập dữ liệu ngẫu nhiên
np.random.seed(10**7)
mu = 121
sigma = 21
x = mu + sigma * np.random.randn(1000)

num_bins = 100

# Vẽ biểu đồ histogram
n, bins, patches = plt.hist(x, num_bins, density=1, color="red", alpha=0.7)

# Tính toán đường cong phân phối chuẩn (Normal Distribution)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

# Vẽ đường nét đứt màu đen
plt.plot(bins, y, "--", color="black")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Hist() function example\n", fontweight="bold")

plt.show()


#Piechart
stores = ["Burgerking", "KFC", "Macdonald", "DanDan"]
scores = ["5", "5.3", "4.7", "5.5"]

plt.pie(scores, labels=stores)
plt.title("No meaning's Scores")
plt.show()


#3d point
def figax3d():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    return fig, ax

def draw_pos(ax, pos, **kwargs):
    x, y, z = zip(*pos)
    line = ax.plot(x, y, z, marker='o', ls='', **kwargs)
    return line[0]

if __name__ == '__main__':
 #   pos = np.array([
 #      [-0.5, 0, 0],
 #      [0.5, 0, 0]
 #      ])
    all_pos = np.random.randn(1, 64, 3)
 #  all_pos = np.load.txt('all_pos.dat).reshape(-1, 64, 3) 
    pos = all_pos[-1]
    
    fig, ax = figax3d()
#    draw_pos(ax, pos, c='r')
#    line = ax.scatter(x, y, z, marker='o', s=[100, 5], c=['r', 'b'])
    draw_pos(ax, pos[:32], c='r', alpha=0.5)
    draw_pos(ax, pos[32:], c='b')
    
    plt.show()
# end__main__



# 3dmatplotlib
import numpy as np
import matplotlib.pyplot as plt
#from helper.vis.pos_vel3d import figax3d, set_lims

def get_cmap(name):
    from matplotlib import cm
    cmap = cm.get_cmap(name)
    return cmap

def get_norm(vmin, vmax):
    norm = plt.Normalize(vmin, vmax)
    return norm

def scalar_v2c(vmin, vmax, name='viridis'):
    cmap = get_cmap(name)
    norm = get_norm(vmin, vmax)
    def v2c(v):  # function mapping value to color
        return cmap(norm(v))
    return v2c

def color_scatter(ax, pos, val):
    v2c = scalar_v2c(val.min(), val.max())
    x, y, z = zip(*pos)
    scat = ax.scatter(x, y, z, marker='o', c=v2c(val))
    return scat

if __name__ == '__main__':
    # get last frame from simulation
    all_pos = np.random.randn(1, 64, 3)
    all_vel = np.random.randn(1, 64, 3)
#   all_pos = np.loadtxt('all_pos.dat').reshape(-1, 64, 3)
#   all_vel = np.loadtxt('all_vel.dat').reshape(-1, 64, 3)
    
    pos = all_pos[-1]
    vel = all_vel[-1]
    
    # build color function from velocity^2
    v2 = np.sum(vel**2, axis=-1)
    
    fig, ax = figax3d()
    color_scatter(ax, pos, v2)
    plt.show()
# end main


#Seaborn-Faceting
    g = sns.FacetGrid(iris, col='species')
    g = g.map(sns.kdeplot, 'sepal_length')

#sb - pairplot
sns.pairplot(iris)

#sb - pairplot
from pandas.plotting import scatter_matrix

fig, ax = plt.subplots(figsize=(12,12))
scatter_matrix(iris, alpha=1, ax=ax)


#seaborn
import seaborn as sb
sb.set_theme(style="dark")
n=1000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y =rng.multivariate_normal(mean, cov, n).T
f, ax = plt.subplots(figsize=(6, 6))
scatter = sb.scatterplot(x=x, y=y, s=5, color=".15")
his = sb.histplot(x=x, y=y, bins=50, pthresh=0.1, cmap="mako")
kde = sb.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

plt.show()

#ploty
import plotly.express as px

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()

import webbrowser
webbrowser.open("https://127.0.0.1:8050")

#plotly
import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
app = Dash(__name__)

# df = px.data.iris()
app.layout = html.Div([
    dcc.Graph(id="scatter-plot"),
    html.P("Petal Width:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])

@app.callback(
    Output("scatter-plot", "figure"),
    [Input("range-slider", "value")]
)
def update_bar_chart(slider_range):
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length",
        color="species", size='petal_length',
        hover_data=['petal_width'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=False)
    import webbrowser
    webbrowser.open("https://127.0.0.1:8050")
    
#ggplot - geom_point
from plotnine import *

from plotnine.data import diamonds
from plotnine.data import mpg, meat



#bieu do 1
ggplot(aes(x='carat', y='price', color='clarity'), diamonds) + geom_point()
#bieu do 2
ggplot(aes(x='carat', y='price', shape='cut'), diamonds) + geom_point()

#geom_line
ggplot(mpg, aes(x ='displ', y= 'cty')) + geom_point() + geom_line()

#ggplot - stat_smooth
#pip install scikit-misc
meat['date'] = pd.to_datetime(meat['date'])
ggplot(meat, aes(x='date', y='beef')) + geom_point() + \
    stat_smooth(method='loess', span=0.4, color='blue', se=False)


#ggplot - stat_density
ggplot(diamonds, aes(x='price', color='clarity')) + stat_density()


#ggplot - scale_x_log
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine.data import diamonds
plt.figure(figsize=(10, 6))
sns.histplot(
    data=diamonds,
    x='price',
    bins=10,
    log_scale=(True, False),   # log trục x, y giữ count
    color='black',
    edgecolor='black'
)
plt.xlabel('price')
plt.ylabel('count')
plt.grid(True, alpha=0.3)
plt.show()

#ggplot - coord
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Phần dữ liệu xoắn ốc
n_points = 500
theta = np.linspace(0, 10 * np.pi, n_points)   # 5 vòng
r = 0.5 * theta                               # điều chỉnh hệ số nếu cần dày/mỏng hơn

# Vẽ polar plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Vẽ điểm xoắn ốc
ax.plot(theta, r, 'k.', markersize=3, alpha=0.8)  # điểm đen nhỏ

# Cài đặt các vòng tròn đồng tâm (rticks)
r_max = r.max()                      
rticks = np.arange(1, r_max + 1, 1)   


ax.set_rticks(rticks)

ax.set_rlabel_position(0)             # nhãn r ở vị trí 0°
ax.set_theta_zero_location('N')       # 0° ở trên
ax.set_theta_direction(-1)            # chiều ngược kim đồng hồ
# Nếu muốn chiều kim đồng hồ: ax.set_theta_direction(1) hoặc bỏ dòng này

ax.grid(True, color='gray', linestyle='-', alpha=0.5)

# ax.set_xticklabels([])

plt.show()
# end_main


# ggplot - facets
ggplot(diamonds, aes(x='price')) + \
geom_histogram() + \
    facet_grid("cut")


# ggplot - facets2
from plotnine import scale_x_continuous, facet_wrap, theme_minimal, ggplot, aes
import pandas as pd

chopsticks = pd.read_csv(r"C:\Users\DELL\Downloads\chopstick-effectiveness.csv", skipinitialspace=True)

(ggplot(chopsticks, aes(x='Chopstick.Length', 
                        y='Food.Pinching.Efficiency', 
                        group='Individual'))
+ geom_point()
+ geom_line(aes(group='~Individual'))
+ facet_wrap('~Individual')
+ scale_x_continuous(breaks=[150, 250, 350])
)  


# ggplot - facets3
ggplot(diamonds, aes(x="carat", y="price",
color="color", shape="cut")) + geom_point() + facet_wrap("clarity")


