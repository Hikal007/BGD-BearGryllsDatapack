advancement revoke @s only bgd:foods/arrow
summon arrow ~ ~2.5 ~
tellraw @s {"text": "我原本和你一样能吃，直到我的腿被射了一箭","color": "gray"}
loot give @s loot bgd:arrow
