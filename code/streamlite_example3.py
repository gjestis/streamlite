#Import the streamlit lib
import streamlit as st
import random
#Tittel for app med header, markdown og eksempel
st.title("Montecarlo Simulator")

st.header("sdsd")

st.markdown("### sdsd")

st.write("""
        sdsdsd :

""")

st.latex(r'''
    BMI = \frac{vekt}{hoyde^2}
    ''')

st.markdown("### Eksempel")

st.write("Per er 1.90 meter høy og veier 90 kg. BMIen til Per er:")

st.latex(r'''
    BMI = \frac{90}{(1.9)^2} = 24.93
    ''')
#Math
def roll_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)

    if die_1 == die_2:
        same_num = True

    else:
        same_num = False
    return die_1, die_2, same_num

die_1, die_2, same_num = roll_dice()

st.write("Die 1: ", die_1)
st.write("Die 2: ", die_2)
st.write("Same?")
if(same_num==True):
    st.success("Success")
elif(same_num==False):
    st.warning("Fail")

#%%
