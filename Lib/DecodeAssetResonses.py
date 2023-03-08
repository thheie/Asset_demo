def decodeAssetObjectTypeAttrib(jsondata):
    objecttypeAttribs = {}
    for attribs in jsondata:
        id = attribs['id']
        name = attribs['name']
        objecttypeAttribs[name]=id
    return objecttypeAttribs