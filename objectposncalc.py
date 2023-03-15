#ImprovedObjectPosCalcHW
print(" Welcome to this program, it will calculate an objects final position.")


#inital position
while (True):
    try:
        initial_position = float(input("Enter the object's initial position: "))
        if (initial_position < 0):
            print("Negative initial positions are not allowed.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid.")
    else:
        another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if (another_calculation != "y"):
        
        break
    
#velocity
while (True):
    try:
        initial_velocity = float(input("What is an objects initial velocity? "))
        if (initial_velocity < 0):
            print("Negative velocity positions are not allowed.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid.")
    else:
        another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if (another_calculation != "y"):
        
        break
#acceleration
while (True):
    try:
       initial_acceleration = float(input("What is the acceleration? "))
       if (initial_acceleration < 0):
            print("Negative accelerations are not allowed.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid.")
    else:
        another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if (another_calculation != "y"):
        
        break
#time
while (True):
    try:
       initial_time = float(input("What is the time in seconds? "))
       if (initial_time < 0):
            print("Negative time inputs are not allowed.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid.")
    else:
        another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if (another_calculation != "y"):
        
        break

#math
x_position = initial_position + initial_velocity * initial_time + 0.5 * initial_acceleration  * initial_time ** 2
 #output
print("Final Position =", x_position)

