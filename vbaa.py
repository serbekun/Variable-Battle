import random

def bot_select_action(player_hp, player_attack, player_heal, player_block, bot_hp, bot_attack, bot_heal, bot_block, round_count):

    if bot_hp < 35:
        return 2
    
    if player_hp < 20:
        return 1

    if round_count < 5:
        return 5
    
    bot_action = random.randint(1, 5)

    if bot_action == 1:
        return 1
    elif bot_action == 2:
        return 2
    elif bot_action == 3:
        return 3
    elif bot_action == 4:
        return 4
    elif bot_action == 5:
        return 5
