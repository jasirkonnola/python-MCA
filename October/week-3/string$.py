string=input("enter a string")
first_string=string[0]
new_string=first_string+ string[1:].replace(first_string,'$')
print("new string:",new_string)
