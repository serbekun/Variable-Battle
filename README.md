# Variable-Battle game enjoy playing!

- for start game start file `vbm.py` encode "variable battle main"

- 1) explanation what doing exist file
- 2) constant meaning
- 3) game rule 


## exist file explanation what doing
### `vba.py` decode "variable battle main" 
- main file where does the function come from
### `vbc` decode "variable battle core"
- in this file exist def such as
- `show_display` use for show all info about now situashon
- `cat_limits` used to avoid exceeding limits
- `check_end_round` used to chek died player or bot and last round for know continue or stop game beocose player lose
### `vba` decode "variable battle actions"
- this file exist defs fore commit variables actions such as
##### defs for player
- `player_attack_def` used for attack bot from player
- `plaer_heal_def` used for heal player
- `player_block_def` used for activate block for player
- `player_increase_attack` used for increase player attack
- `player_increase_heal` used for increase player heal
##### defs for bot
- `bot_attack_def` used for attack bot from bot
- `bot_heal_def` used for heal bot
- `bot_block_def` used for activate block for bot
- `bot_increase_attack` used for increase bot attack
- `bot_increase_heal` used for increase bot heal
### `vbab` decode "variable battle bot action"
- this file need for select bot action
- this file exist def
- `bot_select_action` used for select bot actions

- ## constant meaning
- `ROUND_COUNT_LIMITS = 100` select last round in match
- `PLAYER_DEAD_HP = 0` select player dead zone
- `BOT_DEAD_HP = 0` too select bot dead zone
- `PLAYER_ATTACK_INC` = 5 sellected player attack increase speed
- `PLAYER_HEAL_INC` = 5 sellected player heal increase speed
- `BOT_ATTACK_INC` = 5 sellected bot attack increase speed
- `BOT_HEAL_INC` = 5 sellected bot heal increase speed
  
## rules

- you can attack with type `1` or `a` if bot exist block attack block and bot not get damage max damege which can used `50` you also can increase attack
- you can heal with type `2` or `h` max health `150`
- you can blcok with type `3` or `b` if block exist damege from bot dimese
- you can increase attack with type `4` of `ia` max attack `50`
- you can increase heal with type `5` `ih` max heal `50`
- for win you must kill bot if bot health less `0` you win
- if round count more `100` you lose game
- if your hp less `0` you lose game
