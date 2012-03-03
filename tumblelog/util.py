def path_break(path):
    """
    Passed a string formatted like 'app.models.Model', will return a tuple of
    strings indicating the path and the local.
    """
    import_from = '.'.join(path.split('.')[:-1])
    import_name = path.split('.')[-1:][0]
    return import_from, import_name


def import_from(path):
    """
    Passed a string formatted like 'app.models.Model', will return Model (a
    local defined in app.models).
    """
    path, name = path_break(path)
    module = __import__(path, globals(), locals(), [name], -1)
    return getattr(module, name)
