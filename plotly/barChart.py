import plotly.graph_objs as go

label=['cricket','football','Hockey','Basketball']
revenue=[400,700,200,600]
trace1=go.Bar(x=label,y=revenue,name='2023')
trace2=go.Bar(x=label,y=[200,350,100,900],name='2025')
layout=go.Layout(title='Sports revenue by year',xaxis_title='sports',yaxis_title='Revenue')
fig=go.Figure(data=[trace1,trace2],layout=layout)
fig.show()




