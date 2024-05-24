import pygame 
import json
import os
# Project modules
from ships import components

class Registry:
    def  __init__(self, name, type_holder):
        self.name = name
        self.type_holder = type_holder
        self.values = {} # Holding in memory, maybe make more optimized

    # Create seperated loader defs for all registries containing there class?


class RegistryAccessor:
    def  __init__(self):
        pass



class Loader:
    def  __init__(self):
        pass
    
    
    def load_components(self, path, component_class):
        assert issubclass(component_class, components.Component)
        #assert component_class is components.Component
        objs = self._import_obj_files(path)
        for obj in objs: 
            #print(f'Object name: {obj["name"]}')
            new_obj = component_class(obj)
            print(new_obj.stats)
            
    
    
    def _import_obj_files(self, path):
        # Get files
        files = self._walk_and_find_files(path)
        objs = []
        for filename in files:
            full_path = f'./{filename}'
            with open(full_path, 'r') as file:
                json_object = json.loads(file.read())     
                objs.append(json_object)
        return objs

    def _walk_and_find_files(self, path):
        files = []
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if filename.endswith(".json"):
                    #print(f'Dirpath: {dirpath}')
                    #print(f'Dirnames: {dirnames}')
                    #print(f'Found file {filename}')
                    full_path = f'{dirpath}/{filename}'
                    files.append(full_path)
        return files