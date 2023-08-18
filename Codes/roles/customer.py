from operator import itemgetter

def view_cars():
    "Customer can view car details"

    sort = input('Do you want to sort the car details (Yes- y/Y, No- any other key) ? ')
    print('')

    if sort == 'Y' or sort == 'y':
        sort_option = input('Sort by Mileage or Budget (M/m- Mileage, B/b- Budget) : ')
        print('')

        if sort_option == 'm' or sort_option == 'M':

            cars = open('car_details.TXT', 'r')
            carslist = eval(cars.read())
            cars.close()

            pad = ' '

            mileage_sort = sorted(carslist, key=itemgetter(2))

            for count in range(len(mileage_sort)):
                for details in range(len(mileage_sort[0])):
                    print(mileage_sort[count][details] + pad * (12 - len(str(mileage_sort[count][details]))), end=" ")
                print()
            print()

        elif sort_option == 'B' or sort_option == 'b':

            cars = open('car_details.TXT', 'r')
            carslist = eval(cars.read())
            cars.close()

            pad = ' '

            budget_sort = sorted(carslist, key=itemgetter(5))

            for count in range(len(budget_sort)):
                for details in range(len(budget_sort[0])):
                    print(budget_sort[count][details] + pad * (12 - len(str(budget_sort[count][details]))), end=" ")
                print()
            print()

        else:
            print('Invalid letter entered.')
    else:

        cars = open('car_details.TXT', 'r')
        carslist = eval(cars.read())
        cars.close()
        pad = ' '
        for count in range(len(carslist)):
            for details in range(len(carslist[0])):
                print(carslist[count][details] + pad * (12 - len(str(carslist[count][details]))), end=" ")
            print()
        print()



def request_td():
    "Customer can request a test drive"

    f = open('td_request.TXT', 'w')

    f.write('Request pending')

    f.close()

    print('Request has been made :)')


def check_request_td():
    "Customer can check request status"

    f = open('td_approval.TXT', 'r+')

    status = f.read()

    if "Request granted\nAppointment provided" in status:
        print('Your recent test drive request has been granted :)')
        f.truncate(0)
    elif 'No appointment provided' in status:
        print('Your test drive request has been denied ):')
        f.truncate(0)
    else:
        print('Your request has not been granted yet')


def request_to_sell():
    'Customers can request to sell their cars'

    f = open('sell_request.TXT', 'w')
    f.write('sell request')
    print('Request has been made :)')
    print('')
    f.close()


def enter_car_details():
    'Customer can enter enter the details of the car they are going to sell'

    print('Enter The car information , \n')

    car_info = []

    name = input('Your Name :- ')
    make = input('Make :- ')
    model = input('Model :- ')
    mileage = int(input('Mileage (kmpl) (number only) :- '))
    year = int(input('Year :- '))
    price = int(input("Price (Rs) (number only) :- "))

    car_info.append(make)
    car_info.append(model)
    car_info.append(str(mileage))
    car_info.append(str(year))
    car_info.append(name)

    car_s = open('sell_cars.TXT', 'w')
    car_s.write(str(car_info))
    car_s.close()



def check_sell_request():
    'Customer can check the status of the sell request'

    f = open('sell_appoint.TXT', 'r+')

    status = f.read()

    if "Request granted\nAppointment provided" in status:
        print('Your recent test drive request has been granted :)')
        f.truncate(0)
    elif 'No appointment provided' in status:
        print('Your test drive request has been denied ):')
        f.truncate(0)
    else:
        print('Your request has not been granted yet')


def request_service():
    'Customer can request maintainance service'

    f = open('service_request.TXT', 'w')
    f.write('service request')
    print('Request has been made :)')
    f.close()

def check_service_request():
    'Customer can check the status of the service request'

    f = open('service _approval.TXT', 'r+')

    status = f.read()

    if "Request granted\nAppointment provided" in status:
        print('Your recent request has been granted :)')
        f.truncate(0)
    elif 'No appointment provided' in status:
        print('Your request has been denied ):')
        f.truncate(0)
    else:
        print('Your request has not been granted yet')