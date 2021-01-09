from random import shuffle

male = ['Nicolas', 'chaelchael', 'haeh', 'kimgappa', 'crosskoo']
female = ['tula', 'mercy', 'hana', 'jane', 'emma']

shuffle(male)
shuffle(female)
couples = zip(male, female)

for i, couple in enumerate(couples):
    print('couple %d : [%s]-[%s]' % (i+1, couple[0], couple[1]))
