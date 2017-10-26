import random
def main():
    first_names=('Lydia', 'Emma', 'Andrew', 'Josie', 'Owen', 'Jack', 'Tucker', 'Samantha', 'Frank',
                'Bill', 'Joey', 'Bob', 'Gorg', 'Jose', 'Jorge', 'Scorge', 'Ben', 'Anita', 'Casey',
                'Bella', 'Marcus', 'Austin', 'Mat', 'Grace', 'Mia', 'Connor', 'Harrison', 'Charlie',
                'Taylor', 'Maxine', 'Anja', 'Aaron', 'Erin', 'Ruthie', 'Emily', 'Chloe', 'Matt', 'David',
                'Kim', 'Cutter', 'Aidan', 'Riley', 'Rosalie', 'Haden', 'Georgina')

    word = ('Lydia', 'Emma', 'Andrew', 'Josie', 'Owen', 'Jack', 'Tucker', 'Samantha', 'Frank',
                 'Bill', 'Joey', 'Bob', 'Gorg', 'Jose', 'Jorge', 'Scorge', 'Ben', 'Anita', 'Casey',
                 'Bella', 'Marcus', 'Austin', 'Mat', 'Grace', 'Mia', 'Connor', 'Harrison', 'Charlie',
                 'Taylor', 'Maxine', 'Anja', 'Aaron', 'Erin', 'Ruthie', 'Emily', 'Chloe', 'Matt', 'David',
                 'Kim', 'Cutter', 'Aidan', 'Riley', 'Rosalie', 'Haden', 'Georgina')
first_names='word'[3]
print first_names

last_name=('Elliott', 'Harrington', 'Bryant', 'Schwieterman', 'Blake', 'Brown', 'Brooks', 'Palma',
                'Sweatyman', 'Holt', 'Dover', 'Pea', 'Holmes', 'Palmtree', 'Concannon', 'Eremita',
                'McFall', 'Lievens', 'Champagne', 'Lane', 'Bradish', 'Sargent', 'Harmon', 'Wilson',
                'DuPuy', 'Wells', 'Doopy', 'Ewing', 'Amory', 'Lawrence', 'Meeker', 'MacMahone', 'Bacon',
                'Reynolds', 'Forest', 'Leonard')

word = ('Elliott', 'Harrington', 'Bryant', 'Schwieterman', 'Blake', 'Brown', 'Brooks', 'Palma',
                    'Sweatyman', 'Holt', 'Dover', 'Pea', 'Holmes', 'Palmtree', 'Concannon', 'Eremita',
                    'McFall', 'Lievens', 'Champagne', 'Lane', 'Bradish', 'Sargent', 'Harmon', 'Wilson',
                    'DuPuy', 'Wells', 'Doopy', 'Ewing', 'Amory', 'Lawrence', 'Meeker', 'MacMahone', 'Bacon',
                    'Reynolds', 'Forest', 'Leonard')
last_name=word[3],random.choice('last_name')
print last_name

group = random.choice('first_names') + ' ' + random.choice('last_name')
print(group)

for x in range(0, 20):
    main()
