# Programmers:
# Course:  CS151, Zelalem Yalew
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement:
# Data In:
# Data Out:
# Credits:

#initial print prompt explaining program to user
print("Hello! This program will calculate the future population of the US after X amount of years.\nFor this program, "
      "you must enter the seconds between birth, seconds between death, seconds between immigration,"
      "the current population,\nand the number of years in the future you would like to calculate for.")

#seconds per year is a constant
seconds_per_year=31536000

#promts for the user to input information
seconds_between_birth=float(input("What are the seconds between birth?:"))
seconds_between_death=float(input("What are the seconds between death?:"))
seconds_between_immigration=float(input("What are the seconds between immigration?:"))
current_population=float(input("What is the current population?:"))
years_in_future=float(input("What is the number of years in future?:"))

#calculation for population change
population_change = (seconds_per_year/seconds_between_birth + seconds_per_year/seconds_between_immigration - seconds_per_year/seconds_between_death)*years_in_future


#calculation for future population
future_population=int(current_population+population_change)

#print statement for stating what future population will be
print("The U.S. population in ", years_in_future, "years will be:",future_population,)

#if statements for stating if population increased or decreased
if future_population > current_population:
    print("The total population has increased.")
else:
    print("The total population has decreased.")




