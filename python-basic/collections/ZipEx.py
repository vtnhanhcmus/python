names = ['Peter packer', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['SpiderMan', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')
