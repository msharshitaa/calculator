def salary_calculator(array):
    salary_amount = 0
    working_hours = 0
    for iterator in range(len(array)):
        salary_amount += array[iterator] * 100
        working_hours += array[iterator]
        salary_amount += (array[iterator] > 8) * ((array[iterator] - 8) * 15)
        
        if iterator == 0:
            salary_amount += (array[iterator] > 0) * (array[iterator] * 100 // 2)

        if iterator == len(array) - 1:
            salary_amount += (array[iterator] > 0) * (array[iterator] * 100 // 4)

    salary_amount += (working_hours > 40) * ((working_hours - 40) * 25)
    return salary_amount
array=list(map(int,input().split()))
print(salary_calculator(array))

