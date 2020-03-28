print('importing modules...')
import examples.icy_roads as ice
import examples.fire as fire
import examples.cancer_neapolitan as cancer
import examples.mrs_gibbon as mrs

print('#############################################################################################\n\n')
print('This simple program test the HUGIN algorithm for belief propagation in junction trees\n\n')
print('To do so, it creates 4 examples of bayesian networks and their junction tree\n')
print('On each network it  runs a certain amount of queries\n')
print('For each query it shows the wanted probability before and after entering some kind of evidence\n')

print('\n\n#############################################################################################')
input('PRESS ENTER TO START THE PROGRAM\n\n\n')

examples = {1:ice.icy_roads_example, 2:mrs.mrs_gibbon_example, 3:fire.fire_example,4:cancer.cancer_neapolitan_example}

exit = False
while not exit: 
    choice = input('\nSelect a number to run an example:\n\n\
1: icy_roads   2: mrs_gibbon   3: fire  4: cancer_neapolitan  quit: EXIT PROGRAM\n\n:').lower()
    
    if choice == 'quit':
        exit = True
        continue
    try:
        ex = int(choice)
        run = examples.get(ex, lambda: print('invalid choice, choose a number between 1 and 4'))
        run()
    except ValueError:
        print('\nINCORRECT VALUE, TRY AGAIN\n')
        
        
        
    
    

