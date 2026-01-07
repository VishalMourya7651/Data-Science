import plotly.graph_objs as go

x=[12,23,16,34]
y=[32,24,15,23]
trace=go.Scatter(x=x,y=y,mode='markers')
trace1=go.Scatter(x=x,y=y,mode='lines')
trace2=go.Scatter(x=x,y=y,mode='text')
fig=go.Figure(data=[trace,trace1,trace2])
fig.show()
