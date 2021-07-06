print("Welcome to the tip calculator")
bill_amount = float(input("Enter the bill amount: "))
percentage = int(input("Enter the perecentage : (10,12 or 15"))
number_of_people = int(input("Enter the number of people: "))

#Calculate tip
tip_of_a_person = (bill_amount * percentage) / number_of_people 
bill_of_a_person = bill_amount/ number_of_people
total_bill_each_person_pay = tip_of_a_person + bill_of_a_person
print(f"Each person should pay ${total_bill_each_person_pay}")
