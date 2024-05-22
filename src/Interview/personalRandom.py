import random
import os
def getQuestion(file:str) -> list:
   if ".txt" not in file:
      file = file + ".txt"
   questions = []
   with open(file, 'r',encoding='utf-8') as file:
      questions = [line for line in file]
   return questions

def ogPrompt(questions) -> None:
   increment = 0

   print("...............input n to exit...............")
   print(".........press anything to continue.........")
   while input() != "n":
      print(questions[increment])
      increment = increment + 1
      print("next -> ")
def writeAnswers(questions) -> None:
   answers = {}
   increment = 0

   print(".........press anything to continue.........")

   while (answer := input().lower()) != "exit":
      if increment == len(questions)/2:
            print("......HALF WAY THERE......")
      if answer == "now":
         print(increment, " out of ", len(questions))
         print("Repeating Question now")
      else:
         increment = increment + 1
         question = questions[increment].strip() + ": "
         print(question)
         answers[increment] = [question, input("Answer: ")]
      print("exit or now or next -> ")
      
   with open('tmp.txt', 'w') as file:
      file.writelines("|Questions|Answers|\n|...|...|\n")
      for key in answers:
         array = answers[key]
         table = ["|"] + [val for pair in zip(array, ["|"] * len(array)) for val in pair]
         file.writelines(table)
         file.write("\n")
         print(table)

if __name__ == "__main__":
   os.system("dir *.txt")
   file = input("Choose file: ")
   questions = getQuestion(file)
   random.shuffle(questions)

   writeAnswers(questions)