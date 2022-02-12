import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

# Define the initial figure
df = px.data.iris()
initial_figure = px.scatter(
    df, x="sepal_length", y="sepal_width", height=350,
    color="species", title="Playing with Fonts")
initial_figure.update_layout(
    font_family="Courier New",
    title_font_family="Times New Roman")

picker_style = {'float': 'left', 'margin': 'auto'}

# Build the app
app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Graph(id="bar-chart", figure=initial_figure),
    daq.ColorPicker(
        id='font', label='Font Color', size=150,
        style=picker_style, value=dict(hex='#119DFF')),
    daq.ColorPicker(
        id='title', label='Title Color', size=150,
        style=picker_style, value=dict(hex='#2A0203')),
])

@app.callback(
    Output("bar-chart", 'figure'), 
    [Input("font", 'value'),
     Input("title", 'value')],
    [State('bar-chart', 'figure')])
def update_bar_chart(font_color, title_color, fig_json):
    # Reconstruct the figure using the JSON specifications
    fig = go.Figure(fig_json)
    fig.update_layout(
        font_color=font_color['hex'],
        title_font_color=title_color['hex'])

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
