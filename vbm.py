import vbc
import vbab
import vba

# inzelashion value

round_count = 0

# player

player_hp = 100
player_attack = 5
player_heal = 5
player_block = False

player_action = 0

# bot

bot_hp = 100
bot_attack = 5
bot_heal = 5
bot_block = False

bot_action = 0

while True:
    
    if vbc.chek_end_round(round_count, player_hp, bot_hp) == False:
        print("exiting")
        exit(1)
        
    vbc.show_display(player_hp, player_attack, player_heal, player_block, bot_hp, bot_attack, bot_heal, round_count)
    
    player_action = input(":")

    # player action select
    
    if player_action == "1" or player_action == "a":
        player_now_attack = True
        bot_hp, bot_block = vba.player_attack_def(player_attack, bot_hp, bot_block)
    elif player_action == "2" or player_action == "h":
        player_hp = vba.player_heal_def(player_heal, player_hp)
    elif player_action == "3" or player_action == "b":
        player_block = vba.player_block_def(player_block)
    elif player_action == "4" or player_action == "ia":
        player_attack = vba.player_increase_attack_def(player_attack)
    elif player_action == "5" or player_action == "ih":
        player_heal = vba.player_increase_heal_def(player_heal)
    else:
        print("Turn skipped!")


    # bot place 

    bot_action = vbab.bot_select_action(player_hp, player_attack, player_heal, player_block, bot_hp, bot_attack, bot_heal, bot_block)

    if bot_action == 1:
        player_hp, player_block = vba.bot_attack_def(bot_attack, player_hp, player_block)
    if bot_action == 2:
        bot_hp = vba.bot_heal_def(bot_heal, bot_hp)
    if bot_action == 3:
        bot_block = vba.bot_block_def(bot_block)
    if bot_action == 4:
        bot_attack = vba.bot_increase_attack_def(bot_attack)
    if bot_action == 5:
        bot_heal = vba.bot_increase_heal_def(bot_heal)
        
    player_hp, player_attack, player_heal, bot_hp, bot_attack, bot_heal = vbc.cat_limits(player_hp, player_attack, player_heal, bot_hp, bot_attack, bot_heal)


    round_count += 1


