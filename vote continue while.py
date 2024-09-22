print("Welcome to Digital Voting Machine")
bjp_votes = 0
congress_votes = 0
aap_votes = 0
tmc_votes = 0
nota_votes = 0
total_voters = 0

while total_voters < 20:
    print("\nVoter", total_voters + 1)
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 18:
        print("You are not eligible to vote.")
        continue
    else:
        print("Choose a party to vote:")
        print("1. BJP")
        print("2. Congress")
        print("3. AAP (Aam Aadmi Party)")
        print("4. TMC (Trinamool Congress)")
        print("5. NOTA (None of the Above)")

        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == "1":
            print("Your vote goes to BJP. Thank you!")
            bjp_votes += 1
        elif choice == "2":
            print("Your vote goes to Congress. Thank you!")
            congress_votes += 1
        elif choice == "3":
            print("Your vote goes to AAP. Thank you!")
            aap_votes += 1
        elif choice == "4":
            print("Your vote goes to TMC. Thank you!")
            tmc_votes += 1
        elif choice == "5":
            print("You chose NOTA. Thank you!")
            nota_votes += 1
        else:
            print("Invalid choice. Please select a valid option.")
            continue
        
        total_voters += 1

print("\nVoting has ended")
print("Total votes for BJP:", bjp_votes)
print("Total votes for Congress:", congress_votes)
print("Total votes for AAP:", aap_votes)
print("Total votes for TMC:", tmc_votes)
print("Total votes for NOTA:", nota_votes)

if bjp_votes > congress_votes and bjp_votes > aap_votes and bjp_votes > tmc_votes:
    print("BJP is the winner!")
elif congress_votes > bjp_votes and congress_votes > aap_votes and congress_votes > tmc_votes:
    print("Congress is the winner!")
elif aap_votes > bjp_votes and aap_votes > congress_votes and aap_votes > tmc_votes:
    print("AAP is the winner!")
elif tmc_votes > bjp_votes and tmc_votes > congress_votes and tmc_votes > aap_votes:
    print("TMC is the winner!")
elif nota_votes > bjp_votes and nota_votes > congress_votes and nota_votes > aap_votes and nota_votes > tmc_votes:
    print("NOTA received the most votes, indicating voters' discontent.")
else:
    print("It's a tie!")
