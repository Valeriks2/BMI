print("Hello my friend")
weight=float(input("какой твой вес?"))
height=float(input("какой твой рост?"))

bmi = (weight // ((height / 100)*(height / 100)))
print("твой bmi " + str(bmi))
if bmi <=16:
    print("высокая масса тела")
if bmi >=16 and bmi <=18.5:
    print("присуствует лишний вес")
if bmi >=18.5 and bmi <=25:
    print("все нормально с весом ")