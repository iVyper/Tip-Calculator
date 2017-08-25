# Welcome users to the tip calculator.
print("Welcome to the tip calculator!")

# Ask the user for the bill's total and input it into the bill_total variable.
bill_total = float(input("What was the total bill? $"))

# Ask the user how much of a tip percentage they would like to leave and put it into the tip_percentage variable.
# Remember that percentages are just an amount out of 100, so we will divide the input by 100.
# Example: 20% tip is 0.20 * the bill's amount.
tip_percentage = int(input("How much percent of a tip would you like to give? 15, 18, or 20? ")) / 100

# Ask the user how many people are splitting the bill and put it into the num_people_to_split variable.
num_people_to_split = int(input("How many people are splitting the bill? "))

# Calculate the amount to be split and put it into the split_total variable.
# Total amount would be the bill's total plus the tip percentage which is the bill's total times the percentage.
# The split amount would be the total after tip divided by the number of people the bill is being split by.
split_total = (bill_total + (bill_total * tip_percentage)) / num_people_to_split

# Print out the amount each person should pay.
# We want to make sure the amount is calculated to 2 decimal places due to currency.
print(f"Each person should pay: ${round(split_total, 2)}")
