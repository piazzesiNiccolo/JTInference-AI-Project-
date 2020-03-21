print('importing modules...')
import examples.icy_roads as ice
import examples.fire as fire
import examples.cancer_neapolitan as cancer
import examples.mrs_gibbon as mrs

examples = {1:ice.icy_roads_example, 2:mrs.mrs_gibbon_example, 3:fire.fire_example,4:cancer.cancer_neapolitan_example}
choice = ''
while choice !=  '0': 
    choice = input('scegli: ').lower()
    ex = int(choice)
    examples.get(ex, lambda: print('invalid choice'))()
    

