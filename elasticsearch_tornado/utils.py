import collections
import json

def serialize(obj):
    # first check if it's dictionary like
    if isinstance(obj, collections.Mapping):
        return "%s\n" % json.dumps(obj)
    elif isinstance(obj, collections.Iterable):
        return "\n".join( json.dumps(x) for x in obj ) + '\n'
