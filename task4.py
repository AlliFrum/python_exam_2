from data import dataset
from task1 import *
from task3 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки грошей витратив.

diagram = go.Bar(
    x=list(res.keys()),
    y=list(res.values())
)

fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='diagram.html')