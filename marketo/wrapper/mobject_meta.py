class MObjectMeta:
    def __init__(self, name, description, fields):
        self.name = name
        self.description = description
        self.fields = fields

    def __str__(self):
        return "%s (%s fields)" % (self.name, len(self.fields))

    def __repr__(self):
        return self.__str__()


def bool_str_to_bool(bool_str):
    return True if bool_str == 'true' else False


def unwrap(xml):
    name = xml.find('name').text
    description = xml.find('name').text
    fields = []

    for field_el in xml.find('fieldList').findall('.//field'):
        fields.append({
           'name': field_el.find('name').text,
           'description': field_el.find('description').text,
           'sourceObject': field_el.find('sourceObject').text,
           'dataType': field_el.find('dataType').text,
           'size': field_el.find('size').text,
           'isReadonly': bool_str_to_bool(field_el.find('isReadonly').text),
           'isUpdateBlocked': bool_str_to_bool(field_el.find('isReadonly').text),
           'isName': bool_str_to_bool(field_el.find('isReadonly').text),
           'isPrimaryKey': bool_str_to_bool(field_el.find('isReadonly').text),
           'isCustom': bool_str_to_bool(field_el.find('isReadonly').text),
           'isDynamic': bool_str_to_bool(field_el.find('isReadonly').text),
           'updatedAt': field_el.find('isReadonly').text,
        })

    return MObjectMeta(name=name, description=description, fields=fields)
