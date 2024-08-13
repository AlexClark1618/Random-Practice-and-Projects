from matplotlib import pyplot as plt
from Running_Average import running_average

with open("sunspots.txt", "r") as sunspots_file:
    
    sunspot_month_data_list=[]

    for line in sunspots_file:
        parts = line.strip().split()

        data_tuple = (int(parts[0]), float(parts[1]))

        sunspot_month_data_list.append(data_tuple)

month_data = [tup[0] for tup in sunspot_month_data_list]
sunspot_number_data = [tup[1] for tup in sunspot_month_data_list]

def plot_raw_data(toggle: bool):
    plt.plot(month_data, sunspot_number_data, label="Raw Data")
    plt.xlabel("Month (Starting form Jan 1749)")
    plt.ylabel("Sunspot Occurance")
    plt.title("Sunspot Occurance Per Month")
    plt.legend(loc="upper left")

    if toggle:
        plt.show()

def plot_running_average(toggle: bool, r: "window_radius"):
    plt.plot(month_data, running_average(sunspot_number_data, r), label=f'Running Average with Window Radius r={r}')
    plt.xlabel("Month (Starting form Jan 1749)")
    plt.ylabel("Sunspot Occurance")
    plt.title("Sunspot Occurance Per Month")
    plt.legend(loc="upper left")

    if toggle:
        plt.show()


plot_raw_data(False)
plot_running_average(True,r=100)

    
    
    

    