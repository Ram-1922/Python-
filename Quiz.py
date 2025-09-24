# Python Quiz game

questions = ("What is the capital of Australia?",
             "Which planet is known as the Red Planet?",
             "Who invented the light bulb?",
             "Which is the largest mammal in the world?",
             "In which year did India gain independence?",
             "Who wrote Romeo and Juliet?",
             "Which gas do plants absorb during photosynthesis?",
             "What is the currency of Japan?",
             "The chemical formula of water is:",
             "Which is the fastest land animal?")

question_num=0
options =((" a)Sydney\n b) Melbourne\n c) Canberra\n d) Perth\n e) Brisbane"),
          (" a) Venus\n b) Mars\n c) Jupiter\n d) Mercury\n e) Saturn"),
          (" a) Alexander Graham Bell\n b) Nikola Tesla\n c) Thomas Edison\n d) Albert Einstein\n e) James Watt"),
          (" a) Elephant\n b) Giraffe\n c) Blue Whale\n d) Whale Shark\n e) Hippopotamus"),
          (" a) 1942\n b) 1945\n c) 1947\n d) 1950\n e) 1962"),
          (" a) Charles Dickens\n b) William Shakespeare\n c) Jane Austen\n d) Mark Twain\n e) George Orwell"),
          (" a) Oxygen\n b) Carbon dioxide\n c) Nitrogen\n d) Hydrogen\n e) Methane"),
          (" a) Yuan\n b) Yen\n c) Won\n d) Dollar\n e) Peso"),
          (" a) H2O\n b) CO2\n c) O2\n d) CH4\n e) NaCl"),
          (" a) Lion\n b) Cheetah\n c) Horse\n d) Tiger\n e) Greyhound"))

answers=["C","B","C","C","C","B","B","B","A","B"]
score=0
for question in questions:
    print(question)
    print(options[question_num])
    guess = input("Enter the Correct option: ").upper()
    while True:    
        if guess not in ('A','B','C','D','E'):
            print("Invalid option!")
            guess = input("Enter the Correct option: ").upper()
        else:
            break
    if guess == answers[question_num]:
        score+=1
        print("Correct Answer😊")
    else:
        print("Wrong Answer 😔")
        print(f"Option {answers[question_num]} is the Correct Answer.")
    question_num+=1
print(f"The Score is {score} / 10")
