def newton_raphson(function, derivative, x, threshold, maxiter):
    """
    Given a function, its derivative, initial guess, threshold between two
    consecutive guesses and max number of iterations: finds the closest root
    to the initial guess

    returns the root found and the number of iterations to find root
    otherwise return None value if no roots are found

    """
    try:
        for i in range(maxiter):
            x_new = x - function(x) / derivative(x)
            if i == maxiter - 1:
                return None
            if abs(x_new - x) < threshold:
                break
            else:
                x = x_new

        return round(x_new, 3), i
    except OverflowError:
        print(
            """Error: Could not find root. Please check that your parameters
are correct and try again."""
        )


if __name__ == "__main__":
    # =============================================================================
    # y = lambda x: 2 * x**3 - 9.5 * x + 7.5
    # dy = lambda x: 6 * x**2 - 9.5
    #
    # =============================================================================

    y = lambda x: x**2 + 1
    dy = lambda x: 2 * x
    print(newton_raphson(y, dy, -10, 0.0001, 100))
