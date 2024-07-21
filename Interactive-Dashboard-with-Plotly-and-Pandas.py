import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Sales': [350, 430, 560, 590, 720],
    'Expenses': [220, 280, 390, 410, 520]
}
df = pd.DataFrame(data)

fig_line = px.line(df, x='Year', y=['Sales', 'Expenses'], title='Sales vs Expenses Over Years')
fig_line.update_layout(
    xaxis_title='Year',
    yaxis_title='Amount ($)',
    legend_title='Category'
)

fig_bar = px.bar(df, x='Year', y='Sales', title='Sales Over Years')
fig_bar.update_layout(
    xaxis_title='Year',
    yaxis_title='Sales ($)'
)

fig_pie = px.pie(df, values='Expenses', names='Year', title='Expenses Distribution')
fig_pie.update_traces(textposition='inside', textinfo='percent+label')

fig = make_subplots(rows=2, cols=2,
                    subplot_titles=['Sales vs Expenses', 'Sales Over Years', 'Expenses Distribution'])

fig.add_trace(fig_line.data[0], row=1, col=1)
fig.add_trace(fig_bar.data[0], row=1, col=2)
fig.add_trace(fig_pie.data[0], row=2, col=1)

fig.update_layout(height=600, width=800, title_text="Interactive Dashboard")

fig.show()


