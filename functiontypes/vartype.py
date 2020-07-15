x=10
def val():
    global x
    x=50
    x=x+50
val()
print(x)