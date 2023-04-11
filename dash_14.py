import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from datetime import datetime, date
ecom_sales = pd.read_csv('Data.txt',sep = ',')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_sales['InvoiceDate'] = pd.to_datetime(ecom_sales['InvoiceDate'])

app = dash.Dash()

app.layout = html.Div([
  html.Img(src=logo_link, 
        style={'margin':'30px 0px 0px 0px' }),
  html.H1('Sales breakdowns'),
  html.Div(
    children=[
    html.Div(
        children=[
        html.H2('Controls'),
        html.Br(),
        html.H3('Sale Date Select'),
        dcc.DatePickerSingle(id='sale_date',
            min_date_allowed=ecom_sales['InvoiceDate'].min(),
            max_date_allowed=ecom_sales['InvoiceDate'].max(),
            initial_visible_month=date(2011,4,1),
            date=date(2011,4,11),
            style={'width':'200px', 'margin':'0 auto'})
        ],
        style={'width':'350px', 'height':'350px', 'display':'inline-block', 'vertical-align':'top', 'border':'1px solid black', 'padding':'20px'}),
    html.Div(children=[
            dcc.Graph(id='sales_cat'),
            html.H2('Daily Sales by Major Category', 
            style={ 'border':'2px solid black', 'width':'400px', 'margin':'0 auto'})
            ],
             style={'width':'700px','display':'inline-block'}
             ),
    ]),
    ], 
  style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
  )
# Create a callback and link
@app.callback(
    Output(component_id='sales_cat', component_property='figure'),
    Input(component_id='sale_date', component_property='date')
)
def update_plot(input_date):
    # Ensure the DataFrame is not overwritten
    sales = ecom_sales.copy(deep=True)
    
	# Conditionally filter the DataFrame using the input
    if input_date:
        sales = sales[sales['InvoiceDate'] == input_date]
        
    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
    bar_fig_major_cat = px.bar(
        title=f'Sales on: {input_date}',data_frame=ecom_bar_major_cat, orientation='h', 
        x='Total Sales ($)', y='Major Category')
	
    # Return the figure to render
    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)