import datetime

wage = 100
bonus = 50 

def parametrized_decor(path):           #Parametrized decorator with file path
    def decorator(func):                #Decorator that return result of all interrior functions
        def record(args,**kwargs):      #Datatime part of code that return into decorator required data
            with open(path, 'w', encoding = 'utf-8') as f:
                date = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
                result = func(*args, **kwargs)
                f.write(date)
                f.write(f'Имя: {func}, Аргументы: {args} , {kwargs}')
                f.write(f'Результат: {result}')
            return (result)
        return (record)

@parametrized_decor(path = 'logs/1.txt')       #Applying decorator
def calculate_salary(wage, bonus):             #initial function
    salary = wage + bonus
    print (f'Зарплата составляет {salary} условных единиц')



