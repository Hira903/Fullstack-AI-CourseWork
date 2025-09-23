#   Percentage of Correct Answers

# taking input from user
total_questions = int(input("Enter total number of questions:   "))
correct_answers = int(input("How many correct answers were there?  "))
 
# Calculating percentage of correct answers
percentage = (correct_answers/total_questions) * 100
print("Percentage of correct answers is: ", percentage, "%")