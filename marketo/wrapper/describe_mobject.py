
import xml.etree.ElementTree as ET
import mobject_meta


def wrap(mobject_type):
    return (
        '<ns1:paramsDescribeMObject>' +
            '<objectName>' + mobject_type + '</objectName>' +
        '</ns1:paramsDescribeMObject>')


def unwrap(response):
    root = ET.fromstring(response.text)
    xml_el = root.find('.//metadata')
    return mobject_meta.unwrap(xml_el)
