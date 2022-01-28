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
