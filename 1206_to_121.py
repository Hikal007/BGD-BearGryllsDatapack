import os
import json
from datetime import datetime
import csv

datapack_path = r'1.20.5-1.20.6.BGD-v1.0.2-Beta\data\minecraft'
minecraft_path = r'data\minecraft'

datapack_recipes_path = r'1.20.5-1.20.6.BGD-v1.0.2-Beta\data\minecraft\recipes'
minecraft_recipes_path = r'data\minecraft\recipe'

datapack_loot_tables_path = r'1.20.5-1.20.6.BGD-v1.0.2-Beta\data\minecraft\loot_tables'
minecraft_loot_tables_path = r'data\minecraft\loot_table'


"""# 自定义except--→在文件中未找到对应的function键
class NoFunctionFind(Exception):
    pass


# 对比类
class OrSimilar:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.id != other.id:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.id)"""


# 获取当前时间
def now_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 查找1.21未被修改的文件并存到directory.log
def find():
    os.remove('directory.log')
    files_to_keep = set()
    for root, _, files in os.walk(datapack_path):
        files_to_keep.update(files)

    for root, _, files in os.walk(minecraft_path):
        for file in files:
            if file in files_to_keep:
                try:
                    # 把修改过的删除
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Failed to delete {os.path.join(root, file)}: {e}")

    # 把没修改过的放到directory.log
    for root, _, files in os.walk(minecraft_path):
        for file in files:
            with open('directory.log', 'a', encoding='utf-8') as f:
                f.write(f'{os.path.join(root, file)}\n')


# 更新1.20.6recipe的格式成1.21
def update_1_20_6_recipe_json():
    components = {"components": {}}
    for filename in os.listdir(datapack_recipes_path):
        if filename.endswith('.json'):
            file_path = os.path.join(datapack_recipes_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    if 'functions' in data['result']:
                        for function in data['result']['functions']:
                            if function['function'] == 'minecraft:set_components':
                                components['components'] = function['components']
                                break
                        del data['result']['functions']
                    data['result'].update(components)
                    with open(file_path, 'w', encoding='utf-8') as file1:
                        json.dump(data, file1, indent=4)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file {file_path}: {e}")


# 更新1.20.6loot_tables的格式成1.21
def update_1_20_6_loot_tables_enchantments():
    log_file = 'update_loot_tables.log'
    os.remove(log_file)
    with open(log_file, 'a', encoding='utf-8') as f1:
        for root, _, files in os.walk(datapack_loot_tables_path):
            for f in files:
                if f.endswith('.json'):
                    file_path = os.path.join(root, f)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            data = json.load(file)
                            if 'pools' in data:
                                for pool in data['pools']:
                                    for entry in pool['entries']:
                                        if 'functions' in entry:
                                            for function in entry['functions']:
                                                # 移除modifiers的name键
                                                if function['function'] == 'minecraft:set_attributes':
                                                    for attr in function['modifiers']:
                                                        del attr['name']

                                                # 移除minecraft:enchant_with_levels的treasure键
                                                # function添加minecraft:enchant_randomly字典
                                                elif function['function'] == 'minecraft:enchant_with_levels':
                                                    del function['treasure']
                                                    entry['functions'].append(
                                                        {"function": "minecraft:enchant_randomly"})

                                                # 将enchantments提取并删除赋值给新的键options
                                                elif function['function'] == 'minecraft:enchant_randomly':
                                                    if 'enchantments' in function:
                                                        function['options'] = function.pop('enchantments')
                                                    else:
                                                        # raise NoFunctionFind()
                                                        f1.write(
                                                            f'[{now_time()}]{file_path}的{function}未找到enchantments键\n')
                                        else:
                                            f1.write(
                                                f'[{now_time()}]{file_path}的{entry}未找到entry键\n')
                            else:
                                f1.write(
                                    f'[{now_time()}]{file_path}未找到pools\n')
                        with open(file_path, 'w', encoding='utf-8') as file1:
                            json.dump(data, file1, indent=4)
                        f1.write(f'[{now_time()}]{file_path}: 已更新\n')
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in file {file_path}: {e}\n")
                        f1.write(f"[{now_time()}]Error decoding JSON in file {file_path}: {e}\n")

"""
# 对1.21最新的recipe文件进行修改重写
# def write_recipe_food_components():
#     # 读取每个json result键的值并保存到datas.csv文件下
#     datas = []
#     # 用于存储已经遇到的id，以避免重复添加
#     seen_ids = set()
#     for root, dirs, files in os.walk(minecraft_recipes_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             with open(file_path, 'r', newline='', encoding='utf-8') as f:
#                 data = json.load(f)
#                 if 'result' in data and 'id' in data['result']:
#                     recipe_id = data['result']['id']
#                     if recipe_id not in seen_ids:  # 检查id是否已存在
#                         seen_ids.add(recipe_id)  # 添加新id到集合中
#                         datas.append({'id': recipe_id})
#                     # for d in data['result']:
#                     #     if OrSimilar(d) == OrSimilar(temp_dict):
#                     #         continue
#                     #     datas.append(temp_dict)
#     # 保存到datas.csv文件下
#     with open('datas.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=['id'])
#         writer.writeheader()
#         writer.writerows(datas)
#
#     # datas文件和components_datas按照id合并并移除空值，
#     # 或者直接使用components_datas文件匹配每个json result的id值进行components添加
#     with open('components_datas.csv', 'r', newline='', encoding='utf-8') as f1,\
#             open('write_recipe_food.log', 'w', newline='',encoding='utf-8') as log:
#         reader = csv.DictReader(f1, delimiter=';')
#         for row in reader:
#             # 清理components_datas中components为空的行
#             if row['components'] is not None:
#                 components = row['components']
#                 try:
#                     components_dict = {'components': json.loads(components)}
#                 except json.decoder.JSONDecodeError as e:
#                     log.write(f'[{now_time()}]JsonDecodeError--{e}\n')
#             # 按照id遍历文件添加components
#             for root, dirs, files in os.walk(minecraft_recipes_path):
#                 for file in files:
#                     file_path = os.path.join(root, file)
#                     with open(file_path, 'r', newline='', encoding='utf-8') as f:
#                         data = json.load(f)
#                         try:
#                             if data['result']['id'] == row['id']:
#                                 data['result'].update(components_dict)
#                         except KeyError as e:
#                             log.write(f'[{now_time()}]Error {file_path} 未找到{e}键\n')
#                     with open(file_path, 'w', encoding='utf-8') as f:
#                         json.dump(data, f,indent=4)
#                         log.write(f'[{now_time()}]{file_path}已成功写入\n')
"""


# 读取每个json result键的值并保存到datas.csv文件下
def extract_recipe_ids(path):
    datas = []
    seen_ids = set()
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if 'result' in data and 'id' in data['result']:
                        recipe_id = data['result']['id']
                        if recipe_id not in seen_ids:
                            seen_ids.add(recipe_id)
                            datas.append({'id': recipe_id})
            except Exception as e:
                print(f'Error 读错误   {file_path}: {e}')
    return datas


# 根据components_datas.csv筛选过滤写入文件
def update_recipe_with_components(recipes_path, components_file, log_file):
    try:
        os.remove(log_file)
    except FileNotFoundError:
        pass
    components_dict = {}
    with open(components_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if row['components']:
                try:
                    components_dict[row['id']] = {'components':json.loads(row['components'])}
                except json.JSONDecodeError as e:
                    with open(log_file, 'a', encoding='utf-8') as log:
                        log.write(f'[{now_time()}] JsonDecodeError -- {row['id']} -- {e}\n')

    for root, dirs, files in os.walk(recipes_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if 'result' in data and 'id' in data['result']:
                        recipe_id = data['result']['id']
                        if recipe_id in components_dict:
                            data['result'].update(components_dict[recipe_id])
                            with open(file_path, 'w', encoding='utf-8') as f:
                                json.dump(data, f, indent=4)
                            with open(log_file, 'a', encoding='utf-8') as log:
                                log.write(f'[{now_time()}] {file_path} 已更新。\n')
            except Exception as e:
                with open(log_file, 'a', encoding='utf-8') as log:
                    log.write(f'[{now_time()}] Error 读/写错误 {file_path}: {e}\n')


if __name__ == '__main__':
    find()
    # update_1_20_6_recipe_json()
    # update_1_20_6_loot_tables_enchantments()
    # recipe_ids = extract_recipe_ids(minecraft_recipes_path)
    update_recipe_with_components(minecraft_recipes_path, 'components_datas.csv', 'write_recipe_food.log')
