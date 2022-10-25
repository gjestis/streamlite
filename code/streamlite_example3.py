#Import the streamlit lib
import streamlit as st
import random
import matplotlib.pyplot as plt

#Layout
col1,col2,col3 = st.columns([1,1,1], gap="medium")



#%%
#COL1
col1.markdown("# Monte Carlo Simulation")
col1.markdown("Here is some info")




#%%
#COL 2
#Functions
def roll_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    if die_1 == die_2:
        same_num = True

    else:
        same_num = False

    return die_1, die_2, same_num
#Layout
col2.header(" Roll dices")

if col2.checkbox("Roll two dices"):
    die_1, die_2, same_num = roll_dice()
    if(same_num==True):
        col2.success("Success!")
        col2.text("Die 1 : {}.".format(die_1))
        col2.text("Die 2 : {}.".format(die_2))

    else:
        col2.error("Not success!")
        col2.text("Die 1 : {}.".format(die_1))
        col2.text("Die 2 : {}.".format(die_2))



#%%
#COL 3
#Functions

def bettin_montecarlo_sim(number_of_simulations,max_number_of_rolls,bet_per_roll,start_balance,odds_per_roll):
    num_simulations = number_of_simulations
    max_num_rolls = max_number_of_rolls
    bet = bet_per_roll
    win_probability = []
    end_balance = []
    fig = plt.figure()
    for i in range(num_simulations):
        balance = [start_balance]
        num_rolls = [0]
        num_wins = 0
        while num_rolls[-1] < max_num_rolls:
            same = roll_dice()
            if same:
                balance.append(balance[-1] + odds_per_roll * bet_per_roll)
                num_wins += 1
            else:
                balance.append(balance[-1] - bet_per_roll)
            num_rolls.append(num_rolls[-1] + 1)
        win_probability.append(num_wins / num_rolls[-1])
        end_balance.append(balance[-1])
        plt.plot(num_rolls, balance)
    plt.title("Monte Carlo Dice Game [" + str(num_simulations) + " simulations]")
    plt.xlabel("Roll Number")
    plt.ylabel("Balance [$]")
    plt.xlim([0, max_num_rolls])
    col3.pyplot(fig)


if col3.checkbox("Monte"):
    bettin_montecarlo_sim(100,100,2,100,0.2)


#%%
