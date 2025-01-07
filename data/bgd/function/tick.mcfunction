#雕纹书架
execute if score cb bgd matches 31.. run schedule clear bgd:foods/chiseled_bookshelf
execute if score cb bgd matches 31.. run tag @a[tag=cb] remove cb
execute if score cb bgd matches 31.. run scoreboard players reset cb bgd

#哭泣黑曜石
execute if score co bgd matches 70.. run schedule clear bgd:foods/crying_obsidian
execute if score co bgd matches 70.. run scoreboard players reset co bgd

#火焰弹
execute if score fc bgd matches 31.. run schedule clear bgd:foods/fire_charge
execute if score fc bgd matches 31.. run tag @a[tag=fc] remove fc
execute if score fc bgd matches 31.. run scoreboard players reset fc bgd

#打火石
execute if score fs bgd matches 16.. run schedule clear bgd:foods/flint_and_steel
execute if score fs bgd matches 16.. run tag @a[tag=fs] remove fs
execute if score fs bgd matches 16.. run scoreboard players reset fs bgd

#烈焰棒
execute if score bp bgd matches 32.. run schedule clear bgd:foods/blaze_powder
execute if score bp bgd matches 32.. run tag @a[tag=bp] remove bp
execute if score bp bgd matches 32.. run scoreboard players reset bp bgd

#烈焰粉
execute if score br bgd matches 42.. run schedule clear bgd:foods/blaze_rod
execute if score br bgd matches 42.. run tag @a[tag=br] remove br
execute if score br bgd matches 42.. run scoreboard players reset br bgd

#兔子脚
execute as @a[scores={bgd.rabbit.dead=1..}] at @s run scoreboard players reset @s bgd.rabbit
execute as @a[scores={bgd.rabbit.dead=1..}] at @s run scoreboard players reset @s bgd.rabbit.dead

#成就
execute as @a[advancements={bgd:display/flint_and_steel_display=true,bgd:display/fire_charge_display=true,bgd:display/blaze_rod_display=true,bgd:display/blaze_powder_display=true},tag=!fire] at @s run function bgd:display/fire
execute as @a[tag=fire,predicate=bgd:fire] at @s run effect give @s fire_resistance infinite

#交互物品/掉落实体
#龙蛋
execute as @a[tag=!d_egg] at @s if items entity @s container.* minecraft:dragon_egg[!minecraft:food={nutrition:4,saturation:2,can_always_eat:true,effects:[{effect:{id:"strength",duration:2400}}]}] run function bgd:foods/fix/dragon_egg
execute as @a[tag=d_egg] at @s if items entity @s container.* minecraft:dragon_egg[minecraft:food={nutrition:4,saturation:2,can_always_eat:true,effects:[{effect:{id:"strength",duration:2400}}]}] run tag @s remove d_egg

execute if score ed bgd matches 1..1 run schedule clear bgd:foods/fix/dragon_egg_c
execute if score ed bgd matches 1..1 run scoreboard players set ed bgd 0
execute if score ed bgd matches 1..1 at @e[tag=ender_drgon] run summon item ~ ~1 ~ {Item:{id:"minecraft:ender_pearl"}}
execute if score ed bgd matches 1..1 at @e[tag=ender_drgon] run summon item ~ ~1 ~ {Item:{id:"minecraft:ender_pearl"}}