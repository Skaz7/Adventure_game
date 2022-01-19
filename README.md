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
- fixed **magic attack**, now enemy dies after its *health* reaches 0
- use of **item** works, **weapons** are destroyed after its *durability* reaches 0, **consumables** are destroyed after use
- stats are updated after item use
- works after forders structure rebuilt

> TODO: stats after using item should be increased for one turn only instead of whole battle
 TODO: doctrings and other comments - *in progress*