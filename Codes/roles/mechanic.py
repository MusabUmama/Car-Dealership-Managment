def m_info():
    "mechanic can enter following maintenance information"

    maintenance_info = []

    car = input('car : ')
    cost = int(input("Cost of maintenance (Rs) : "))
    damage = input('Damaged areas : ')

    maintenance_info.append(car)
    maintenance_info.append(damage)
    maintenance_info.append(str(cost))

    cost_ = (str(cost)+'\n')

    m_info = open('maintenance_info.TXT', 'r')
    m_info_list = eval(m_info.read())
    m_info.close()

    m_info_list.append(maintenance_info)

    m_info = open('maintenance_info.TXT', 'w')
    m_info.write(str(m_info_list))
    m_info.close()

    costs = open('maintenance_costs.TXT', 'a')
    costs.write(cost_)
    costs.close()




