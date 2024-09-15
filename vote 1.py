name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    vote = input("You are eligible for vote.\nName of the candidate you want to vote for: ")
    print("Thank you, " + name)
    print("Your vote for " + vote + " has been recorded.")
else:
    print("Sorry, " + name + ", you are not eligible to vote.")
