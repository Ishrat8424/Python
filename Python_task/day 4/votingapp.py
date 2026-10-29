# Voting app: Accept the number of voters. 
# For each voter, check that they are 18 or older, and skip those who aren't. '
# 'Let eligible voters choose among three candidates, and count invalid votes separately. '
# 'At the end, print each candidate's votes and declare the winner, or a tie. 


print("===== ONLINE VOTING SYSTEM =====")

candidate1 = 0
candidate2 = 0
candidate3 = 0
invalidVotes = 0
eligible = 0
notEligible = 0

n = int(input("Enter Number of Voters: "))

for i in range(1, n + 1):
    print("\n===== Voter", i, "=====")

    age = int(input("Enter Age: "))

    if age < 18:
        print("Not Eligible to Vote!")
        notEligible += 1
        continue

    eligible += 1

    print("\n===== CANDIDATE LIST =====")
    print("1. Rahul")
    print("2. Priya")
    print("3. Arjun")

    choice = int(input("Choose Candidate (1-3): "))

    if choice == 1:
        candidate1 += 1
        print("Vote Recorded Successfully!")

    elif choice == 2:
        candidate2 += 1
        print("Vote Recorded Successfully!")

    elif choice == 3:
        candidate3 += 1
        print("Vote Recorded Successfully!")

    else:
        invalidVotes += 1
        print("Invalid Vote!")

print("\n===== FINAL VOTING REPORT =====")

print("Total Voters:", n)
print("Eligible Voters:", eligible)
print("Not Eligible Voters:", notEligible)

print("\nRahul Votes:", candidate1)
print("Priya Votes:", candidate2)
print("Arjun Votes:", candidate3)
print("Invalid Votes:", invalidVotes)

print("\n===== ELECTION RESULT =====")

if candidate1==0 and candidate2==0 and candidate3==0:
    print("No Valid Votes! No Winner.")

elif candidate1>candidate2 and candidate1>candidate3:
    print("Winner: Rahul")

elif candidate2>candidate1 and candidate2>candidate3:
    print("Winner: Priya")

elif candidate3>candidate1 and candidate3>candidate2:
    print("Winner: Arjun")

elif candidate1==candidate2 and candidate1>candidate3:
    print("Tie Between Rahul and Priya")

elif candidate1==candidate3 and candidate1>candidate2:
    print("Tie Between Rahul and Arjun")

elif candidate2==candidate3 and candidate2>candidate1:
    print("Tie Between Priya and Arjun")

else:
    print("Tie Between All Three Candidates")

print("\n===== THANK YOU FOR VOTING =====")
