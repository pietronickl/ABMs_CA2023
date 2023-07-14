#SIR.py

## there must be a way of doing this that doesn't require back and forth conversion of flat and matrix views of the grid 

side = 100

# initialise an empty array with the population size
SIR = np.zeros((side, side))

# random patient 0: first infection
SIR[randint(0, side), randint(0, side)] = 1  

# plot the 1-dimensional array as a 2D matrix, by reshaping it. Then display
im = plt.imshow(SIR)
plt.axis('off')

# while there is at least one active infection, the cascade keeps going
while 1 in SIR: 

    # get neighbors of infected person
    neighbors = []

    infected = np.nonzero(SIR == 1) #index of infected person 

    for x in infected[0]:
        for y in infected[1]:
            neighbors.append(get_neighbors_indices(SIR, x[0], y[1]))

    flattened = list(itertools.chain(*neighbors))
    
    unique_neighbors = list(set(flattened))

    # Keep only those who are susceptible, i.e. whose value is 0

    susceptible_neighbors = np.array([n for n in unique_neighbors if SIR[n] == 0])

    sharing_p = 0.30 

    actually_infected = rand(1, len(susceptible_neighbors)) 

    got_it = (actually_infected < sharing_p)

    new_inf = susceptible_neighbors[got_it[0]] #why is got_it a 2D array??

    # those who were already infected recover (2)
    SIR[np.nonzero(SIR == 1)] = 2

    # the newly infected become infectious (1)
    SIR[new_inf] = 1

    # update figure
    im.set_data(SIR.reshape(int(sqrt(N)), int(sqrt(N))))

    # show figure
    display.display(plt.gcf())
    display.clear_output(wait=True)

    # pause for a split second 
    time.sleep(0.1)
    

# print all the recovered cells
#print(f'in this cascade, {np.count_nonzero(SIR == 2)} people were infected')