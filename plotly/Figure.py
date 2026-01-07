import plotly.graph_objs as go

trace = go.Scatter(
    x=[12,23,16,34],
    y=[32,24,15,23],
    mode='lines'
)

fig = go.Figure(data=[trace],layout=go.Layout(title="HELLO"))
fig.show()
