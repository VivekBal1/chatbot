def calculateValue(responses):
    print("Chatbot: sure, what you want to calculate? select anyone from this list (sum, subtract, multiplication, division)")
    math_operation = input("You: ")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    if math_operation in responses['math']:
        msg = ""
        if math_operation == "sum":
            msg = "Sum of a and b: ", a + b
            return msg
        elif math_operation == "subtract":
            msg = "Subtraction of a and b: ", a - b
            return msg
        elif math_operation == "division":
            msg = "Division of a and b: ", a / b
            return msg
        elif math_operation == "multiplication":
            msg = "Multiplication of a and b: ", a * b
            return msg
        return msg