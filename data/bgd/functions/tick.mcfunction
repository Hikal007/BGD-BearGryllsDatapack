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