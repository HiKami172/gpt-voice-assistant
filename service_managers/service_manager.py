from abc import ABC


class ServiceManager(ABC):
    def get_manager_public_methods(self):
        user_defined_methods = []
        for method_name in dir(self):
            if method_name.startswith('_'):
                continue
            method = getattr(self, method_name)
            if callable(method) and hasattr(method, '__func__'):
                if method.__func__.__module__ == self.__class__.__module__:
                    user_defined_methods.append(method)
        return user_defined_methods
