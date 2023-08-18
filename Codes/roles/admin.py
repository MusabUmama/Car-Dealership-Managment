
def enter_car_details():
    "admin should enter following details of the car"

    car_details = []

    make = input('Make :- ')
    model = input('Model :- ')
    mileage = input('Mileage (kmpl) :- ')
    year = int(input('Year :- '))
    owner = input('Owner :- ')
    asking_price = input('Asking Price (Rs):- ')
    selling_price = input('Selling Price (Rs):- ')

    car_details.append(make)
    car_details.append(model)
    car_details.append(mileage)
    car_details.append(str(year))
    car_details.append(owner)
    car_details.append(selling_price)

    cars = open('car_details.TXT', 'r')
    carlist = eval(cars.read())
    cars.close()

    carlist.append(car_details)

    car_s = open('car_details.TXT', 'w')
    car_s.write(str(carlist))
    car_s.close()


def enter_sold_cars():
    'Admin can enter sold cars details'

    sold_cars = []

    make = input('Make :- ')
    model = input('Model :- ')
    mileage = input('Mileage (kmpl) :- ')
    year = int(input('Year :- '))
    asking_price = input('Asked Price (Rs):- ')
    selling_price = input('Sold Price (Rs):- ')

    sold_cars.append(make.upper())
    sold_cars.append(model.upper())
    sold_cars.append(mileage)
    sold_cars.append(str(year))
    sold_cars.append(selling_price)

    sc = open('sold_cars.TXT', 'r')
    carlist = eval(sc.read())
    sc.close()

    carlist.append(sold_cars)

    sc = open('sold_cars.TXT', 'w')
    sc.write(str(carlist))
    sc.close()

    asking_p = (str(asking_price) + '\n')
    selling_p = (str(selling_price) + '\n')

    ap = open('asking_prices.TXT', 'a')
    ap.write(asking_p)
    ap.close()

    sp = open('selling_prices.TXT', 'a')
    sp.write(selling_p)
    sp.close()


def enter_customer_info():
    "admin should enter following customer informations"

    customer_info = []

    name = input('Name :- ')
    tel_no = int(input('Telephone Number :- '))
    email = input('Email :- ')
    address = input('Address :- ')
    nic = input('NIC Number :- ')
    sold_car_price = int(input("Final Sold price (Rs) :- "))

    customer_info.append(name.upper())
    customer_info.append(str(tel_no))
    customer_info.append(email)
    customer_info.append(address)
    customer_info.append(nic)
    customer_info.append(str(sold_car_price))

    ci = open('customer_info.TXT', 'r')
    customer_list = eval(ci.read())
    ci.close()

    customer_list.append(customer_info)

    ci = open('customer_info.TXT', 'w')
    ci.write(str(customer_list))
    ci.close()


def approve_request_td():
    "admin can check and approve customer requests for test drive"

    f = open('td_request.TXT', 'r+')
    file = open('td_approval.TXT', 'w')

    check = f.read()

    if "Request pending" in check:
        print('There is a new customer request')

        print('')

        approve = input('Provide an appointment (Y/y- Yes, Any other key- No) ? : ')

        if approve == 'Y' or approve == 'y':
            file.write('Request granted\nAppointment provided')
            print('Appointment provided')
            f.truncate(0)

            file.close()
        else:
            print('No appointment provided')
            f.truncate(0)
    else:
        print('No new requests')


def approve_request_sell():
    'admin can check and approve customer request to sell cars'

    f = open('sell_request.TXT', 'r+')
    file = open('sell_appoint.TXT', 'w')

    check = f.read()

    if 'sell request' in check:
        print('There is a new sell request.')
        print('')

        approve = input('Provide an appointment (Y/y- Yes, Any other key- No) ? : ')

        if approve == 'Y' or approve == 'y':
            file.write('Request granted\nAppointment provided')
            print('Appointment provided')
            f.truncate(0)

            file.close()

        else:
            print('No appointment provided')
            f.truncate(0)

    else:
        print('No new requests')


def approve_service_request():
    'Admin can check and approve customer service request'

    f = open('service_request.TXT', 'r+')
    file = open('service _approval.TXT', 'w')

    check = f.read()

    if 'service request' in check:
        print('There is a new service request.')
        print('')

        approve = input('Provide an appointment (Y/y- Yes, Any other key- No) ? : ')

        if approve == 'Y' or approve == 'y':
            file.write('Request granted\nAppointment provided')
            print('Appointment provided')
            f.truncate(0)

            file.close()

        else:
            print('No appointment provided')
            f.truncate(0)

    else:
        print('No new requests')
