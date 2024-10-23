import json
import os
path = r'C:\Users\uziem\AppData\Roaming\com.modrinth.theseus\profiles\Creation\saves\Creation Origins\datapacks\Creation\data\tech\advancements\kill_origin'
for directory in os.listdir(path):
    if directory[-5:] == '.json':
        name = directory[:-5]
        with open(path+os.sep+directory, encoding='utf-8') as file:
            data = json.loads(file.read())
            title = data['display']['title']
            description = data['display']['description']
            print(f'"creation.advancements.kill.{name}.title": "{title}",')
            print(f'"creation.advancements.kill.{name}.description": "{description}",')