import random
def getQuestion():
   questions = []
   with open('behave.txt', 'r',encoding='utf-8') as file:
      questions = [line for line in file]
   return questions

def ogPrompt(questions):
   increment = 0

   print(".........press anything to continue.........")
   print("...............input n to exit...............")
   while input() != "n":
      print(questions[increment])
      increment = increment + 1
      print("next -> ")
def writeAnswers(questions):
   increment = 0
   print(".........press anything to continue.........")
   print("...............input n to exit...............")
   while input() != "n":
      print(questions[increment])
      increment = increment + 1
      print("your input: ", input())
      print("next -> ")

if __name__ == "__main__":
   questions = getQuestion()
   random.shuffle(questions)
   writeAnswers(questions)