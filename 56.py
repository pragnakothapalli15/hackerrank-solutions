def evaluate_expression():
    # Read expression as a string
    var = input().strip()

    # Evaluate the expression using eval()
    eval(var)

if __name__ == "__main__":
    evaluate_expression()