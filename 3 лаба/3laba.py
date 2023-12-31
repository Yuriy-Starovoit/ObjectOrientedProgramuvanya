import random
import string
class MyName:
    total_names = 0 

    def __init__(self, name=None) -> None:
        self.name = name if name is not None else "Anonymous"  
        MyName.total_names += 1  
        self.my_id = self.total_names

    @property
    def whoami(self):
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name.lower()}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Class method
        """
        return cls("Anonymous")  

    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"
    
    def crpass(le= 8):
        """Створення паролю, унікального для кожної людини
        """
        characters = string.ascii_letters + string.digits + string.punctuation #бібліотека string дає можливість вибрати рандомний символ
        return ''.join(random.choice(characters) for _ in range(le))



print("Let's Start!") 
#names = ("Bohdan", "Marta", None) 
#all_names = {name: MyName(name) for name in names} 
#
#for name, me in all_names.items(): 
#    print(f"""{">*<"*20} 
#This is object: {me}  
#This is object attribute: {me.name} / {me.my_id} 
#This is {type(MyName.whoami)}: {me.whoami} / {me.my_email} 
#This is {type(me.create_email)} call: {me.create_email()} 
#This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
#This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names} 
#{"<*>"*20}""") 
#
#print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?") 
#
#### Індивідуальні завдання
custom_message = "Greetings to all!"
print(MyName.say_hello(custom_message)) 

anon_user = MyName.anonymous_user()
print(anon_user.whoami) 
print(anon_user.my_email)  
