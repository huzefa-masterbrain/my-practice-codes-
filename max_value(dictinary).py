def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    return (employee_of_month, current_max)

work_hours = [('John', 100), ('Doe', 200), ('Smith', 150)]  # Example work hours
print(employee_check(work_hours))

