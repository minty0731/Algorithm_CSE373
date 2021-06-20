from random import choices


def group_by_color(data, start, stop, color):
    operations_counter = 0

    while start < stop and start < len(data) and stop >= 0:
       
        while start < len(data) and data[start] == color:  
            start += 1  
            operations_counter += 1

        while start < stop and stop >= 0 and data[stop] != color:  
            stop -= 1  
            operations_counter += 1

        if start < stop:
            data[start], data[stop] = data[stop], data[start] 
            operations_counter += 1

    assert operations_counter <= len(data) * 2  
    return start 


colors_list = choices(['red', 'white', 'blue'], k=100)
red_ending = group_by_color(colors_list, 0, len(colors_list) - 1, 'red')  
group_by_color(colors_list, red_ending + 1, len(colors_list) - 1, 'white')
