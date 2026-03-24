def ft_recursion(harvest_time, n):
    if n <= harvest_time:
        print(f"Day {n}")
        ft_recursion(harvest_time, n + 1)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive():
    harvest_time = int(input("Days until harvest: "))
    ft_recursion(harvest_time, 1)
