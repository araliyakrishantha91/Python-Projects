print("welcome to tip calculator")
bill = float(input("enter the bill amount: $ "))
percentage = float(input("what percentage tip do you give? 10, 12, 15? "))
people = int(input("how many people share the bill? "))

tip = (percentage/100)*bill
total_bill = tip + bill
cost_per_person = round(total_bill , 2) / people
final_cost_per_person = round(cost_per_person, 2)
print(f"one person has to pay ${final_cost_per_person}")
