
def main():
    choice = input('\n Where do you want to go for the ultimate surviving test? (riverside/hilltop): ')

    if choice == 'riverside':
        return river_side()
    elif choice == 'hilltop':
        return hill_top()

def river_side():
    choice = input('\n You found yourself at a riverside.It has a strong flowing water.you have given the task to survive till the morning.Choose an option(bath/fishing): ').lower()

    if choice == 'bath':
        print('Gameover! You got swept away by the tides.')
    elif choice == 'fishing':
        return fishing()
    else:
        print('invalid choice')

def fishing():
    choice = input('\n You went for fishing,not sure with what object. Choose an option(withstick/withhand): ').lower()

    if choice == 'withstick':
        return fire()
    elif choice == 'withhand':
        print('a poisonus fish attacted you, you died.Game over.')
    else:
        print('invalid choice')

def fire():
    choice = input('\n You got a nice fish.You have to fry it with fire. But Fire can attract wild animals. You got confused. Choose an option(burnfire/nofire): ').lower()

    if choice == 'burnfire':
        return blowout()
    elif choice == 'nofire':
        print('you feared and decided to didnt burn fire.as a result you straved and died.Game over.')
    else:
        print('invalid choice')

def blowout():
    choice = input('\n You have eaten fish. and now you wnat to sleep but fire? (blowout/keep): ').lower()
    
    if choice == 'blowout':
        print('You decided to blow out the fire and went to sleep. and the morning came in a blink of an eye. You win.')
    elif choice == 'keep':
        print('you feared and decided to keep fire.fire spread to the jungle and a wolf came and killed you .Game over.')
    else:
        print('invalid choice')

def hill_top():
    choice = input('\n you found youself on top of the hill.you have given the task to survive till the morning.you found an old cave.Where would you sleep?(insidecave/outsidecave): ').lower()

    if choice == 'insidecave':
        return oldcave()
    elif choice == 'outsidecave':
        print('you decided not to go into the cave, suddenly thunders and rain came as downpour and u got caught in the thunders. you died, Game Over.')
    else:
        print('Invalid choice.')

def oldcave():
    choice = input('\n You found so mush darkness in the cave.where do you want to spend night on? (tent/ground): ').lower()

    if choice == 'tent':
        return tent()
    elif choice == 'ground':
        print('you decided to spend the night on the ground,but un fortunately a scorpion came upon and bite you,and you died.Game Over.')
    else:
        print('Invalid choice.')

def tent():
    choice = input('\n you got sleepy.what do you want? (sleep/explore): ').lower()

    if choice == 'explore':
        return explore()
    elif choice == 'outsidecave':
        print('you decided to sleep, but there was a bear inside cave ,that killed you. you died, Game Over.')
    else:
        print('Invalid choice.')

def explore():
    choice = input('\n You find a creepy oldman probably of 100+ year old. And a small pond full of honey .where do you want to go to? (oldman/honey): ').lower()

    if choice == 'oldman':
        return oldman()
    elif choice == 'honey':
        print('you decided to go towards honey, but there is a bear sleeping. due to bees he gets up and killed you. you died, Game Over.')
    else:
        print('Invalid choice.')

def oldman():
    choice = input('\n you got close to oldman with the frightening step but u stopped. Enter your choice? (meet/ignore): ')

    if choice == 'meet':
        return meet()
    elif choice == 'ignore':
        print('you decided to ignore the oldman,and you got lost in the cave. and died due to suffosticating on the lack of oxygen in the cave.Game Over')
    else:
        print('Invalid choice.')

def meet():
    choice = input('\n you gave the oldman some food you have on yourself. oldman smiled and receive your offering. he gave you two rewards as a thanks given but he told you to pick only one. Pick only one. (oldmap/oldring): ')
    
    if choice == 'oldmap':
        print('you have a fond of old maps, so u choose map over the ring,and fortunately with the help of the map ,you are able to find the treasure that has been in the cave for long time and no one was able to find it.You win')
    elif choice == 'oldring':
        print('you decided to take the ring as a thought of that the ring is some kind of treasure, you put that into your ring finger but that is poisonus ,that killed you. you died, Game Over.')
    else:
        print('Invalid choice.')
    
main()