import json


def load_fixture(fixture_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            with open(fixture_name, "r") as doc_for_test:
                fixture_data = json.load(doc_for_test)
            return func(self, fixture_data, *args, **kwargs)

        return wrapper

    return decorator
