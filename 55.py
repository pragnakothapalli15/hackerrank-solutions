def evaluate_polynomial():
    # Read x and k values
    x, k = map(int, input().split())

    # Read polynomial expression
    poly_expr = input().strip()

    # Replace 'x' with 'x' value and evaluate the expression
    result = eval(poly_expr.replace('x', str(x)))

    # Check if result equals k
    print(result == k)

if __name__ == "__main__":
    evaluate_polynomial()