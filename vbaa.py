import random

def bot_select_action(player_hp, player_attack, player_heal, player_block, bot_hp, bot_attack, bot_heal, bot_block):

    if bot_hp < 35:
        return 2
    
    if player_hp < 20:
        return 1