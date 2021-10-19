def check_even_in_list(my_list):
    even_list = []
    for item_name in my_list:
        if item_name % 2 == 0:
            even_list.append(item_name)
        else:
            pass
    return even_list

my_testlist = [20,3,5,18,9,2,3]
my_even_list = check_even_in_list(my_testlist)
print (my_even_list)

def employee_check(work_hours):
    curr_max = 0
    emp_name_max = ''

    for emp_name,emp_hours in work_hours:
        if emp_hours > curr_max:
            curr_max=emp_hours
            emp_name_max = emp_name

        else:
            pass
    #return (curr_max, emp_name_max)
    emp_of_the_month = [curr_max, emp_name_max]
    return emp_of_the_month


employee_list = [("Amit", 1800), ("Anand",1200), ("Pradeep", 3000)]
emp_of_the_month = employee_check(employee_list)
print (emp_of_the_month)



