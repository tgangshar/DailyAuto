import random
import os
def getQuestion(file:str):
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
   increment = 0
   print("...............input n to exit...............")
   print(".........press anything to continue.........")
   while input() != "n":
      if increment == 50:
         print("......HALF WAY THERE......")
      print(questions[increment])
      increment = increment + 1
      print("your input: ", input())
      print("next -> ")

if __name__ == "__main__":
   os.system("dir *.txt")
   file = input("Choose file: ")
   questions = getQuestion(file)
   random.shuffle(questions)
   writeAnswers(questions)