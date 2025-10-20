#Alaysha Gupta
#buliding a daily calorie tracker console app

print("Welcome to calorie tracking console app \nThis tool will help you track your total calorie")
meals_name=[]
calorie_amount=[]
num_meal=int(input("How many meals you want to take today?"))
#get meal name
for i in range(num_meal):
    meal_name=input(f"meal {i+1} of {num_meal}")

    meals_name.append(meal_name)
#get calorie intake
    calorie_input=int(input(f"enter calorie for {meal_name}"))
    calorie_amount.append(calorie_input)

    print("meal names entered:",meals_name)
print("calorie amount entered:",calorie_amount)

#calorie calculation

total_calorie=sum(calorie_amount)
if len(calorie_amount)>0:
    average_calories=total_calorie/len(calorie_amount)
else:
    average_calories=0.0

print(f"Total Calories Consumed: {total_calorie}")
print(f"Average Calorie Per Meal: {average_calories}")

#limit warning

limit_input=int(input("Enter daily calorie limit"))
if (total_calorie>limit_input):
    exceed_calorie=total_calorie-limit_input

    print(f"you have taken{exceed_calorie} extra calorie")
elif(total_calorie==limit_input):
    print("you have hit your dainy calorie limit exactly")
else:
    print(f"you have taken{total_calorie} total calorie")

#print data in table


   
header=(f"{meals_name},{calorie_amount}")
print(header)
print("-"*30)
zip(meals_name,calorie_amount)
print(f"{meals_name},{calorie_amount}")
print(f"Total \t \t\t{total_calorie}")
print(f"Average calories \t {average_calories}")
print(f"Daily limit \t\t {limit_input}")


print("Thank you for using the daily calorie tracker")
