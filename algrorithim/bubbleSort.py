#BUBBLE SORT----------------------------------------

for i in range(0, number_of_elements - 1):#outter loop

    


    for index in range(0, number_of_elements - 1):#inner loop

       
        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):

            

            #if above is true, swap places!

            temp = name[index]

            name[index] = name[index + 1]

            name[index + 1] = temp

 
            #swap all other values

            temp = age[index]

            age[index] = age[index + 1]

            age[index + 1] = temp
