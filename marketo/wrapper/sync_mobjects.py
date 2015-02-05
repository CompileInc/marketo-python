import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape


def wrap_one(mobject_type, id=None, attributes=None, attr_type=None, object_associations=None):
    attr = ''
    for i in attributes:
        attr += '' +\
            '<attrib>' +\
                '<name>' + i[0] + '</name>' +\
                '<value>' + escape(str(i[1])) + '</value>' +\
            '</attrib>'

    if id is None:
        id_section = ''
    else:
        id_section = "<id>" + str(id) + "</id>"

    if attr_type is None:
        attr_type_section = ''
    else:
        attr_type_section = "<attrType>" + attr_type + "</attrType>"

    if object_associations is None:
        object_association_list_section = ''
    else:
        for object_association_data in object_associations:
            object_association_list_section = ''
            if object_association_data.get('id') is None:
                object_association_id_section = ''
            else:
                object_association_id_section = '<id>' + str(object_association_data['id']) + '</id>'

            if object_association_data.get('external_key') is None:
                object_association_external_key_section = ''
            else:
                object_association_external_key_section = '' +\
                    '<externalKey>' +\
                    '<name>' + object_association_data['external_key']['name'] + '</name>' +\
                    '<value>' + object_association_data['external_key']['value'] + '</value>' +\
                    '</externalKey>'

            object_association_list_section += '' +\
                '<mObjAssociation>' + \
                    '<mObjType>' + object_association_data['mobject_type'] + '</mObjType>' +\
                     object_association_id_section +\
                     object_association_external_key_section +\
                '</mObjAssociation>'
        object_association_list_section = '<mObjAssociationList>' + object_association_list_section + '</mObjAssociationList>'

    return (
        '<mObject>' +
            '<type>' + mobject_type + '</type>' +
            id_section +
            '<typeAttribList>' +
                '<typeAttrib>' +
                    attr_type_section +
                    '<attrList>' + attr + '</attrList>' +
                '</typeAttrib>' +
            '</typeAttribList>' +
            object_association_list_section +
        '</mObject>'
    )


def wrap(mobject_type, data_list):
    mobject_list_section = ''
    for mobject_dict in data_list:
        mobject_list_section += wrap_one(mobject_type=mobject_type, **mobject_dict)

    return (
        '<ns1:paramsSyncMObjects>' +
            '<mObjectList>' + mobject_list_section + '</mObjectList>' +
            '<operation>UPSERT</operation>' +
        '</ns1:paramsSyncMObjects>'
    )
