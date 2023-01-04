import importlib
import inspect

def get():
    results = {}
    module = importlib.import_module('models')
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and name.lower() != 'sqlalchemy':
            results[name.lower()] = obj
    return results
    