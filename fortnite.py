from fractions import Fraction
import math
import sys

def start():
  global mode
  mode = int(input("""
 _____        _                            _                    
/__   \ _ __ (_)  __ _         ___   ___  | |__   __  ___  _ __ 
  / /\/| '__|| | / _` | _____ / __| / _ \ | |\ \ / / / _ \| '__|
 / /   | |   | || (_| ||_____|\__ \| (_) || | \ V / |  __/| |   
 \/    |_|   |_| \__, |       |___/ \___/ |_|  \_/   \___||_|   
                 |___/\n                                          
Enter 1 for trig ratio calculator. . . \nEnter 2 for quadrant solver. . . \nEnter 3 to exit. . . """))

start()

def trigCalc():
  counter = 0
  problemCount = int(input("Enter the amount of coordinate pairs you want to find trig ratios for: "))
  problemSet = [[] for i in range(problemCount)]

  for i in problemSet:
    x = abs(int(input("Enter X value for first pair: ")))
    y = abs(int(input("Enter Y value for first pair: ")))
    problemSet[counter].append(x)
    problemSet[counter].append(y)
    r = int(math.sqrt(x ** 2 + y ** 2))
    
    sin = Fraction(y, r)
    cos = Fraction(x, r)
    
    if(x != 0):
      sec = Fraction(r, x)
      tan = Fraction(y, x)
    else:
      print("Cannot display secant and tangent because of division by 0 occured. . .")
      sec = None
      tan = None
      pass
    
    if(y != 0):
      csc = Fraction(r, y)
      cot = Fraction(x, y)
    else:
      print("Cannot display cosecant and cotangent because of division by 0 occured. . .")
      csc = None
      cot = None
    
    def trigAnswers():
      print(f"Ratios for problem set {counter + 1}: \n")
      print(sin)
      print(cos)
      print(tan)
      print(csc)
      print(sec)
      print(cot)
      print("\n\n")
      if(counter != problemCount):
        print("NEXT PROBLEM SET\n\n")
        #print ("\033[A                             \033[A")

      else:
        print("Back to main menu!")
    trigAnswers()
    counter += 1
    if(counter == problemCount):
      start()
      main()

def quadSolver():
  balls = "balls"
  print(balls)
  quadrant = int(input("Enter specified quadrant: "))
  num_dom = []
  ratio = input("Enter any pair for numer and denom X, Y, R\n(seperate with proper spacing and comma): ").lower()
  """x, y"""
  numerator = ratio[:1]
  denominator = ratio[-1:]
  
  if(numerator == "r" or denominator == "r"):
    if(quadrant == 1):
      answer = "pos"
    if(quadrant == 2):
      if(numerator == "x" or demoninator == "x"):
        answer = "neg"
      else:
        answer = "pos"
    if(quadrant == 3):
      answer = "neg"
    if(quadrant == 4):
      if(numerator == "y" or demoninator == "y"):
        answer = "neg"
      else:
        answer = "pos"
  else:
    if(quadrant == 1):
      answer = "pos"
    if(quadrant == 2):
      answer = "neg"
    if(quadrant == 3):
      answer = "pos"
    if(quadrant == 4):
      answer = "neg"
  print(f"\n\nThe ratio is {answer}!\n\n")
  start()
  main()
    
    
def main():
  if(mode == 1):
    trigCalc()
  elif(mode == 2):
    quadSolver()
  else:
    sys.exit()
    

main()
