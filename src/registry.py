import pygame 
import json
import os
from typing import Union, Self, Optional
# Project modules
from ships import components, ship_templates
from manufacturer import manufacturers

class RegistryKeys:
    def __init__():
        self.components = []


# Loader class for walking through files
class Loader:
    def  __init__(self):
        pass
    
    # Import a single obj from known path
    def _import_single_obj(self, path: str):
        obj = {}
        with open(path, 'r') as file:
            json_object = json.loads(file.read())     
            obj = json_object
        return obj
    
    # Import all objs from the data directory
    def _import_obj_files(self, path: str):
        # Get files
        files = self._walk_and_find_files(path)
        objs = []
        for filename in files:
            full_path = f'./{filename}'
            with open(full_path, 'r') as file:
                json_object = json.loads(file.read())     
                objs.append(json_object)
        return objs

    # Walk through all files in the data directory 
    def _walk_and_find_files(self, path: str) -> list[str]:
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


# Basic Holder of data members
class Registry:
    def  __init__(self, name: str, key_id: str, location: str, data_type):
        self.name = name
        self.id = key_id
        self.location = location
        self.data_type = data_type
        # Holding in memory, maybe make more optimized
        self.members = {} 

    def _register_members(self, loaded_objs):
        for obj in loaded_objs:
            val = self.data_type(obj)
            key_id = obj['id'] # Must have id
            self.members[key_id] = val

# ComplexRegistry -> Holds multiple registries

# Main entry point for accesing data
class RegistryAccessor:
    def  __init__(self):
        root = f'data'
        # Defined Member Fields
        self.components = Registry('Components', 'components', f'{root}/ship/components', components.Component)
        self.hull_templates = Registry('Hull Templates', 'hull_templates', f'{root}/ship/hull_templates', ship_templates.HullTemplate)
        self.manufacturers = Registry('Components', 'components', f'{root}/manufacturer', manufacturers.Manufacturer)
        
    def _register_all(self, loader: Loader):
        registries = [self.components, self.hull_templates, self.manufacturers]
        # register all
        for registry in registries:
            members = loader._import_obj_files(registry.location)
            registry._register_members(members)

