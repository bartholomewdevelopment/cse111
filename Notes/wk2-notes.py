from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


first_name = 'Susan'
print_time('First name assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')




first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial + last_name_initial)


def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:  
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name,False)
last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial + last_name_initial)