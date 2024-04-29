#初始化
#Made by Big_Jls、Hikal007、WhiteFox_rua（排名不分先后）
#tellraw @a[tag=admin] {"text": "加载成功"}
playsound entity.experience_orb.pickup player @a ~ ~ ~ 1 1 1
advancement revoke @a from bgd:foods/root
advancement grant @a only bgd:foods/root
difficulty hard
scoreboard objectives add bgd dummy
recipe take @a bgd:bedrock

#雕纹书架
scoreboard players set cb bgd 0

#哭泣黑曜石
scoreboard players set co bgd 0

#火焰弹
scoreboard players set fc bgd 0

#打火石
scoreboard players set fs bgd 0

#烈焰棒
scoreboard players set br bgd 0

#烈焰粉
scoreboard players set bp bgd 0

#兔子脚
scoreboard objectives add bgd.rabbit dummy
scoreboard objectives add bgd.rabbit.dead deathCount
scoreboard players reset @a bgd.rabbit
scoreboard players reset @a bgd.rabbit.dead

#龙蛋
scoreboard players set ed bgd 0