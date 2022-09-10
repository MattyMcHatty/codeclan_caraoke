#MYRMIDON Build 0.0.1

# Choose your opponent and return the answer so a fight can be started

print('Welcome to')
print('     ___  ___ _  _ ____  ___  ___ __ ____     ___   __  __  ')
print('     || \//|| \ // ||  \ || \//|| || ||  \   //  \  ||\ ||  ')
print('     || \/ ||  )/  ||_// || \/ || || ||  )) ((   )) || \||  ')
print('     ||    || //   ||  \ ||    || || ||_//   \ _//  ||  ||  ')
print('')

def choice_function(opponent):
    print(' ')
    print('     Choose Your Opponent')
    print(' ')
    opponent_choice = input('(r)at, (g)oldfish or (p)igeon : ')
    if opponent_choice == 'r':
        print('You have chosen to fight a rat')           
        opponent = 'rat'
    elif opponent_choice == 'g':
        print('You have chosen to fight a goldfish')
        opponent = 'goldfish'
    elif opponent_choice == 'p':
        print('You have chosen to fight a pigeon')
        opponent = 'pigeon'
    else:
        print('That opponent does not exist!')
        #choice_function(opponent)
    return opponent;

# Rat fight functions

def rat_function(player_hp, rat_turn_counter, player_command, rat_hp, rat_str, rat_def,rat_mag):
        if rat_turn_counter == 4 or rat_turn_counter == 2:
            if player_command == 'a':
                rat_hp = rat_hp - player_str
            elif player_command == 'm':
                rat_hp = rat_hp - player_mag
            if rat_hp > 0:
                print('The rat lunges and bites you!')
                player_hp, player_command = is_move_blocked(player_hp, player_command)
                player_hp = player_hp - rat_str
        elif rat_turn_counter == 3 or rat_turn_counter == 1:
            if player_command == 'a':
                rat_hp = rat_hp + rat_def - player_str
            elif player_command == 'm':
                rat_hp = rat_hp + rat_def - player_mag
            if rat_hp > 0:
                print('The rat turns away and defends itself!')   
        elif rat_turn_counter == 0:
            rat_turn_counter = 5
            if player_command == 'a':
                rat_hp = rat_hp - player_str
            if player_command == 'm':
                rat_hp = rat_hp - player_mag
            if rat_hp > 0:
                print('The rat attacks and misses!')
        rat_hp_left(rat_hp)
        return player_hp, rat_turn_counter, player_command, rat_hp;

def rat_fight_function(player_hp):
    rat_hp = 5
    rat_str = 1
    rat_mag = 0
    rat_def = 1
    rat_turn_counter = 4
    player_command = 0
    print('  ,,==.')
    print(' //    `')
    print('||      ,--~~~~-._ _(\--,_')
    print(' \._,-~   \       v    *  `o')
    print('  `---~\( _/,___( /_/`---~~')
    print('        ``==-    `==-,')
    print(' ')
    while rat_hp > 0:
        is_player_dead(player_hp)
        print('You have ' + str(player_hp) + ' HP left')
        player_command = player_command_function(player_command)
        player_hp, rat_turn_counter, player_command, rat_hp = rat_function(player_hp, rat_turn_counter, player_command, rat_hp, rat_str, rat_def, rat_mag)
        rat_turn_counter = rat_turn_counter - 1
    else:
        print('The rat has been destroyed!')
    return player_hp;

# Determines how much HP the rat has left and if it has none, prints that the rat is dead
def rat_hp_left(rat_hp):
    if rat_hp > 0:
        print('The rat has ' + str(rat_hp) + ' HP remaining!')
    else:
        print('The rat has 0 HP left')

# Goldfish fight functions

def goldfish_function(player_hp, goldfish_turn_counter, player_command, goldfish_hp, goldfish_str, goldfish_def, goldfish_mag):
        if goldfish_turn_counter >= 4:
            if player_command == 'a':
                goldfish_hp = goldfish_hp + goldfish_def - player_str
            elif player_command == 'm':
                goldfish_hp = goldfish_hp + goldfish_def - player_mag
            if goldfish_hp > 0:
                print('The goldfish attempts to deflect your attack with its scales!')
        elif goldfish_turn_counter >= 2 and goldfish_turn_counter <= 3:
            if player_command == 'a':
                goldfish_hp = goldfish_hp - player_str
            elif player_command == 'm':
                goldfish_hp = goldfish_hp - player_mag
            if goldfish_hp > 0:
                print('The goldfish splashes water at you!') 
                player_hp, player_command = is_move_blocked(player_hp, player_command)
                player_hp = player_hp - goldfish_mag
        elif goldfish_turn_counter == 1:
            if player_command == 'a':
                goldfish_hp = goldfish_hp - player_str
            elif player_command == 'm':
                goldfish_hp = goldfish_hp - player_mag
            if goldfish_hp > 0:
                print('The goldfish flails about aimlessly!')
        elif goldfish_turn_counter == 0:
            goldfish_turn_counter = 7
            if player_command == 'a':
                goldfish_hp = goldfish_hp - player_str
            elif player_command == 'm':
                goldfish_hp = goldfish_hp - player_mag
            if goldfish_hp > 0:
                print('The goldfish flails about aimlessly!')
        goldfish_hp_left(goldfish_hp)
        return player_hp, goldfish_turn_counter, player_command, goldfish_hp;

def goldfish_fight_function(player_hp):
    goldfish_hp = 6
    goldfish_str = 0
    goldfish_mag = 1
    goldfish_def = 1
    goldfish_turn_counter = 6
    player_command = 0
    print('  _')
    print('><_>')
    print('')
    while goldfish_hp > 0:
        is_player_dead(player_hp)
        print('You have ' + str(player_hp) + ' HP left')
        player_command = player_command_function(player_command)
        player_hp, goldfish_turn_counter, player_command, goldfish_hp = goldfish_function(player_hp, goldfish_turn_counter, player_command, goldfish_hp, goldfish_str, goldfish_def, goldfish_mag)
        goldfish_turn_counter = goldfish_turn_counter - 1
    else:
        print('The goldfish has been destroyed!')
    return player_hp;

# Determines how much HP the goldfish has left and if it has none, prints that the goldfish is dead
def goldfish_hp_left(goldfish_hp):
    if goldfish_hp > 0:
        print('The goldfish has ' + str(goldfish_hp) + ' HP remaining!')
    else:
        print('The goldfish has 0 HP left')

# Pigeon fight functions

def pigeon_function(player_hp, pigeon_turn_counter, player_command, pigeon_hp, pigeon_str, pigeon_def, pigeon_mag):
        if pigeon_turn_counter == 2:
            if player_command == 'a':
                pigeon_hp = pigeon_hp - player_str
            elif player_command == 'm':
                pigeon_hp = pigeon_hp - (player_mag * 2)
                print('The pigeon is weak to magic!')
            if pigeon_hp > 0:
                print('The pigeon lashes at you with its wing!')
                player_hp, player_command = is_move_blocked(player_hp, player_command)
                player_hp = player_hp - pigeon_str
        elif pigeon_turn_counter == 1:
            if player_command == 'a':
                pigeon_hp = pigeon_hp - player_str
            elif player_command == 'm':
                pigeon_hp = pigeon_hp - (player_mag * 2)
                print('The pigeon is weak to magic!')
            if pigeon_hp > 0:
                print('The pigeon flaps its wings and sends a huge gust straight at you!')
                player_hp, player_command = is_move_blocked(player_hp, player_command)
                player_hp = player_hp - pigeon_mag
        elif pigeon_turn_counter == 0:
            pigeon_turn_counter = 3
            if player_command == 'a':
                pigeon_hp = pigeon_hp - player_str
            elif player_command == 'm':
                pigeon_hp = pigeon_hp - (player_mag * 2)
                print('The pigeon is weak to magic!')
            if pigeon_hp > 0:
                print('The pigeon stands there looking bewildered!')
        pigeon_hp_left(pigeon_hp)
        return player_hp, pigeon_turn_counter, player_command, pigeon_hp;

def pigeon_fight_function(player_hp):
    pigeon_hp = 10
    pigeon_str = 1
    pigeon_mag = 2
    pigeon_def = 1
    pigeon_turn_counter = 2
    player_command = 0
    print('              __')
    print('             /*{>')
    print('         ____) (____')
    print('       // --;   ;--  \ ')
    print('      ///////\_/\ \ \ \ ')
    print('             m m')
    print(' ')
    while pigeon_hp > 0:
        is_player_dead(player_hp)
        print('You have ' + str(player_hp) + ' HP left')
        player_command = player_command_function(player_command)
        player_hp, pigeon_turn_counter, player_command, pigeon_hp = pigeon_function(player_hp, pigeon_turn_counter, player_command, pigeon_hp, pigeon_str, pigeon_def, pigeon_mag)
        pigeon_turn_counter = pigeon_turn_counter - 1
    else:
        print('The pigeon has been destroyed!')
    return player_hp;

# Determines how much HP the pigeon has left and if it has none, prints that the pigeon is dead
def pigeon_hp_left(pigeon_hp):
    if pigeon_hp > 0:
        print('The pigeon has ' + str(pigeon_hp) + ' HP remaining!')
    else:
        print('The pigeon has 0 HP left')

# Determines whether the player blocked the opponents attack
def is_move_blocked(player_hp, player_command):
    if player_command == 'd':
        player_hp = player_hp + player_def
        print('You succesfully blocked the attack, reducing the damage by ' + str(player_def))
    return player_hp, player_command;

# Determines if the player has ran out of HP and if so terminates the program
def is_player_dead(player_hp):
    if player_hp == 0:
        print('You are dead! Game Over')
        exit()

# Determines the players input during any fight
def player_command_function(player_command):
    player_command = input('(a)ttack, (m)agic, (d)efend : ' )
    if player_command == 'a':
            print('You attacked with your sword')
    elif player_command == 'm':
            print('You cast a spell!')
    elif player_command == 'd':
            print('You raised your shield to defend the attack!')
    else:
            print('That is not a valid command! The enemy gains the upper hand!')
    return player_command;


# Player stats
player_hp = 10
player_str = 2
player_mag = 2
player_def = 1

def choose_class(player_hp, player_str, player_mag, player_def):
    print('  Choose your fighting class')
    print(' ')
    print('  (>+<)      (o)         |    ')
    print('    |         |        --|--  ')
    print('    |         |          |    ')
    print('    |         |          |    ')
    print(' ')
    player_class = 0
    player_class = input('(w)arrior, (m)age or (p)aladin : ')
    if player_class == 'w':
        player_hp = 8
        player_str = 3
        player_mag = 1
        player_def = 1
    elif player_class == 'm':
        player_hp = 8
        player_str = 1
        player_mag = 3
        player_def = 1
    elif player_class == 'p':
        player_hp = 10
        player_str = 2
        player_mag = 2
        player_def = 1
    else:
        print('That is not a valid class!')
        choose_class(player_hp, player_str, player_mag, player_def)
    return player_hp, player_str, player_mag, player_def;

rat_dead = 1
goldfish_dead = 1
pigeon_dead = 1

creatures_defeated = 0

player_hp, player_str, player_mag, player_def = choose_class(player_hp, player_str, player_mag, player_def)

while creatures_defeated < 3:
# Define the opponent and choose one to fight
    opponent = 0
    opponent = choice_function(opponent)
    print(str(player_hp) + str(player_str) + str(player_mag) +  str(player_def))
# Determine which opponent was chosen and initiate the fight
    if opponent == 'rat':
        if rat_dead >= 1:
            player_hp = rat_fight_function(player_hp)
            rat_dead -= 1
            creatures_defeated += 1
        elif rat_dead <= 0:
            print('The rat has already been destroyed!')
    elif opponent == 'goldfish':
        if goldfish_dead >= 1:
            player_hp = goldfish_fight_function(player_hp)
            goldfish_dead -= 1
            creatures_defeated += 1
        elif goldfish_dead <=0:
            print('The goldfish has already been destroyed!')
    elif opponent == 'pigeon':
        if pigeon_dead >= 1:
            player_hp = pigeon_fight_function(player_hp)
            pigeon_dead -= 1
            creatures_defeated += 1
        elif pigeon_dead <= 0:
            print('The pigeon has already been destroyed!')
    #print(creatures_defeated)

print('You have defeated all the creatures!')









