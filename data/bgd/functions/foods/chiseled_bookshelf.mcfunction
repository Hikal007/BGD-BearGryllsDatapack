advancement revoke @s only bgd:foods/chiseled_bookshelf
tag @s add cb
execute as @a[tag=cb] at @s run effect give @e[distance=0..25] glowing 3 0
scoreboard players add cb bgd 5
schedule function bgd:foods/chiseled_bookshelf 5s