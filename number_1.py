import pathlib
def total_salary(path):
    salary = list()
    try:
        with open(path, 'r') as file:
            for line in file:
                salary.append(float(line.split(',')[1]))
    except FileNotFoundError:
        print('File not found')
        return None, None
    return sum(salary), sum(salary)/len(salary)
file_path = pathlib.Path(r'C:\Users\User\Desktop\projects\repos\dzModule4\salary.txt')
total, average = total_salary(file_path)  
print("total salary:", total)
print("average:", average)