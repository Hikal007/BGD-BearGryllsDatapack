tellraw @s {"text": "加载成功"}
playsound entity.experience_orb.pickup player @a ~ ~ ~ 1 1 1
advancement revoke @a everything
advancement grant @a only bgd:foods/root
scoreboard objectives add cb dummy
scoreboard players set cb cb 0