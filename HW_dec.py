import datetime

def decorator(func):           #Decorator that return result of all interrior functions
    def record(args,**kwargs):      #Datatime part of code that return into decorator required data
        with open('1.txt', 'w', encoding = 'utf-8') as f:
            date = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
            result = func(*args, **kwargs)
            f.write(date)
            f.write(f'Имя: {func}, Аргументы: {args} , {kwargs}')
            f.write(f'Результат: {result}')
        return (result)
    return (record)

@decorator                          #Applying decorator
def calculate_salary():             #initial function
    print ('calculate salary')


