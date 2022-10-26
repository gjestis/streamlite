#Import packages
import random
import matplotlib.pyplot as plt
import streamlit as st

#Roll two dices function
def roll_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)

    if die_1 == die_2:
        same_num = True

    else:
        same_num = False
    return same_num

#Betting function two dices
def bettin_montecarlo_sim(number_of_simulations,max_number_of_rolls,bet_per_roll,start_balance,odds_per_roll):
    num_simulations = number_of_simulations
    max_num_rolls = max_number_of_rolls
    bet = bet_per_roll
    win_probability = []
    end_balance = []

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
    st.pyplot()

    overall_win_probability = sum(win_probability) / len(win_probability)
    overall_end_balance = sum(end_balance) / len(end_balance)
    return overall_win_probability, overall_end_balance
    #print("Average win probability after " + str(num_simulations) + "   runs: " + str(overall_win_probability))
    #print("Average ending balance after " + str(num_simulations) + " runs: $" + str(overall_end_balance))


