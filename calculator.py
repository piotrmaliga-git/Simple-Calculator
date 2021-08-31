class Calculator:   
    def __init__(self, number_1,number_2):
        
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        return self.number_1 + self.number_2

    def subtract(self):
        return self.number_1 - self.number_2
    
    def multiply(self):
        return self.number_1 * self.number_2
    
    def divide(self):
        return self.number_1 / self.number_2
    
    def decision(self, user_decision):
        if user_decision == "+":
            return self.add()
        elif user_decision == "-":
            return self.subtract()
        elif user_decision == "*":
            return self.multiply()
        elif user_decision == "/":
            return self.divide()


def main(): 
    while True:
        user_input = input("Please type in your calculation: ")
        user_input = user_input.strip().split(" ")

        user_number_1 = int(user_input[0])
        user_number_2 = int(user_input[2])
        decision = user_input[1]

        calc = Calculator(user_number_1,user_number_2)
        result = calc.decision(decision)
        print(result)

        futher_calculation = input("Do you want to make any further calculations? [y/n]?: ")
        
        if futher_calculation.lower()[0] == "y":
            continue
        else:
            break

main()