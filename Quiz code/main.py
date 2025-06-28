import json

add = input("Add questions y/n ").lower()

if add == "y":
    with open("question.json", "r") as file:
        Quiz_question = file.read()

    # Load the JSON data from the string
    data = json.loads(Quiz_question)

    new_question = input("Enter the new question")

    options = {}
    options["a"] = input("Enter option a: ")
    options["b"] = input("Enter option b: ")
    options["c"] = input("Enter option c: ")
    options["d"] = input("Enter option d: ")

    while True:
        correct_answer = input("Enter  the correct answer: a,b,c,d ").lower()
        if correct_answer in ["a", "b", "c", "d"]:
            break
        else:
            print("")
            print("lets try that again")

    question_dict = {
        "question": new_question,
        "options": options,
        "correct_answer": correct_answer
    }
    # we created a dict

    data.append(question_dict)

    with open("question.json", "w") as file:
        json.dump(data, file, indent=4)

    for question in data:
        print(question['question'])  # " question" refres to the q in json
    print("Updated sucessufully")

else:
    with open("question.json", "r") as file:
        Quiz_question = file.read()
data = json.loads(Quiz_question)


print("These are the questions")

for question in data:
    print(question['question'])

question_count = len(data)

print("")
print("there are ", question_count, "Questions")
print("")



loop_counter = 0

answers = {}

while loop_counter != question_count:

    print("Enter the answer to Q" , loop_counter)
    answers[loop_counter] = input("Answer = ").lower()
    loop_counter += 1
    print("")
    # sotres the user answers # works fine use a for loop to compare

score = 0
for i in range(question_count):
    correcct_ans = ans['correct_answer']
    print(correcct_ans)
    if answers[i] == correcct_ans:
        score += 1

#gets the corrtect answer from the json
#only saves one overwritten
print("score")