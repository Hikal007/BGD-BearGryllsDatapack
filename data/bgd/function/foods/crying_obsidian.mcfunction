advancement revoke @s only bgd:foods/crying_obsidian
scoreboard players add co bgd 10
weather thunder 10s
execute if score co bgd matches 10..10 at @a run summon lightning_bolt ~4 ~ ~-1
execute if score co bgd matches 20..20 at @a run summon lightning_bolt ~-1 ~ ~-5
execute if score co bgd matches 30..30 at @a run summon lightning_bolt ~1 ~ ~3
execute if score co bgd matches 40..40 at @a run summon lightning_bolt ~1 ~ ~-5
execute if score co bgd matches 50..50 at @a run summon lightning_bolt ~-4 ~ ~-1
execute if score co bgd matches 60..60 at @a run summon lightning_bolt ~1 ~ ~-5
schedule function bgd:foods/crying_obsidian 10s