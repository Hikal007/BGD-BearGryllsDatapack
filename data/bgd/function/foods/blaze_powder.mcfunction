advancement revoke @s only bgd:foods/blaze_powder
tag @s add bp
execute as @a[tag=bp] at @s run setblock ~ ~ ~ fire
#playsound minecraft:item.firecharge.use player @s ~ ~ ~ 0.5 0.5 1
scoreboard players add bp bgd 1
schedule function bgd:foods/blaze_powder 10t