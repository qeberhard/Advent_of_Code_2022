#Day two: Elf Rock Paper Scissors Score Guide
#   Data contains two columns of letters, first column is the opponent choice, second column is your choice.
#   A loss = +0, a win = +6, a tie = +3
#   You assume that:
#   Rock = X = 1, Paper = Y = 2, and Scissors = Z = 3

score = 0
choice_options = {"X":1, "Y":2, "Z":3}
options = {"Rock":"X", "Paper":"Y", "Scissors":"Z"}
op_choices = {"Rock":"A", "Paper":"B", "Scissors":"C"}
matches = {"A":"X", "B":"Y", "C":"Z"}
win = 6
loss = 0
tie = 3

with open("inputs/input_day_two.tsv", "r") as data:
    for line in data:
        op_choice, your_choice = line.strip().split(" ")

        #In event of a tie:
        if matches[op_choice] == your_choice:
            score = score + (choice_options[your_choice] + tie)

        elif op_choice == op_choices["Rock"]:
            #Then Paper would win
            if your_choice == options["Paper"]:
                score = score + (choice_options[your_choice] + win)
                
            #And Scissors would lose, the only remaining option
            else:
                score = score + (choice_options[your_choice] + loss)
        
        #If opponent does 
        elif op_choice == op_choices["Paper"]:
            if your_choice == options["Scissors"]:
                score = score + (choice_options[your_choice] + win)
                
            else:
                score = score + (choice_options[your_choice] + loss)
        
        elif op_choice == op_choices["Scissors"]:
            if your_choice ==  options["Rock"]:
                score = score + (choice_options[your_choice] + win)
                
            else:
                score = score + (choice_options[your_choice] + loss)
                

print("Following the original strategy guide, you would receive %s points" % score)

#   You are then told that:
#       X = try to lose, Y = try to tie, and Z = try to win.

score = 0
choice_options = {"A":1, "B":2, "C":3}
round_objective = {"X":0, "Y":3, "Z":6}
#How to lose:
loss_choices = {"A":"C", "B":"A", "C":"B"}
#How to win:
win_choices = {"A":"B", "B":"C", "C":"A"}

with open("inputs/input_day_two.tsv", "r") as data:
    for line in data:
        op_choice, your_objective = line.strip().split(" ")

        #In event of a tie:
        if your_objective == "Y":
            score = score + (choice_options[op_choice] + round_objective[your_objective])

        #
        elif your_objective == "X":
            score = score + (choice_options[loss_choices[op_choice]] + round_objective[your_objective])          
        
        else:
            score = score + (choice_options[win_choices[op_choice]] + round_objective[your_objective])
                

print("Following the updated strategy guide, you would receive %s points" % score)
