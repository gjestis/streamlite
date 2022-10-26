#Importing packages
import streamlit as st
import random
import numpy as np
import pandas as pd
import time

#Other
st.set_option('deprecation.showPyplotGlobalUse', False)

#Main page
st.set_page_config(layout="wide")

st.title("Monte Carlo Simulator")
st.subheader("Monte Carlo method using a dice game")

st.markdown("*Check out the [wikie page](https://en.wikipedia.org/wiki/Monte_Carlo_method) for more info about the method*")

st.write("""
        A game of dices where the player through two dices and win if they are the same and lose if they are not.
        The player has to place a bet for each roll, and the house need to offer an odds. One game can for instance
        contain 100 rolls where the player bets 1 dollar per roll and the house offers to double the money if the 
        dices are same.
        

""")



#Sidebare
st.sidebar.title("Control Panel")
st.sidebar.subheader("Place your bets")

#Take number of simulations
number_of_sim = st.sidebar.number_input(
    "Number of simulations",
    min_value=100,
    max_value=None,
    value=1000,
    step=100,
    help="The more simulations the higher the confidence in result",
)

#Take number of max rolls of dices per simulation
number_of_rolls = st.sidebar.number_input(
    "Number of rolls for each simulation",
    min_value=1,
    max_value=500,
    value=100,
    step=10
)

#Bet per roll
bet_per_roll = st.sidebar.number_input(
    "How much money is on the line for each roll",
    min_value=1,
    max_value=None,
    value=1,
    step=1
)

#Start balance
start_balance = st.sidebar.number_input(
    "How much money are you starting with ",
    min_value=1,
    max_value=None,
    value=100,
    step=10
)

#Betting odds per roll from house
odds_per_roll = st.sidebar.number_input(
    "Betting odds for each roll",
    min_value=1,
    max_value=None,
    value=10,
    step=1,
    help="What is the odds given to you from the house e.g 5-1, 10-1 etc."
)

#Simulation

#Create button for simulation with progress bar
if(st.sidebar.button("Simulate now")):
    my_bar = st.sidebar.progress(0)
    from functions_for_app import roll_dice, bettin_montecarlo_sim
    overall_win_probability, overall_end_balance = bettin_montecarlo_sim(number_of_sim,number_of_rolls,bet_per_roll,start_balance,odds_per_roll)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    st.sidebar.success("Simulation is done")
    st.text("Average win probability after " + str(number_of_sim) + " runs:" + str(overall_win_probability))
    st.text("Average ending balance after " + str(number_of_sim) + " runs:" + str(overall_end_balance))
