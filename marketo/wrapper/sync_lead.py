
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
import lead_record


def _wrap(email=None, attributes=None):
    attr = ''
    for i in attributes:
        attr += '<attribute>' \
            '<attrName>' + i[0] + '</attrName>' \
            '<attrType>' + i[1] + '</attrType>' \
            '<attrValue>' + escape(str(i[2])) + '</attrValue>' \
            '</attribute>'

    return(
        '<leadRecord>' +
        '<Email>' + email + '</Email>' +
        '<leadAttributeList>' + attr + '</leadAttributeList>' +
        '</leadRecord>' +
        '<returnLead>true</returnLead>' +
        '<marketoCookie></marketoCookie>'
    )


def wrap(email=None, attributes=None):
    return '<mkt:paramsSyncLead>' + _wrap(email, attributes) + '</mkt:paramsSyncLead>'


def unwrap(response):
    root = ET.fromstring(response.text.encode('utf8'))
    lead_record_xml = root.find('.//leadRecord')
    return lead_record.unwrap(lead_record_xml)
