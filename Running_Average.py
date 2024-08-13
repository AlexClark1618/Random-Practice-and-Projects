
def running_average(data: list, r: "window radius"):

    running_avg_list = []

    for i in range(len(data)):

        list_window = data[-r+i: r+i+1]
        
        if not list_window or (r+i+1) > len(data): #Addresses the indexing errors at the boundaries #Note: Returning empty list becasue negative indices just reverse the order. So i can alter the code to do the except when the list is empty

            start_index = max(0, i - r)

            end_index = min(len(data), i + r + 1)    
                
            list_window = data[start_index: end_index]
            
            while len(list_window) < (2 * r + 1):
                    
                list_window += list_window #Duplicates list

        list_window_avg = sum(list_window) / len(list_window)

        running_avg_list.append(list_window_avg)

    return running_avg_list


if __name__ == "__main__":

    prac_list=[1,2,3,4,5,6,7,8,9,10]

    print(running_average(prac_list, r=2))