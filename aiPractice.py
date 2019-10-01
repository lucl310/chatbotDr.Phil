import random

# PROJECT head in a jar, dr phil
# iteration 3
# 8/28/19 Luc Lambert

# CREATE PROGRAM THAT, WHEN RUN, GREETS THE USER IN THE VOICE OF YOUR SELECTED HISTORICAL FIGURE

print('Thank you very much for coming on the show. ')
print( 'Oh boy. Hello, and welcome to the dr phil show. My name is dr. phil, and today we have the case of a troubled young child,'
      ' trying to talk, to a computer')

q1 = input('how are you doing today?')
answerI = ['i', 'I']
response1 = ['good', 'fine', 'ok', 'nice', 'well', 'great', 'okay']

if q1[0] in answerI:
      print("you are " +q1[4:]+'? ok')
else:
      print(q1 + "? ok")
if q1[2:6] in response1:
      print()
else:
      print('well, I hope we can change that today')

q2 = input('So, can you explain to me why you are talking to, to... a computer?')
# checks if user is possibly teacher
answer2 = ['required', 'grading', 'summative', 'formative', "don't"]
answer3 = ['enjoy', 'want']

if q2[4:12] or q2[4:11] or q2[3:11] or q2[3:10] in answer2:
      answer2_1 = ['yes', 'Yes', 'am']
      answer2_1_1 = ['no', 'not']

      q2_1 = input('What is your job, what do you do? Are you a teacher?')

      if q2_1[4:7] in answer2_1_1:
            q2_2 = ("Ok, so are you currently, uh, grading this assignment?")
            if q2_2 == "yes"or"Yes":
                  print("well, this student, he's worked very hard on this, so please give him a good grade")
                # shamelessly begs for a better grade
      else:
            relative = ["cousin", "nephew", "neice", "uncle", "aunt", "great grandmother", "great great great grand uncle", "godfather"]
            injury = ["a broken ankle", "fired for a DUI", "killed by a stray Badger", "pestered by a swarm of angry Wasps", "mauled by an angry Aardvark", "injured by a falling Armadillo"]
            input("so what do you do then?")
            # makes a hopefully funny line
            print('Oh really? my ' + relative[random.randint(0, 7)] + ' used to do that, but he got ' + injury[random.randint(0,5)] + " so they had to quit")
else:
      print('Are you delusional? Do you suffer from mental illness?')
q3 = input("anyways, do you enjoy your work?")
answer3 = ['yes', 'yeah', 'i do', 'yep']
if q3 in answer3:
      print("Then why, why are you trying to talk to computers, instead of working?")
      print("I think that I have a solution that can help you. I want you to go to this place called the ranch. It's a nice place, and it provides a break from society that people like you may find useful")
else:
      print("Well then, I can see why you spend your time talking to computers")
      print("I think that I have a solution that can help you. I want you to go to this place called the ranch. It's a nice place, and it provides a break from society that people like you may find useful"
            "")
      input("Is there anything else you would like to say before you are sent away?")