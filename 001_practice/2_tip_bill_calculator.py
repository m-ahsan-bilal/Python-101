#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print(" Welcome to the Bill splitter Calculator! ")
print("----------------------------------")

 
bill = int(input("What was the total bill? \nRs."))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip = 1 + (tip_percentage /100)

bill_per_person = (bill / people) * tip
final_bill_per_person = round(bill_per_person,2)
final_bill_per_person = "{:.2f}".format(final_bill_per_person)

print("----------------------------------")
print("Each person should pay: Rs." + final_bill_per_person)
# print(f"Each person should pay: Rs.{final_bill_per_person}")
print("Thanks for using the Tip Calculator! Have a great day! ")