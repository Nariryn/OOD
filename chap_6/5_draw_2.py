def staircase(n, cur_step=1):
    if n == 0:
        return "Not Draw!"

    elif cur_step > abs(n):
        return ''

    if n > 0:
        return f"{'_' * (n - cur_step)}{'#' * cur_step}\n{staircase(n, cur_step + 1)}"
    else:
        return f"{'_' * (cur_step - 1)}{'#' * (abs(n) - cur_step + 1)}\n{staircase(n, cur_step + 1)}"

n = int(input("Enter Input : "))
print(staircase(n))