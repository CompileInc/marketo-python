
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
import sync_lead


def wrap(data_list, dedup_enabled=True):
    xml_str = ''
    dedup_enabled = 'true' if dedup_enabled else 'false'
    for lead_data in data_list:
        xml_str += sync_lead._wrap(lead_data[0], lead_data[1])
    return '<ns1:paramsSyncMultipleLeads><leadRecordList>' + xml_str + '</leadRecordList><dedupEnabled>' + dedup_enabled + '</dedupEnabled></ns1:paramsSyncMultipleLeads>'


def unwrap(response):
    root = ET.fromstring(response.text.encode('utf8'))
    r = {}
    for status_xml in root.findall('.//syncStatus'):
        r['lead_id'] = int(status_xml.find('leadId').text)
        r['status'] = status_xml.find('status').text
        r['error'] = status_xml.find('error').text
    return r
