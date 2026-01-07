import plotly.graph_objs as go

label=['cricket','football','Hockey','Basketball']
revenue=[400,700,200,600]
trace=go.Pie(labels=label,values=revenue,hole=0.5)
layout=go.Layout(title="Sports revenue")

fig=go.Figure(trace,layout=layout)
fig.show()