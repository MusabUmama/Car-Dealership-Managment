from roles import admin
from roles import customer
from roles import owner
from roles import mechanic
from roles import sales_dep


rerun = 'y'
admin_password = 'Admin&99a'
owner_password = 'Boss0#1'
mechanic_password = 'mech@6w'


while rerun == 'y':
    print('1- Admin\n2- Owner\n3- Customer\n4- Mechanic')
    print("")
    role_number = input('Enter the role number : ')
    print('')

    if role_number == '1':

        password = input('Enter the password :- ')
        print('')

        if password == admin_password:

            print('A- Entering car details.\nB- Entering customer (Buyer) information.\nC- Check and Approve customer requests.\nD- Enter Sold car details.')
            print('')

            function_option = input('Enter the function letter : ')

            if function_option == 'A' or function_option == 'a':

                admin.enter_car_details()

            elif function_option == 'B' or function_option == 'b':

                admin.enter_customer_info()

            elif function_option == 'C' or function_option == 'c':

                print('1- Customer test drive requests.\n2- Customer sell requests.\n3- Customer maintenance request')
                print('')

                approve_opt = input('Enter the function number :- ')
                print('')

                if approve_opt == '1':
                    admin.approve_request_td()

                elif approve_opt == '2':
                    admin.approve_request_sell()

                elif approve_opt == '3':
                    admin.approve_service_request()

                else:
                    print('Invalid input')

            elif function_option == 'D' or function_option == 'd':

                admin.enter_sold_cars()

            else:
                print('Invalid letter')

        else:
            print('Wrong password\n')

    elif role_number == '2':

        o_password = input('Enter the password :- ')
        print('')

        if o_password == owner_password:

            print('A- View Customer Information.\nB- View Monthly Reports and Graphs.')
            print("")
            view_option = input('Enter The option (A/a or B/b) : ')
            print('')

            if view_option == 'a' or view_option == 'A':

                owner.view_customer_info()

            elif view_option == 'b' or view_option == 'B':
                print('')

                print('A - Total monthly profit\nB - Top 5 sold car models of the month.\nC - Best customers for the month.\nD - Total income for the last 6 months.\nE - Number of cars sold last 6 months.\nF - View graphs.\nG - Full report (All in One).')
                print('')

                owner_choice = input('Enter the option : ')
                print('')

                if owner_choice == 'A' or owner_choice == 'a':

                    sales_dep.profit_calculator()

                elif owner_choice == 'B' or owner_choice == 'b':

                    owner.top_models()

                elif owner_choice == 'C' or owner_choice == 'c':

                    owner.best_customers()

                elif owner_choice == 'D' or owner_choice == 'd':

                    sales_dep.total_incomes()

                elif owner_choice == 'E' or owner_choice == 'e':

                    sales_dep.no_of_cars_sold()

                elif owner_choice == 'F' or owner_choice == 'f':

                    print('1 - Number of cars sold monthly.\n2 - Monthly incomes for last 6 months.')
                    print('')

                    graph_no = input('Enter the graph number :- ')
                    print('')

                    if graph_no == '1':

                        sales_dep.cars_sold_graph()

                    elif graph_no == '2':

                        sales_dep.income_graph()

                    else:
                        print("Wrong number \n")

                elif owner_choice == 'G' or owner_choice == 'g':

                    print('\t\tTotal profit for the month\n')
                    print('')

                    sales_dep.profit_calculator()
                    print('')

                    print('\t\tBest car models of the month\n')
                    print('')

                    owner.top_models()
                    print('')

                    print('\t\tBest customers of the month\n')
                    print('')

                    owner.best_customers()
                    print('')

                    print('\t\tTotal monthly incomes\n')
                    print('')

                    sales_dep.total_incomes()
                    print('')

                    print('\t\tNumber of cars sold\n')
                    print('')

                    sales_dep.no_of_cars_sold()
                    print('')

                    print('\t\tGraph - Monthly income\n')
                    print('')

                    sales_dep.income_graph()
                    print('')

                    print('\t\tGraph - Number of cars sold\n')
                    print('')

                    sales_dep.cars_sold_graph()
                    print('')

                    print('\t\tEnd of report.')

                else:
                    print('Wrong letter')
                    pass

        else:
            print('Wrong password\n')

    elif role_number == '3':

        print('A- view cars.\nB- Request for test drive.\nC- Request to sell cars.\nD- Request for maintenance service.\nE- Check status of the requests.')
        print('')

        customer_option = input('Enter the option : ')
        print('')

        if customer_option == "A" or customer_option == 'a':
            customer.view_cars()

        elif customer_option == 'B' or customer_option == 'b':
            customer.request_td()

        elif customer_option == 'C' or customer_option == 'c':
            customer.request_to_sell()
            customer.enter_car_details()

        elif customer_option == 'D' or customer_option == 'd':
            customer.request_service()

        elif customer_option == 'e' or customer_option == 'E':
            print('1- Check test drive request status.\n2- Check sell request status.\n3- Check maintenance request status')
            print('')

            check_opt = input('Enter the function number :- ')
            print('')

            if check_opt == '1':
                customer.check_request_td()
            elif check_opt == '2':
                customer.check_sell_request()
            elif check_opt == '3':
                customer.check_service_request()
            else:
                print('Invalid input\n')

        else:
            print('Invalid input\n')


    elif role_number == '4':

        m_password = input('Enter the password :- ')
        print('')

        if m_password == mechanic_password:
            mechanic.m_info()

        else:
            print('Wrong password\n')

    else:
        print("Wrong Input !")

    print('')
    rerun_main_menu = input('\nDo you want to Go back to the main Menu (Yes - Y/y, No - any key) ? ')

    if rerun_main_menu == 'Y' or rerun_main_menu == 'y':

        rerun == 'y'

    else:

        print('\n\t\t\t\t--------------******--------------')
        break