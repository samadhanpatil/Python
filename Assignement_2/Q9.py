9) Write program to display user's name and age and display
Hello <name>, you will turn <age+1> next year

def hello(name,age):
 print(f"Hello {name}, you will turn {age} next year")

if __name__=="__main__":
	name=input("Enter Name ")
	age=input("Enter age ")
	age1=int(age)+1
	hello(name,age1)
