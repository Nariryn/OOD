def staircase(n, cur_step=1):
    if n == 0:
        return "Not Draw!"

    elif cur_step > abs(n):
        return ''

    if n > 0:
        return f"{'_' * (n - cur_step)}{'#' * cur_step}{'\n' if cur_step != n else ''}{staircase(n, cur_step + 1)}"
    else:
        return f"{'_' * (cur_step - 1)}{'#' * (abs(n) - cur_step + 1)}{'\n' if cur_step != abs(n) else ''}{staircase(n, cur_step + 1)}"

n = int(input("Enter Input : "))
print(staircase(n))