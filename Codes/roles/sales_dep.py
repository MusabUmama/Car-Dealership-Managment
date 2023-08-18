
def profit_calculator():
    'Owner can view the total monthly profit'

    f = open('selling_prices.TXT', 'r')

    amounts = f.readlines()

    total = 0

    file = open('asking_prices.TXT', 'r')
    a = file.readlines()

    tot = 0

    for i in a:
        tot = tot + int(i)

    print('Total asked prices of sold cars - Rs.', float(tot))

    for amount in amounts:
        total = total + int(amount)

    print('total selling income - Rs.', float(total))


    profit = (tot - total)

    print('_'*50)
    print('Total Profit for the month : Rs.', float(profit))
    print('_' * 50)


def total_incomes():
    'Total incomes of this month and last 5 months'

    total_incomes = [float(201396650), float(191326800), float(188162000), float(178955300), float(183558660)]

    f = open('maintenance_costs.TXT', 'r')
    maintenace_income = f.readlines()
    f.close()

    file = open('selling_prices.TXT', 'r')
    selling_income = file.readlines()
    file.close()

    sell_income = 0
    maintenance_in = 0

    for amount in selling_income:
        sell_income = sell_income + int(amount)

    print('Total sales income this month (So far) :- Rs.', sell_income)

    for figure in maintenace_income:
        maintenance_in = maintenance_in + int(figure)

    print("Total maintenance income this month (So far) :- Rs.", maintenance_in)

    total_income = sell_income + maintenance_in

    print('Total income for the month (so far) :- Rs.', total_income)
    print('')

    total_incomes.append(float(total_income))

    month = 1
    count = 0


    print('Total incomes of last 5 months,\n')
    print('')

    while count <= 4:

        print('Month', month, 'total income :- ', 'Rs.', total_incomes[count])

        count += 1
        month += 1


def no_of_cars_sold():
    'Number of cars sold for last 6 months'

    f = open('sold_cars.TXT', 'r')
    lines = eval(f.read())
    f.close()

    cars = []

    for line in lines:
        car = line[0]
        cars.append(car)

    count = len(cars)

    no_of_cars_sold = [22, 25, 27, 24, 19]

    no_of_cars_sold.append(count)

    print('Number of cars sold this month (So far) :- ', count, 'Cars')
    print('')

    n = 0
    month = 1

    while n <= 4:
        print('Number of cars sold for month', month, ':-', no_of_cars_sold[n], 'Cars')

        n += 1
        month += 1


def cars_sold_graph():
    'Graph which visualize the number of cars sold monthly for last 6 months'

    f = open('sold_cars.TXT', 'r')
    lines = eval(f.read())
    f.close()

    cars = []

    for line in lines:
        car = line[0]
        cars.append(car)

    count = len(cars)

    no_of_cars_sold = [22, 25, 27, 24, 19]

    no_of_cars_sold.append(count)

    print('\t\t\tNumber of cars sold - Last 6 months\t\t\t\t\t0 - Count\n')

    count = 5
    month = 6

    while count >= 0:
        print('Month', month, '|', (int((no_of_cars_sold[count] / 2) * 2.4)) * '0', '\n')
        count -= 1
        month -= 1

    print('=' * 70, '>  Cars')

    n = 0

    while n <= 50:
        print('\t\t', '|', end='\t')

        n += 10

    print('\n')

    i = 0

    while i <= 50:
        print('\t\t', i, end='\t')

        i += 10

    print('\n\n\t\t\t\tNumber of cars')


def income_graph():
    'Graph that visualize monthly income for last 6 months'

    total_incomes = [201396650, 191326800, 188162000, 178955300, 183558660]

    f = open('maintenance_costs.TXT', 'r')
    maintenace_income = f.readlines()
    f.close()

    file = open('selling_prices.TXT', 'r')
    selling_income = file.readlines()
    file.close()

    sell_income = 0
    maintenance_in = 0

    for amount in selling_income:
        sell_income = sell_income + int(amount)

    for figure in maintenace_income:
        maintenance_in = maintenance_in + int(figure)

    total_income = sell_income + maintenance_in

    total_incomes.append(float(total_income))

    print('\t\t\t\tTotal incomes for last 6 months\t\t\t\t\t0 - Count (1 Million)\n')

    n = 5
    month = 6

    while n >= 0:
        print('Month', month, '|', int((total_incomes[n] / 1000000)) * '0', '\n')

        n -= 1
        month -= 1

    print('=' * 224, '>  Million Rs')

    print('\t\t', '|\t\t ' * 10, '|\t\t\t  ' * 12)

    i = 0

    while i <= 210:
        print('\t\t', i, end='')

        i += 10

    print('\n\n\t\t\t\t\t\t\t\t\tTotal income')