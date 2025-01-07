advancement revoke @s only bgd:foods/fire_charge
tag @s add fc
execute as @a[tag=fc] at @s run setblock ~ ~ ~ fire
#playsound minecraft:item.firecharge.use player @s ~ ~ ~ 0.5 0.5 1
scoreboard players add fc bgd 1
schedule function bgd:foods/fire_charge 1s