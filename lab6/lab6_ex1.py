# Загальні ймовірності
P_Yes = 10/14  # Ймовірність "Yes"
P_No = 4/14   # Ймовірність "No"

# Умовні ймовірності для кожного атрибута
P_Sunny_Yes = 3/10  # Ймовірність "Sunny" за "Yes"
P_Sunny_No = 2/4   # Ймовірність "Sunny" за "No"

P_Normal_Yes = 6/9  # Ймовірність "Normal" за "Yes"
P_Normal_No = 1/5   # Ймовірність "Normal" за "No"

P_Strong_Yes = 3/9  # Ймовірність "Strong Wind" за "Yes"
P_Strong_No = 3/5   # Ймовірність "Strong Wind" за "No"

# Розрахунок P(Yes) і P(No) для заданих умов
P_Yes_given_conditions = P_Sunny_Yes * P_Normal_Yes * P_Strong_Yes * P_Yes
P_No_given_conditions = P_Sunny_No * P_Normal_No * P_Strong_No * P_No

# Нормалізація (знаменник формули Байєса)
normalizing_factor = P_Yes_given_conditions + P_No_given_conditions

# Ймовірності "Yes" і "No" після нормалізації
P_Yes_final = P_Yes_given_conditions / normalizing_factor
P_No_final = P_No_given_conditions / normalizing_factor

print(f"Ймовірність Yes: {P_Yes_final:.2%}")
print(f"Ймовірність No: {P_No_final:.2%}")
