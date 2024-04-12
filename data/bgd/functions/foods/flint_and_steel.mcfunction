advancement revoke @s only bgd:foods/flint_and_steel
tag @s add fs
execute as @a[tag=fs] at @s run setblock ~ ~ ~ fire
#playsound minecraft:item.firecharge.use player @s ~ ~ ~ 0.5 0.5 1
scoreboard players add fs bgd 1
schedule function bgd:foods/flint_and_steel 1s