import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from datetime import datetime, date
ecom_sales = pd.read_csv('Data.txt',sep = ',')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'

def make_break(num_breaks):
    br_list = [html.Br()] * num_breaks
    return br_list

def add_logo():
    corp_logo = html.Img(
        src=logo_link, 
        style={'margin':'20px 20px 5px 5px',
              'border':'1px dashed lightblue',
              'display':'inline-block'})
    return corp_logo

def style_c():
    layout_style={
        'display':'inline-block',
        'margin':'0 auto',
        'padding':'20px',
    }
    return layout_style

app = dash.Dash(__name__)

app.layout = html.Div([
  add_logo(),
  *make_break(2),
  html.H1('Sales Dashboard'),
  *make_break(3),
  html.Div(
    children=[
    html.Div(
        children=[
        html.H2('Controls', style=style_c()),
        html.H3('Set minimum OrderValue'),
        *make_break(2),
        dcc.Input(
          # Create the specified input
          id='min_order_val', type='range', 
          min=50, max=550, value=50,
          # Ensure the callback is triggered only when the user stops moving the slider
          debounce=False,
        style={'width':'300px', 'height':'30px'})
        ],
        style={'width':'350px', 'height':'350px', 'vertical-align':'top', 'border':'1px solid black',
        'display':'inline-block', 'margin':'0px 80px'}),
    html.Div(children=[
            dcc.Graph(id='sales_country'),
            html.H2('Sales Quantity by Country', 
            style={ 'border':'2px solid black', 'width':'400px', 'margin':'0 auto'})
            ],
             style={'width':'700px','display':'inline-block'}
             ),
    ])
    ], 
  style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
  )

@app.callback(
    Output(component_id='sales_country', component_property='figure'), 
    Input(component_id='min_order_val', component_property='value'))

def update_plot(input_val):
  
    if not input_val:
      input_val = 0
  
    sales = ecom_sales.copy(deep=True)

    # Check for input then use to subset data
    if input_val:
        input_val = round(float(input_val), 2)
        sales = sales[sales['OrderValue'] > input_val]
    
    fig = px.scatter(data_frame=sales, y='OrderValue', height=400,
                     x='Quantity', color='Country',
					 # Set the conditional title
                     title=f'Orders of Min Value ${input_val}')
    return fig
      
if __name__ == '__main__':
    app.run_server(debug=True)