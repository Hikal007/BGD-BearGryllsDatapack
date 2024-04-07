tellraw @s {"text": "加载成功"}
playsound entity.experience_orb.pickup player @a ~ ~ ~ 1 1 1
advancement revoke @a everything
advancement grant @a only gbd:foods/root