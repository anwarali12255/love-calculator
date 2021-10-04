print('welcome to the LOVE CALCULATOR!')
name1=input('Whats your name?\n ')
name2=input('Whats their name?\n ')
x=name1.lower()
y=name2.lower()
name=x+y
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count('o')
v=name.count('v')
e=name.count('e')
total=t+r+u+e
total2=l+o+v+e
lovescore=int(str(total)+str(total2))
if lovescore<10 or lovescore>90:
  print(f"Your score is {lovescore}%, you go together like coke and mentos.")
elif lovescore>40 and lovescore<50:
    print (f"Your score is {lovescore}%, you are alright together.")
else:
  print(f"Your score is {lovescore}%")
