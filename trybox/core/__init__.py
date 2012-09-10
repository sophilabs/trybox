from context import Context

cls_cache = {}
def serialize(obj):

    def _attrs(cls):
        if cls not in cls_cache:
            sclass, sfields = getattr(cls, 'serialize', (None, [],))
            cls_cache[cls] = sfields + \
                             sum([_attrs(bcls) for bcls in cls.__bases__], [])
        return cls_cache[cls]

    def _get(f):
        objn = getattr(obj, f)
        if isinstance(objn, (list, tuple)):
            objn = [serialize(objnc) for objnc in objn]
        return objn

    return dict([(f, _get(f)) for f in _attrs(obj.__class__)] + \
                [('class', obj.__class__.serialize[0])])