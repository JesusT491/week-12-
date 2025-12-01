# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.


# Prints whether it’s cold, warm, or hot using comparison operators.



# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temperature_input = int(input("Hi, What is today's temperature?: "))
warning = "Extreme Temperature warning!"

#Temperature checker
if -10 <= temperature_input <= 30:
    print("temperature is cold!")
elif 30 <= temperature_input <= 60:
    print("Temperature is warm!")
elif 60 <= temperature_input <= 110:
    print("Temperature is hot today!")
else:
    print(warning)

