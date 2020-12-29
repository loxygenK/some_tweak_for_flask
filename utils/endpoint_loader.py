from utils.submodule_worker import import_submodules


def load_endpoints():
    import_submodules("controller.endpoint")