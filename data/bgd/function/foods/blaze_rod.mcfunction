advancement revoke @s only bgd:foods/blaze_rod
tag @s add br
execute as @a[tag=br] at @s run setblock ~ ~ ~ fire
#playsound minecraft:item.firecharge.use player @s ~ ~ ~ 0.5 0.5 1
scoreboard players add br bgd 1
schedule function bgd:foods/blaze_rod 10t