from complex_calculator import add_rr, sub_rr,multi_rr


#v = "123.5345351∠-45"
#v = "123.5345351-j45"

# to identify if it is polar or rectangular
#if "∠" in v: # if returns True if statement will execute
    #print("You Entered Polar Coordinates")
#elif "j" in v: # if returns True the statement below will execute
    #print("You have Entered Rectangular Coordinates")


print(add_rr("1.9+j3.0001", "0+j0"))
print(sub_rr("1.9+j3.0001", "1.9+j3.0001"))
print(multi_rr("1+j1", "1+j1"))