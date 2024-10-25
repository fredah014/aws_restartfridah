#ask the user for a value and confirm the supplied value  is greater than 5
def checkvalue(valuetocheck):
    assert (type (valuetocheck )is int), "you must enter a number."
    assert(valuetocheck >5 ) , "value must must be greater than 0"

    if valuetocheck > 10:
       print ("value is greater than 10")
    else:
            print ("value is greater than 4")

var   = int(input("Enter a number greater than 5: "))
checkvalue(var)
