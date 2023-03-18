import pandas as pd
import plotly.express as px

"""
Para imprimir un DataFrame en Python separado por comas, puedes utilizar el método to_csv() del objeto DataFrame y especificar la separación de coma (,) como el separador de campo. Aquí hay un ejemplo de cómo hacerlo:

python
Copy code
import pandas as pd

# crear un DataFrame de ejemplo
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})

# imprimir DataFrame separado por comas
print(df.to_csv(index=False, sep=','))

"""
ecom_sales = pd.read_csv('Data.txt',sep = ',')
ecom_sales = ecom_sales.groupby(['Year-Month','Country'])['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

# Create the line graph
line_graph = px.line(
  # Set the appropriate DataFrame and title
  data_frame= ecom_sales, title='Total Sales by Country and Month', 
  # Set the x and y arguments
  x='Year-Month', y='Total Sales ($)',
  # Ensure a separate line per country
  color='Country')


import pandas as pd
import plotly.express as px
ecom_sales = pd.read_csv('Data.txt',sep = ',')
ecom_sales = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

# Create the bar graph object
bar_fig = px.bar(
  # Set the DataFrame, x and y
  data_frame=ecom_sales,x='Total Sales ($)', y='Country',
  # Set the graph to be horizontal
  orientation='h', title='Total Sales by Country')

# Increase the gap between bars
bar_fig.update_layout({'bargap': 0.5})

bar_fig.show()