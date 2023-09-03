# Example file for Advanced Python: Language Features by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
#x = 5
#print(x)

# TODO: the assignment operator is part of an expression
#(x := 10)
#print(x)

# TODO: The assignment expression is useful for writing concise code
#while (thestr := input("value ? ")) != "exit":
#   print(thestr)

# TODO: The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    #"length": len(values),
    #Simplified with the method
    "length": (l := len(values)),
    #"total": sum(values),
    "total": (s := sum(values)),
    #"average": sum(values) / len(values)
    "average": s/l
}
pprint.pp(val_data)