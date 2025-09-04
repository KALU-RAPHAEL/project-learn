#Write a function on_all that applies a function to every element of a list. Use it to print the fi rst twenty perfect squares. The perfect squares can be found by multiplying each natural number with itself. The first few perfect squares are 1*1=1, 2*2=4 etc. Twelve for example is not a perfect square because there is no natural number m so that m*m=12
def on_all(func, data_list):
    return [func(item) for item in data_list]

def square(x):
    return x * x

numbers = list(range(1, 21))
perfect_sqr = on_all(square, numbers)

print(f"The first twenty perfect squares are: {perfect_sqr}")