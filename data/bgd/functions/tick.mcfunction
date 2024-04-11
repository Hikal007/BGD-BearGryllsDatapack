#雕纹书架
execute if score cb bgd matches 30.. run schedule clear bgd:foods/chiseled_bookshelf
execute if score cb bgd matches 30.. run tag @a[tag=cb] remove cb
execute if score cb bgd matches 30.. run scoreboard players reset cb bgd

#哭泣黑曜石
execute if score co bgd matches 70.. run schedule clear bgd:foods/crying_obsidian
execute if score co bgd matches 70.. run scoreboard players reset co bgd