# finding average temparature
temp_list = []
days = int(input("how many days average temp do u need ?"))
for i in range(days):
    temp = int(input("enter the temp recorded:"))

    temp_list.append(temp)
    print(temp_list)
    average_temp = float(sum(temp_list[i])/days)
    print(average_temp)

