#Import module
import streamlit as st

#Title,header and text
#Create Title
st.title("Hello GE - this is a title")

#Create header
st.header("This is a header")

#Create Subheader
st.subheader("This is a subheader")

#Text
st.text("This is some text")

#Markdown
st.markdown("### This is a markdown")
#%%
#Different signs

#Sucess
st.success("Success")

#Info
st.info("Information")

#Warning
st.warning("Warning")

#Error
st.error("Error")
#%%
#Writing

#Text with write
st.write("Text with write")

#Code with write
st.write(range(10))

#%%
#Images

#Using Pillow to open images
from PIL import Image
img = Image.open(r"C:\Users\jg\code\GE\streamlite\images\fish.jpg")

#Display image using streamlit, width is used to set the width of an image
st.image(img, width=300)

#%%
#Checkbox

if st.checkbox("Push this to show a message!"):
    st.text("The message!")


#%%
#Selection box

#The first argument takes the titleof the selectionbox
#Second argument takes options
hobby = st.selectbox("Hobbies :", ["Dancing", "Reading", "Traveling"])

#Print the selected hobby
st.write("Your hobby is :", hobby)

#Multi-Selectbox
politics = st.multiselect("Left or right?" ,["Left", "Inbetween", "Right"])

#Write the selected options
st.write("You selected :", len(politics), "options")
#%%
#Buttons

#Create a button
st.button("Random button")

#If button is pushed then show message
if(st.button("Push this button to see a message!")):
    st.text("The message!")

#%%
#Text Input

#Save the input text as a variable name
name = st.text_input("Enter your name:", "Type here ....")

#Display the name when the submit button is clicked
if(st.button("Submit")):
    result = name.title()
    st.success(result + " is submitted!")
#%%
#Slider

#Arg1: title of slider
#Arg2: Start of slider
#Arg3: End og slider
level = st.slider("Select the level",1,5)

#Print the level
st.text("Selected: {}".format(level))




#%%
