import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.text("welcome to vgu")
st.text("welcome to dashboard")

st.header ("I'm sumit")
st.write("you can write",1-+5)

name=st.text_input("Enter your name: ")
age =st.number_input("Enter your age: ")
st.write("Enter your name",name, "Enter your age:",age)
st.selectbox("Enter your course: ",["BCA","B.TECH"])
if st.button("click"):
    st.success("click button")

file= st.file_uploader("upload file")
if file:
    content=file.read()
    st.write("file uploaded successfully")


data ={"Name":["jack","mack","joe","root"] ,"Marks":[10,20,30,40]}
df =pd.DataFrame(data)

st.dataframe(df)
data = pd.DataFrame({
    "marks":[10,20,30,40]
})

st.line_chart(data)
st.bar_chart(data)

subject=["python","java","c++","c"]
marks=[10,20,30,40]

fig, Ad=plt.subplots()
Ad.pie(marks,labels=subject)
st.pyplot(fig)




