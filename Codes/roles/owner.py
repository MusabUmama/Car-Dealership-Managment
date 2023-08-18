
def view_customer_info():
    'Owner can View The customer information'

    c = open('customer_info.TXT', 'r')
    readlist = eval(c.read())
    c.close()

    pad = ' '

    for count in range(len(readlist)):
        for details in range(len(readlist[0])):
            print(readlist[count][details] + pad * (30 - len(str(readlist[count][details]))), end=" ")
        print()
    print()


def top_models():
    'owner can view the top 5 models sold'

    f = open('sold_cars.TXT', 'r')
    cars = eval(f.read())
    f.close()

    models = []

    for line in cars:
        model = line[1]
        models.append(model.upper())

    top = max(set(models), key=models.count)

    print('1.',top)

    for m in models:
        if m == top:
            models.remove(m)

    for i in models:
        if i == top:
            models.remove(i)

    second = max(set(models), key=models.count)

    print('2.',second)

    for k in models:
        if k == second:
            models.remove(k)

    for k in models:
        if k == second:
            models.remove(k)

    third = max(set(models), key=models.count)

    print('3.',third)

    for j in models:
        if j == third:
            models.remove(j)

    for j in models:
        if j == third:
            models.remove(j)

    fourth = max(set(models), key=models.count)

    print('4.',fourth)

    for p in models:
        if p == fourth:
            models.remove(p)

    for p in models:
        if p == fourth:
            models.remove(p)

    fifth = max(set(models), key=models.count)

    print('5.',fifth)


def best_customers():
    'Owner can view the best customers'

    f = open('customer_info.TXT', 'r')
    customers = eval(f.read())
    f.close()

    names = []

    for line in customers:
        name = line[0]
        names.append(name.upper())

    top = max(set(names), key=names.count)

    print('1.', top)

    for m in names:
        if m == top:
            names.remove(m)

    for m in names:
        if m == top:
            names.remove(m)

    second = max(set(names), key=names.count)

    print('2.', second)

    for m in names:
        if m == second:
            names.remove(m)

    for m in names:
        if m == second:
            names.remove(m)

    third = max(set(names), key=names.count)

    print('3.', third)

    for j in names:
        if j == third:
            names.remove(j)

    for j in names:
        if j == third:
            names.remove(j)


    fourth = max(set(names), key=names.count)

    print('4.', fourth)

    for p in names:
        if p == fourth:
            names.remove(p)

    for p in names:
        if p == fourth:
            names.remove(p)


    fifth = max(set(names), key=names.count)

    print('5.', fifth)
