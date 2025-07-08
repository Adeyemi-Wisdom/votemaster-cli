from itertools import count
from collections import Counter
vote_person= []
list_of_scores = []
c = Counter(list_of_scores)
def admin():
    print("Avoid wrong spelling of the contestant")
    contestant = input("Contestant name: ")
    vote_person.append(contestant)
    while True:
        continuation = input("Add the name of the next contestant and if no more, kindly press 'f' to start the voting session: ")
        vote_person.append(continuation)
        if continuation == "f":
            vote_person.pop()
            print("Names of the contestants successfully collected!")
            break
def voters():
    while True:
        print("These are the list of the contestants, Kindly input the serial number of your desire candidate and your vote wil be successfully recorded")
        for i, value in enumerate(vote_person):
            print(f"{i+1}. {value}")
        for i in vote_person:
            list_of_scores.append(0)
        while True:
            choice = int(input("Kindly Enter the serial number of your chosen candidate: "))
            if 1 <= choice <= len(vote_person):
                selected_option = vote_person[choice - 1]
                list_of_scores[choice - 1] += 1
                print(f"You have elected {selected_option}")
                break
            else:
                print("Error! Check your input properly")
                continue
        con = input("Another voter? Yes/No: ")
        if con == "no":
            winner_max = max(list_of_scores)
            winners = [vote_person[i] for i, score in enumerate(list_of_scores) if score == winner_max ]
            print("\nVoting Results:")
            for i, value in zip(vote_person, list_of_scores):
                print(f"{i}:{value}")
            if len(winners) == 1:
                print(f"The winner is : {winners[0]} 🥳")
            else:
                print("We have a tie! The winners are: ")
                for w in winners:
                    print(f"-{w}")
            break
        else:
            continue
print("You are welcome to Cognito's Tech automated voting app👆")
while True:
    user = input("Kindly input 'admin' to Setup the system by inserting names of the contestant: ")
    try:
        if user == "admin":
         admin()
         voters()
         break
    except ValueError:
        print("Error! Check your input please")