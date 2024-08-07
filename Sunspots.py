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
plt.xlabel("Month (Starting form Jan 1749)")
plt.ylabel("Sunspot Occurance")
plt.title("Sunspot Occurance Per Month")
plt.show()

def running_average(data: list, r: "radius"):

    running_avg_data=[]

    for i in range(len(sunspot_number_data)):

        try:
            sum(sunspot_number_data[-r+i, r+i+1])
        if sunspot_number_data.index(data) < r or sunspot_number_data.index(data) > (len(sunspot_number_data) - r):

    for i in range(-r, r+1):
    

    
    
    

    