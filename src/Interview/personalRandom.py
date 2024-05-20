import random
import os
def getQuestion(file:str):
   if ".txt" not in file:
      file = file + ".txt"
   questions = []
   with open(file, 'r',encoding='utf-8') as file:
      questions = [line for line in file]
   return questions

def ogPrompt(questions):
   increment = 0

   print("...............input n to exit...............")
   print(".........press anything to continue.........")
   while input() != "n":
      print(questions[increment])
      increment = increment + 1
      print("next -> ")
def writeAnswers(questions):
   answers = {}
   increment = 0

   print(".........press anything to continue.........")
   while input() != "exit":
      if increment == 50:
         print("......HALF WAY THERE......")
      question = questions[increment].strip() + ": "
      print(question)
      answers[increment] = [question, input("Answer: ")]
      print("exit or next -> ")

      increment = increment + 1
   with open('tmp.txt', 'w') as file:
      for key in answers:
         file.writelines(answers[key])
         file.write("\n")

if __name__ == "__main__":
   os.system("dir *.txt")
   file = input("Choose file: ")
   questions = getQuestion(file)
   random.shuffle(questions)
   writeAnswers(questions)