import streamlit as st
import seaborn as sns
import math


st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")

st.title("This is my first Machine learning website")
st.text("Streamlit is cool, and it is simple to use")

st.header("This is my second header")
st.text("Streamlit is joke, MACHINE LEARNING IS EASY")

df = sns.load_dataset("iris")
st.write(df[['species','sepal_length','petal_length']].head(10))

st.subheader("Bar Chart")
st.bar_chart(df[['sepal_length','petal_length']])


st.subheader("Bar Chart of Sepal Length")
st.bar_chart(df['sepal_length'])

st.subheader("Line Chart of Sepal Length")
st.line_chart(df['sepal_length'])

st.subheader("Area Chart of Sepal and Petal Length")
st.area_chart(df[['sepal_length','petal_length']])

st.subheader("Table of Sepal and Petal Length")
st.table(df[['sepal_length','petal_length']])


sns.pairplot(df,hue = 'species',height = 3)
st.pyplot()


st.sidebar.header("This is my sidebar header")

st.subheader("Scatter Chart of Sepal and Petal Length")
st.scatter_chart(df[['sepal_length','petal_length']])

st.subheader("Dataframe of Sepal and Petal Length")
st.dataframe(df[['sepal_length','petal_length']])
st.dataframe(df[['sepal_length','petal_length']].describe())

st.subheader("JSON of Sepal and Petal Length")

st.json(df[['sepal_length','petal_length']].head(10).to_json())

st.subheader("Text")

st.text("This is my text")

st.subheader("Markdown")

st.markdown("This is my markdown")

st.subheader("LaTeX")

st.latex(r''' e^{i\pi} + 1 = 0 ''')

st.write("This is a regular text")

st.subheader("Code")

with st.echo():

    st.write("This is a code block")

st.subheader("Colorful Text and Error Text")

st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name not defined')")

st.subheader("Get Help Information")

st.help(range)

st.subheader("Slider")

st.slider("Select a range of values",0.0,100.0,(25.0,75.0))

st.subheader("SelectBox")

st.selectbox("Choose a option",["Option 1","Option 2","Option 3"])

st.subheader("MultiSelect")

st.multiselect("Choose a option",["Option 1","Option 2","Option 3"])

st.subheader("File Uploader")

st.file_uploader("Choose a CSV file",type = "csv")

st.subheader("Color Picker")


st.color_picker("Pick a color")

st.subheader("Date Input")

st.date_input("Pick a date")

st.subheader("Time Input")

st.time_input("Pick a time")

st.subheader("Display JSON")

st.subheader("Images")

st.image("https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg", width=700)

st.subheader("Videos")

st.video("https://youtu.be/M_cVyB0Z3sA?si=OiV2pyEghqHI0O8o")

st.subheader("Audio")

st.audio("https://pixabay.com/music/folk-celtic-irish-scottish-tin-whistle-background-music-10455/")

st.subheader("Checkbox")

if st.checkbox("Show/Hide"):

    st.text("Showing or Hiding Widget")

st.subheader("Radio Button")

status = st.radio("What is your status", ("Active","Inactive"))

if status == "Active":

    st.success("You are Active")

else:
    st.warning("Inactive, Activate")

st.subheader("SelectBox")

occupation = st.selectbox("Your Occupation", ["Programmer","Data Scientist","Doctor","Businessman"])

st.write("You selected this option", occupation)

st.subheader("MultiSelect")


location = st.multiselect("Where do you work?", ("London","New York","Accra","Kiev","Nepal"))

st.write("You selected", len(location), "locations")

st.subheader("Slider")

age = st.slider("What is your age?", 1, 100)

st.write("I'm ", age, "years old")

st.subheader("Button")

st.button("Simple Button")

st.subheader("Text Input")

name = st.text_input("Enter your name", "Type Here")

if st.button("Submit"):

    st.write("Hello", name)

else:
    st.write("Goodbye")

st.subheader("Number Input")

number = st.number_input("Enter a number")

st.write("The number is ", number)

st.subheader("Text Area")

message = st.text_area("Enter your message", "Type Here")

if st.button("Submit"):

    st.write(message)

else:

    st.write("Goodbye")

st.subheader("Date Input")

import datetime

today = st.date_input("Today is", datetime.datetime.now())

st.subheader("Time Input")

the_time = st.time_input("The time is", datetime.time())

st.subheader("Display JSON")

st.subheader("Display Raw Code")

st.subheader("Display Raw Code")

with st.echo():

    # This will also be shown

    st.write('This code will be printed')

st.subheader("Progress Bar")

import time

my_bar = st.progress(0)

for p in range(10):
    
        my_bar.progress(p + 1)

st.subheader("Spinner")

with st.spinner("Waiting .."):

    time.sleep(5)

st.success("Finished!")

st.subheader("Baloon")

st.balloons()

st.subheader("Sidebar")

st.sidebar.header("About")

st.sidebar.text("This is Streamlit Tut")

st.sidebar.header("My name is")

st.sidebar.text("Kofi")

st.sidebar.header("My age is")

st.sidebar.text("20")

st.sidebar.header("My country is")

st.sidebar.text("Ghana")

st.sidebar.header("My occupation is")

st.sidebar.text("Data Scientist")

st.sidebar.header("My favorite color is")

st.sidebar.text("Blue")

st.sidebar.header("My favorite programming language is")

st.sidebar.text("Python")

st.sidebar.header("My favorite food is")

st.sidebar.text("Fufu and Goat Light Soup")

st.sidebar.header("My favorite sport is")

st.sidebar.text("Football")

st.sidebar.header("My favorite team is")

st.sidebar.text("Chelsea")

st.sidebar.header("My favorite player is")

st.sidebar.text("Lionel Messi")





