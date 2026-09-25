""" bill = float(input("what's your bill "))
tip = int(input ("whats your tip "))
print(f"your total is {bill+tip}") """



""" sentence = input("gimme a sentence ")
word_count = len(sentence.split())
print ("there are ", word_count, "words") """



""" temp = float(input("whats da temp "))
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
 """



""" num = float(input("put in a num "))
if num % 2 == 1:
    print ('ts odd just like u')
elif num % 2 == 0:
    print ('ts even like the number of jobs u lost')
else:
    print ("wth how did u get this message") """



""" bill = float(input("how much did u get fatty - "))
service = input("how much u like da food so was it slappin, chillin, mid, or horrindus - ")
if service == "so good that i will tip 100%":
    print("we live to serve you")
elif service == "slappin":
    print("we recemond tipping 25% " )
elif service == "chillin":
    print("we recemond tipping 20%" )
elif service == "mid":
    print("we recemond tipping 10% cheap") 
elif service == "horrindus":
    print("we recemond tipping not tipping cause u broke af")
else:
    print("answer me peasant") """



number = int(input('gimme a num - '))

for i in range(1, number+1):
    if number%(i) == 0:
        print (i)

