from matplotlib import pyplot as plt

with open("sunspots.txt", "r") as sunspots_file:
    
    sunspot_month_data_list=[]

    for line in sunspots_file:
        parts = line.strip().split()

        data_tuple = (int(parts[0]), float(parts[1]))

        sunspot_month_data_list.append(data_tuple)

month_data = [tup[0] for tup in sunspot_month_data_list]
sunspot_number_data = [tup[1] for tup in sunspot_month_data_list]

plt.plot(month_data, sunspot_number_data)
plt.xlabel("Month (form Jan 1749)")
plt.ylabel("Sunspot Occurance")
plt.title("Sunspot Occurance Per Month")
plt.show()
    

    
    
    

    