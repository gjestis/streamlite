#Import the streamlit lib
import streamlit as st


#Tittel for app med header, markdown og eksempel
st.title("BMI - kalkulator")

st.header("BMI er en av flere målemetoder for å gi en indikasjon på om du er undervektig, normalvektig, overvektig, eller sykelig overvektig.")

st.markdown("### Slik regner du ut BMI")

st.write("""
        Verdens helseorganisasjon (WHO) har fastsatt grenseverdier for 
        kroppsmasseindeks hos voksne, disse er ment å forene hensyn til alle typer av sykdom som har 
        med vekt å gjøre og hensyn til individ og samfunn.
        Grenseverdiene benyttes også i helseovervåking.
        
        BMI er et uttrykk for vekt i forhold til høyde og er lik vekten delt på kvadratet av høyden :

""")

st.latex(r'''
    BMI = \frac{vekt}{hoyde^2}
    ''')

st.markdown("### Eksempel")

st.write("Per er 1.90 meter høy og veier 90 kg. BMIen til Per er:")

st.latex(r'''
    BMI = \frac{90}{(1.9)^2} = 24.93
    ''')
#%%
#BMI Kalkulator

#Legger inn markdown
st.markdown("### Kalkulator")

#Vekt som input i kgs
weight = st.number_input("Hvor mye veier du (i kg) ?", step=0.5)

#Høyde med en radio knapp
status = st.radio("Oppgi måleenhet for høyde:", ("cms", "meter", "feet"))

#Sjekker målenhet for status
if(status=="cms"):
    #Høyde i cm
    height = st.number_input("Hvor mange centimeter er du?")
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Skriv inn en verdi for høyde!")

elif(status=="meter"):
    #Høyde i meter
    height = st.number_input("Hvor mange meter er du?")
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Skriv inn en verdi for høyde!")

else:
    #Høyde i feat
    height = st.number_input("Hvor mange feet er du?")
    # 1 meter er 3.28 feet
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Skriv inn en verdi for høyde!")

#Sjekker om knappen er trykket
if(st.button("Finn din BMI")):
    #Printer BMI
    st.text("BMIen din er {}.".format(bmi))
    #Evaluerer BMIen
    if(bmi<18.4):
        st.error("Undervektig!")
        st.error("Sykdomsrisiko : Lav for diabetes, økt for andre helseproblemer")
    elif(bmi>=18.4 and bmi< 24.9):
        st.success("Normalvekt!")
        st.success("Sykdomsrisiko : Lav")
    elif(bmi>=24.9 and bmi < 29.9):
        st.warning("Overvektig!")
        st.warning("Sykdomsrisiko : Økt for diabetes")
    elif(bmi >= 29.9 and bmi < 34.9):
        st.warning("Fedme, grad 1")
        st.warning("Sykdomsrisiko : Økt for diabetes og økt dødelighet")
    elif(bmi>=34.9 and bmi < 39.9):
        st.warning("Fedme, grad 2")
        st.warning("Sykdomsrisiko : Høy risiko for flere helseproblemer og økt dødelighet")
    elif(bmi>=39.9):
        st.warning("Fedme, grad 3")
        st.warning("Sykdomsrisiko : Ytterligere økt helserisiko")




#%%
