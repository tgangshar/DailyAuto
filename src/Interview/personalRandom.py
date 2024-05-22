import random
import os
def getQuestion(sourcePath:str) -> list:
   if ".txt" not in sourcePath:
      sourcePath = sourcePath + ".txt"
   questions = []
   with open(sourcePath, 'r',encoding='utf-8') as file:
      questions = [line for line in file]

   with open("tmp.txt", 'r') as file:
      if not file.read(1):
         return questions
      pastQuestions = file.readlines()[-1]
      print(pastQuestions[0])
      if pastQuestions[0].isdigit():
         print("we have removed these questions:", pastQuestions)
         pastQuestions = list(map(int,pastQuestions.split(',')))
         increment = 0
         for i in pastQuestions:
            if increment > i:
               return questions
            questions.pop(i - increment)
            increment = increment + 1 
   return questions

def ogPrompt(questions:list) -> None:
   increment = 0

   print("...............input n to exit...............")
   print(".........press anything to continue.........")
   while input() != "n":
      print(questions[increment])
      increment = increment + 1
      print("next -> ")

#How does single functionality work? 
#Function: Ask questions
#But also: Stores answers
#Maybe have the while loop in another function? 
#For now Return answers
def questionGUI(questions:list) -> dict:
   answers = {}
   increment = 0

   print(".........press anything to continue.........")
   while (answer := input().lower()) != "exit":
      if increment == len(questions)/2:
            print("......HALF WAY THERE......")
      if answer == "now":
         print(increment, " out of ", len(questions))
      else:
         increment = increment + 1
         question = questions[increment].strip()
         print(question)
         answers[increment] = [question, input("Answer or STRIKE: ")]
      print("exit or now or next -> ")
   return answers

def answerTable(answers:dict) -> None:
   questionNumbers = []
   with open('tmp.txt', 'w') as file:
      file.writelines("|Questions|Answers|\n|...|...|\n")
      for value in answers.values():
         if value[1].upper() == "STRIKE":
            questionNumbers.append(value[0].split(".")[0])
         else:
            questionNumbers.append(value[0].split(".")[0])
            #table = ["|"] + [val for pair in zip(array, ["|"] * len(array)) for val in pair] + ["\n"]
            table = "|" + "|".join(value) + "|\n" 
            file.writelines(table)
      print(f"you answered questions:{','.join(questionNumbers)} out of {len(answers)}")
      file.write('\n' + ','.join(questionNumbers))
   
if __name__ == "__main__":
   os.system("dir *.txt")
   file = input("Choose file: ")

   questions = getQuestion(file)
   
   random.shuffle(questions)
   answers = questionGUI(questions)
   answerTable(answers)