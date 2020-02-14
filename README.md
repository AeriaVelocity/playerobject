# Player object for game
[![Run on Repl.it](https://repl.it/badge/github/CutieGorlAstrid/playerobject)](https://repl.it/github/CutieGorlAstrid/playerobject)

The Python file `PlayerModule.py` in this repo contains the underlying code for a W.I.P. game. This repo will eventually grow to form a whole game, but for now it just holds my early code.

## Prerequisites

### Running the code online
You can use [repl.it](https://repl.it) via the button above to run the code without downloading anything. Feel free to experiment with `DefaultPlayer.py`.

## Running the code on your computer
If cloning/downloading the repo to your computer, you'll need at least [Python 3.6](https://www.python.org/downloads/release/python-3610/), as `PlayerModule.py` uses [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings). The [latest version](https://www.python.org/downloads/) of Python is recommended.

## How to use the module
To create a new player, simply type 
```
import PlayerModule
Player = PlayerModule.PlayerObject(PlayerName, PlayerHealth, PlayerAttack, GameName)
```
### Keywords
`PlayerName` - The name of the player. Will be used in most dialogues.

`PlayerHealth`- The maximum health of the player.

`PlayerAttack` - The base attack strength of the player. Actual attack strength is determined by an RNG value ranging from base attack to double base attack. For example, if base attack is 15, a full-strength attack would be 30.

`GameName` - The name of the game to be printed upon creating a new player in the format `"Welcome to {GameName}, {PlayerName}!"`.

> The above function will later be included in a `GameProperties` object, which doesn't yet exist

The PlayerObject object has three attributes - `Attack()`, `Damage(InitialDamageAmount)` and `Heal(HealAmount)`

`Player.Attack()` - Performs an attack as described earlier. Only prints out how much damage is dealt as of now, and does not damage any enemies, as there are none.

`Player.Damage(InitialDamageAmount)` - This works the same as `Player.Attack()`, but instead of dealing damage to any enemies, it deals damage to the player. Unlike the aforementioned `Player.Attack()`'s attack points, `Player.Damage()`'s `InitialDamageAmount` can be tripled.

`Player.Heal(HealAmount)` - Simply heals the player by the specified amount. If `HealAmount` is greater than or heals to a value greater than the player's max health, it sets the player's current health to max.

## `DefaultPlayer.py`

`DefaultPlayer.py` is a separate Python file in this repo that is used as an example of how `PlayerModule.py` can be used.
