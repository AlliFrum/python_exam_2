from data import dataset
from task1 import *
from task3 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: якого товару на яку суму продано.

diagram = go.Pie(labels=list(res.keys()), values=list(res.values()))

plotly.offline.plot([diagram], filename='diag2.html')