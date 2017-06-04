
import re

print("Our Magical Calculator")
print("Type 'quit' to exit")
print("Type 'clear' to clear(duh)\n")

previous = None
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == None:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("\nGoodbye, shizno")
        run = False

    elif equation == "clear":
        previous = None

    else:
        equation = re.sub('[^0-9\-\+/*]', '', equation)

        if previous == None:
            previous = eval(equation)
        else:
            equation = str(previous) + equation
            previous = eval(equation)

while run:
    performMath()
