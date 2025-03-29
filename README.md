# Variable-Battle Game: Enjoy Playing!

- To start the game, run the file `vbm.py`, which stands for "Variable Battle Main."

- Explanation of existing files, constants, and game rules.

## Explanation of Existing Files

### `vba.py` (decodes to "Variable Battle Actions")
- The main file where all the game functions are defined.

### `vbc` (decodes to "Variable Battle Core")
- This file contains definitions such as:
  - `show_display`: Displays the current game situation.
  - `cat_limits`: Prevents exceeding preset limits.
  - `check_end_round`: Checks if the player or bot has died or if the round limit has been reached, determining whether the game continues or stops because the player has lost.

### `vba` (decodes to "Variable Battle Actions")
- This file contains functions related to managing variable actions, such as:

#### Functions for the Player:
- `player_attack_def`: Used for attacking the bot.
- `player_heal_def`: Used for healing the player.
- `player_block_def`: Activates a block for the player.
- `player_increase_attack`: Increases the player's attack.
- `player_increase_heal`: Increases the player's healing ability.

#### Functions for the Bot:
- `bot_attack_def`: Used for the bot to attack the player.
- `bot_heal_def`: Used for healing the bot.
- `bot_block_def`: Activates a block for the bot.
- `bot_increase_attack`: Increases the bot's attack.
- `bot_increase_heal`: Increases the bot's healing ability.

### `vbab` (decodes to "Variable Battle Bot Action")
- This file is used to select the bot's actions and includes the function:
  - `bot_select_action`: Determines the bot's actions during a turn.

## Constant Definitions

- `ROUND_COUNT_LIMITS = 100`: Sets the maximum number of rounds in a match.
- `PLAYER_DEAD_HP = 0`: Defines the player's death condition.
- `BOT_DEAD_HP = 0`: Defines the bot's death condition.
- `PLAYER_ATTACK_INC = 5`: Specifies the rate at which the player's attack increases.
- `PLAYER_HEAL_INC = 5`: Specifies the rate at which the player's healing ability increases.
- `BOT_ATTACK_INC = 5`: Specifies the rate at which the bot's attack increases.
- `BOT_HEAL_INC = 5`: Specifies the rate at which the bot's healing ability increases.

## Rules

- You can attack by entering `1` or `a`. If the bot is blocking, the attack is blocked, and the bot takes no damage. The maximum attack damage is `50`. You can also increase your attack.
- You can heal by entering `2` or `h`. The maximum health is `150`.
- You can block by entering `3` or `b`. If the block is active, damage from the bot is reduced.
- You can increase your attack by entering `4` or `ia`. The maximum attack value is `50`.
- You can increase your healing ability by entering `5` or `ih`. The maximum healing value is `50`.
- To win, you must defeat the bot by reducing its health below `0`. If the bot's health is less than `0`, you win.
- If the round count exceeds `100`, you lose the game.
- If your health drops below `0`, you lose the game.
