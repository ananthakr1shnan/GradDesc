x = [60, 63, 65, 70, 70, 70, 80, 90, 80, 80,85, 89, 90, 90, 90, 90, 94, 100, 100, 100]
y = [1, 0, 1, 2, 5, 1, 4, 6, 2, 3, 5, 4, 6, 8, 4, 5, 7, 9, 7, 6]

def gradient_descent(x, y, learning_rate):
    m = len(x)
    theta0 = sum(y) / len(y)  
    theta1 = (max(y) - min(y)) / (max(x) - min(x))  
    for i in range(3000000):
        predictions = [theta0 + theta1 * X for X in x]
        errors = [pred - Y for pred, Y in zip(predictions, y)]
        
        theta0_gradient = (1 / m) * sum(errors)
        theta1_gradient = (1 / m) * sum(error * X for error, X in zip(errors, x))
        
        theta0 -= learning_rate * theta0_gradient
        theta1 -= learning_rate * theta1_gradient

    return theta0, theta1

theta0, theta1 = gradient_descent(x, y, 0.0001)

print("Theta0 (Intercept):", theta0)
print("Theta1 (Slope):", theta1)

x1=97
predicted_y = theta0 + theta1 * x1

print("Prediction for x =", x1, "is:", predicted_y)