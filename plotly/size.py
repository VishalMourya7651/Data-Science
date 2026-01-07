import plotly.graph_objs as go

trace=go.Scatter(x=[23,24,32,26],y=[43,54,35,26],marker=dict(size=[40,50,60,70]),mode='markers')
fig=go.Figure(trace)
fig.show()