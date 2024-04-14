advancement revoke @s only bgd:foods/arrow
tellraw @s {"text": "我原本和你一样能吃，直到我的腿被射了一箭","color": "gray"}
loot replace entity @s armor.legs loot bgd:arrow
