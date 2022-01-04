def min_num_taxis(requests):
    pu, do = zip(*requests)
    counter = 0
    pu_list, do_list =[x for x in pu], [x for x in do]
    pu_list.sort() 
    do_list.sort()
    for element in pu_list:
        if element <= do_list[0]:
            counter +=1
        else:
            del do_list[0]
    return counter