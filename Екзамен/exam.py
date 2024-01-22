class MyClass:
    def my_method(self, additional_argument):
        print("Виклик методу з додатковим аргументом:", additional_argument)
        return True

my_instance = MyClass()
result = my_instance.my_method("Додатковий текст")
print("Результат методу:", result)
