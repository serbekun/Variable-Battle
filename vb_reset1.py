import random

round_count = 0

# Initialize values

# Game setting

select_event_setting = True
random_event_setting = True

# player settings
player_hp = 100
player_attack = 5
player_heal = 5
player_block = False
player_attack_inc = 5
player_heal_inc = 5

# ai settings
ai_hp = 100
ai_attack = 5
ai_heal = 5
ai_block = False
ai_attack_inc = 5
ai_heal_inc = 5

while round_count < 100:
    
    #event 
    
    #maybi next update
    
    # Game random event
    
    if random_event_setting == True:
        random_event_first_chanse = random.randint(1, 30)
        if random_event_first_chanse == 1:
            ai_hp -= 50
            player_hp -= 50

    # check player
    if player_hp > 150:
        player_hp = 150
    if player_attack > 100:
        player_attack = 100
    if player_heal > 50:
        player_heal = 50
    # check ai
    if ai_hp > 150:
        ai_hp = 150
    if ai_attack > 100:
        ai_attack = 100
    if ai_heal > 50:
        ai_heal = 50
    
    # +1 in round count
    round_count += 1

    # set done turn False
    player_turn_done = False
    ai_turn_done = False

    # player select action place
    print(f"Player HP = {player_hp} | AI HP = {ai_hp} | Turn {round_count}")
    print(f"Player power | Heal = {player_heal} | Attack = {player_attack}")
    print(f"Ai power     | Heal = {ai_heal} | Attack = {ai_attack}")
    print("Block Status =", player_block)
    print("\n1. Attack\n2. Block\n3. Heal\n4. Increase attack\n5. Increase heal")
    player_action = input(":")

    # player input initialize code

    # player attack code
    if (player_action == "1" or player_action == "a") and not player_turn_done:
        player_turn_done = True
        
        # ai think place 
        if not ai_block and not ai_turn_done:
            ai_turn_done = True
            ai_blck_see_player_attack = random.randint(1, 5)
            if ai_blck_see_player_attack == 1:
                ai_block_chance = random.randint(1, 4)
                if ai_block_chance != 4:
                    ai_block = True

        # ai stop thinking
        if ai_block:
            print("\nAttack blocked\n")
            ai_block = False
        else:
            print("\nAttack successful\n")
            ai_hp -= player_attack
    
    # player block code
    elif player_action == "2" or player_action == "b":
        player_turn_done = True
        player_block_chance = random.randint(1, 4)
        if player_block_chance != 4:
            print("\nYou block\n")
            player_block = True
        else:
            print("\nYou lose block\n")
            
    # player heal code
    elif (player_action == "3" or player_action == "h") and not player_turn_done:
        player_turn_done = True
        player_hp += player_heal

    # player increase attack code
    elif (player_action == "4" or player_action == "ia") and not player_turn_done:
        player_turn_done = True
        player_attack += player_attack_inc

    # player increase heal code
    elif (player_action == "5" or player_action == "ih") and not player_turn_done:
        player_turn_done = True
        player_heal += player_heal_inc

    ### ai start thinking

    # ai action when hp 40 and low
    if ai_hp <= 40 and not ai_turn_done:
        ai_turn_done = True
        ai_action_when_hp_low = random.randint(1, 2)
        if ai_action_when_hp_low == 1 and ai_block == False:
            ai_block = True
        else:        
            ai_hp += ai_heal

    # ai action for become master
    elif round_count <= 4 and not ai_turn_done:
        ai_turn_done = True
        ai_heal += ai_heal_inc

    # when ai don't know what he must doing
    elif not ai_turn_done:
        ai_action = random.randint(1, 4)
        if ai_action == 1:
            ai_turn_done = True
            if player_block:
                player_block = False
            else:
                player_hp -= ai_attack   
            
        elif ai_action == 2 and ai_hp <= 150:
            ai_turn_done = True
            ai_hp += ai_heal

        elif ai_action == 3 and not ai_block:
            ai_turn_done = True
            ai_block = True

        elif ai_action == 4:
            ai_turn_done = True
            if ai_hp >= 70 and ai_attack < 100:
                ai_attack += ai_attack_inc
            elif ai_heal < 50:
                ai_heal += ai_heal_inc
        elif ai_turn_done == False:
            ai_turn_done = True
            if player_block:
                player_block = False
            else:
                player_hp -= ai_attack  

    # End the round
    if player_hp <= 0 or round_count >= 100:
        print("You lose")
        break
    if ai_hp <= 0:
        print("You win")
        break

print("Thank for playing")