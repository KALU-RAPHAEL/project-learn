#Write a function that computes the running total of a list.
def calc_total(list):
    run_total = []
    current_sum = 0
    for n in list:
        current_sum += n
        run_total.append(current_sum)
    return run_total

num = [12, 24, 36, 48, 60, 72, 84, 96]
result = calc_total(num)
print(result)