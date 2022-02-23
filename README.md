### v0.4.3
- fixed using ***mana potion***, now players' magic attack back to previous level on next turn.
- fixed ***escape from battle***

> TODO: get rid of global variables, especially **escape from battle**



### v0.4.2
- fixed printing spells in ***Temple***. Now player can see only spells that matches his experience level

> TODO: escape from battle not working, after successful escape enemy still gets his turn and battle continues



### v0.4.1
- adding ***Chest*** class. Player now will find treasure chest in some locations

> TODO: magic attack won't back to normal level after using **mana potion**, potion works permanently 
> fix printing spells in ***Temple*** in **Town**



### v0.4.0
- battle divided into turns
- fixed bug when after searching dead enemy body started last enemy turn
- fixed issue when player didn't level up after reaching exp. level while teleporting in battle
- added ***Greater Regeneration*** potion
  
> TODO: assign enemies to regions
> change ***mana*** stat - instead of defining magic attack power, it should decrease after each spell use.
> define ***spell*** functions for casting spells during battle



### v0.3.9
- fixed bug with player max health during battle, now it reffers to player.maxhealth from Hero class instead of global variable

> TODO: when player deals critical damage to enemy, sometimes damage is negative



### v0.3.8
- fixed bug with leveling up after magic attack.

> TODO: player max health during battle is lowered to value from previous battle (160/160 instead of 160/200) 



### v0.3.7
- fixed bug with selling items in shop.
- added hero creator at game start.

> TODO: fix bug with leveling up after magic attack. Now player gets more levels than he should.



### v0.3.6
- added new item **bandage**
- added some new item effects (cure poison, cure burn, bandage)
- few minor improvements

> TODO: fix bug with selling items in shop. Items is correctly removed from inventory, but ***enumerate*** numbers of other items are wrong



### v0.3.5
- fixed ***run from battle***, now player gets to region which he has been exploring instead of **decision path** function

> TODO: fix bug with selling items in shop. Items is correctly removed from inventory, but ***enumerate*** numbers of other items are wrong



### v0.3.4
- now enemy level must match the player's level +-1

> TODO: add difficulty level at the beginning of the game. Monsters are going to be stronger and player will get less experience.
> TODO: fix bug when player doesn't die after his health is below 0, instead it's end of battle and player health less than 0



### v0.3.3
- rebuilding enemy class, now enemies will be saved in csv file with all statistics instead of randomly generated stats and names



### v0.3.2

### What works?:
- ***Temple*** in ***Town*** (hero can heal his wounds)
- fixed **leveling up**, now health is correctly increased by 10% each level.

> TODO: implement ***inn*** in ***Town*** where player can take **quests** and **rest**.
> TODO: rewrite create ***enemy functions***, add ***enemy level*** and ***specials***



### v0.3.1
- added new ***teleport scrolls*** - *Cave* and *Dungeon*
- added ***Hero Screen*** on every location options
- fixed bug - items from inventory aren't destroyed after use, it's durability goes below 0

> TODO: divide items from ***shop*** to ***blacksmith***, ***temple*** and ***medic*** - in progress



### v0.3.0
- now negative ***player state*** impacts player health on the end of the turn
- added **town scroll** item that teleports player to another location (town)

> TODO: other teleport locations, 3 maybe
> TODO: fix bug - items from inventory aren't destroyed after use, it's durability goes below 0



### v0.2.9
- fixed bug when player input in ***explore_world*** was invalid, now game is not crashing and returns 'wrong option' message

> TODO: add **medic**, **temple**, **inn** functions in ***Town***
> TODO: add **town portal scroll**, that teleports player from actual area to Town



### v0.2.8
- still implementing ***functions*** to ***explore_world*** (partially works)

#### What works?:
- explore_world works with examine every area in game. back from battle and shop to previous region also works

> TODO: add **medic**, **temple**, **inn** functions in ***Town***



### v0.2.7
- implementing ***functions*** to ***explore_world***

#### What works?:
- when player explores region and chooses to inspect it, the battle is initiated

#### What doesn't work?:
- when battle is over player gets to main menu, and when he chooses **explore world** he gets to Town instead of region he was during battle

> TODO: fix bug when battle is over - game should return to region from ***explore_world*** instead of main menu



### v0.2.6
- working on world exploration. Updating locations description
- working on player negative conditions after getting critical hit from enemy

> TODO: fix bug with leveling up, add 10% health when player level increases. Now health is always 200.



### v0.2.5

#### What works?:
- fixed bug with using **other** items, when stats wasn't reset after end of turn

#### What doesn't work?:
- player health is always 200 HP on start of battle, even after reaching new level. It should be increased each level.

> TODO:



### v0.2.4

#### What works?:
- fixed leveling up, now player gets only 2 stat points after reaching new level

#### What doesn't work?:
- player health is always 200 HP on start of battle, even after reaching new level. It should be increased each level.

> TODO: fix bug when using **other** items. Now player can use for example *for leaf clover* as many times as he wants in one battle, and stats raises each time.



### v0.2.3
- fixed player and enemy health bar length - now it's 60 '=' characters for both of them
- fixed shop bug with list indexes errors

> TODO: leveling up bug - player gets more additional points for the stats after reaching new experience levels (it should be always 2 points).
> Change player_temp_stat_boost from global to local for better memory usage



### v0.2.2
- fixed bug when player chooses not to search body of defeated enemy and is forced to fight dead enemy with negative value of *health*.
- added 2 experience points after reaching *new level*. Points are distributed to player stats
- player **inventory** is now empty at game start. Player gets more *money* and can buy selected *items* in **shop**.
- added risk of activating a trap when search of dead enemy body fails

> TODO: bug fix: when trying to use item from empty inventory causes dictionary error.



### v0.2.1
- reworked function use_item(), now the parameter with index [0] will change player stats
- added some new items

#### What works?:
- stats after using item are now increased for one turn only instead of whole battle

> TODO: stats and effects after using new items from inventowy (poison, burn)
> TODO: player will get 1 point to selected stat after **level_up()**
> TODO: fix health bars for *player* and *enemy*, make it length equal and independent of health value
> TODO: change description for each region, because it was copy/pasted
>        options in regions (search, fight, examine, etc...)



### v0.2

#### What works?:
- exploring regions

> TODO: change description for each region, because it was copy/pasted
>        options in regions (search, fight, examine, etc...)



### v0.1.9

- added module for exploring world

#### What doesn't work?:
- durability of weapon/armor isn't decreasing each turn, it decreases when item is picked from inventory

> TODO: stats and effects after using new items from inventowy (poison, burn)
 TODO: add states to states list in hero class
 TODO: add items that gives immune for poison, fire, frost...



### v0.1.8
#### What works?:
- fixed shop bug when bought item wasn't added to inventory

#### What doesn't work?:
- durability of weapon/armor isn't decreasing each turn, it decreases when item is picked from inventory

> TODO: stats and effects after using new items from inventowy (poison, burn)
 TODO: add states to states list in hero class
 TODO: add items that gives immune for poison, fire, frost...



### v0.1.75
- back to previous modules structure because of errors during modules import
#### What works?:
- battle functions
- search body after victory
#### What doesn't work?:
- error in shop after buying item



### v0.1.7
- working on shop function, still has error when importing modules



### v0.1.6

#### What works?:
- started working on shop function

> TODO: stats after using item should be increased for one turn only instead of whole battle
 TODO: doctrings and other comments - *in progress*



### Adventure Game v0.1.5

#### What works?:

- working battle system, implemented leveling up
- working item show in battle.
- working early stage of using items
- fixed *magic attack*, now enemy dies after its *health* reaches 0
- use of **item** works, **weapons** are destroyed after its **durability** reaches 0, **consumables** are destroyed after use
- stats are updated after item use
- works after forders structure rebuilt

> TODO: stats after using item should be increased for one turn only instead of whole battle
 TODO: doctrings and other comments - *in progress*
