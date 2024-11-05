import streamlit as st
import numpy as np 
import pandas as pd 
import time


if "counter" not in st.session_state:
   st.session_state.counter = 0

st.session_state.counter += 1
st.header(f"Tis page has run {st.session_state.counter} times.")
st.button("Run it again")

#df = np.random.randn(10, 20)

df = pd.DataFrame(
    np.random.randn(10, 20),
    #columns=('col' + str(i) for i in range(20))   
    columns=('col %d' % i for i in range(20))
)
st.dataframe(df.style.highlight_max(axis=0))
#st.table(df)



chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = (list('abc'))
)

st.dataframe(chart_data)
st.line_chart(chart_data)

st.text('display some map data')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], 
    columns=['lat', 'lon']
)

st.map(map_data)

# widgets (slider, button, select_box)
x = st.slider('x')
st.write(x, 'squared is', x * x)

#Widgets can also be accessed by key, 
#if you choose to specify a string to use as the unique key for the widget
st.text_input("Your name", key="name")
st.session_state.name

# checkbox
if st.checkbox('show dataframe'):
    chart_data

# select box
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })    
option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected:', option
st.text(option)

# layout
add_selectbox = st.sidebar.selectbox(
    'how would you like to be contacted?',
    ('email', 'home phone', 'Mobile phone')
)

# add a slider to the sidebar
add_slider = st.sidebar.slider(
    'Select a range of value', 
    0.0, 100.0, (25.0, 75.0)
)

# control layout
left_column, right_column = st.columns(2)
# use a column just like st.sidebar
left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  #latest_iteration.text(f'Iteration {i+1}')
  #ar.progress(i + 1)
  #time.sleep(0.1)
    pass

'...and now we\'re done!'

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

st.table(st.session_state.df)