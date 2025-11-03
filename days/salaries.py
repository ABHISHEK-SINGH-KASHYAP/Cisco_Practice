salaries = [] #list() => this is called constructor of list i.e. init fucmtion inside the class is called

salaries.append(30000)
salaries.append(40000)
salaries.append(99000)

print(salaries)

search = 40000
I = 0
search_index = -1
for salary in salaries:
    if salary==search:
        search_index = I
        break
    I +=1

print(search_index)