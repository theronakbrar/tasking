import random

taskingName = str(input("Enter the name of the tasking: "))
taskingDate = str(input("Enter the date of the tasking: "))
num = int(input("Enter the number of taskees: "))
cYear = int(input("Enter the class year (0 if all accepted): "))
with open("cadets.txt") as f: 
    data = f.readlines() #string element in a list
    pool = [[]]
    for each in data:
        x = each.split(":")
        y = x[0].split(" CDT ")
        name = y[0]
        year = int(y[1][:4])
        occurances = int(x[1])
        for i in range(occurances):
            pool.append([name,year])
    with open('tasking.txt', 'a') as fl:
        while num != 0:
            if cYear == 0:
                cadet = random.choice(pool)
                fl.write(taskingName+" on "+ taskingDate +": "+cadet[0]+"' "+ str(cadet[1])+"\n")
                pool.remove(cadet)
                print(taskingName+" on "+ taskingDate +": "+cadet[0]+"' "+ str(cadet[1])+"\n")
            else:
                cadet = random.choice(pool)
                if cadet[1] == cYear:
                    fl.write(taskingName+" on "+ taskingDate +": " + cadet[0]+"' "+ str(cadet[1])+"\n")
                    pool.remove(cadet)
                    #print(taskingName+" on "+ taskingDate +": "+cadet+"\n")
                else:
                    num += 1
            num -= 1