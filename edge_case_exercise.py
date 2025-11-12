def move(my_list, direction):

    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    if direction == 'right' :
        if idx < len(my_list) -1 :
            my_list[idx] = 0
            my_list[idx + 1] = 1
    elif direction == 'left' : 
        if idx > 0 :
            my_list[idx] = 0
            my_list[idx -1 ] = 1
 

    return my_list
