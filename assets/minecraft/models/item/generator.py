import json


materials = ['wooden', 'stone', 'iron', 'golden', 'diamond', 'netherite']
tools = ['axe', 'hoe', 'pickaxe', 'shovel', 'sword']
names = []
for t in tools:
    names.extend([m+'_'+t for m in materials])

for name in names:
    with open(name + '.json', 'w') as file:
        template = {
            "parent": "minecraft:item/handheld",
            "textures": {
                "layer0": f"minecraft:item/{name}"
            },
            "overrides": [
                {
                    "predicate": {
                        "custom_model_data": 74201
                    },
                    "model": "tech:item/druid_staff"
                }
            ]
        }
        json.dump(template, file, indent=4)