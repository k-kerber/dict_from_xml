from json import dumps
import pytest
from time import time_ns
from dict_from_xml import from_file, from_string


@pytest.fixture
def test_json_output():
    return """{"{adobe:ns:meta/}xmptk": "XMP toolkit 2.9.1-13, framewo rk 1.6", "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF": {"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description": [{"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about": "", "{http://ns.adobe.com/xap/1.0/}ModifyDate": "2024-12-09T21:07:26+00:00", "{http://ns.adobe.com/xap/1.0/}CreateDate": "2010-01-29T12:18:08-08:00", "{http://ns.adobe.com/xap/1.0/}CreatorTool": "OCRmyPDF 16.6.2 / Tesseract OCR-hOCR 5.5.0"}, {"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about": "", "{http://purl.org/dc/elements/1.1/}format": "application/pdf", "{http://purl.org/dc/elements/1.1/}title": {"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt": {"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li": {"{http://www.w3.org/XML/1998/namespace}lang": "x-default"}}}, "{http://purl.org/dc/elements/1.1/}creator": {"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq": {"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li": "steve"}}}]}}"""


@pytest.fixture
def test_xml_text():
    return """<?xpacket begin="\ufeff" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP toolkit 2.9.1-13, framewo
rk 1.6">\n<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:iX="http://ns.adobe.com/iX/1.0/">\n<rdf:Description xmlns:pdf="http://ns.adobe.com/pdf/1.3/" rdf:about="" pdf:Producer="pikepdf 9.4.2"/>\n<rdf:Description xmlns:xmp="http://ns.adobe.com/xap/1.0/" rdf:about=""><xmp:ModifyDate>2024-12-09T21:07:26+00:00</xmp:ModifyDate>\n<xmp:CreateDate>2010-01-29T12:18:08-08:00</xmp:CreateDate>\n<xmp:CreatorTool>OCRmyPDF 16.6.2 / Tesseract OCR-hOCR 5.5.0</xmp:CreatorTool></rdf:Description>\n<rdf:Description xmlns:xapMM="http://ns.adobe.com/xap/1.0/mm/" rdf:about="" xapMM:DocumentID="uuid:22828538-ee8e-11fa-0000-92a0ac7f4d7a"/>\n<rdf:Description xmlns:dc="http://purl.org/dc/elements/1.1/" rdf:about="" dc:format="application/pdf"><dc:title><rdf:Alt><rdf:li xml:lang="x-default">Printing from undefined</rdf:li></rdf:Alt></dc:title><dc:creator><rdf:Seq><rdf:li>steve</rdf:li></rdf:Seq></dc:creator></rdf:Description>\n<rdf:Description xmlns:pdfaid="http://www.aiim.org/pdfa/ns/id/" rdf:about="" pdfaid:part="2" pdfaid:conformance="B"/><rdf:Description xmlns:xmp="http://ns.adobe.com/xap/1.0/" rdf:about="" xmp:MetadataDate="2024-12-09T21:07:26.996486+00:00"/></rdf:RDF>\n</x:xmpmeta>\n\n<?xpacket end="w"?>\n"""


@pytest.fixture
def test_xml_file(tmp_path, test_xml_text):
    p = tmp_path.joinpath(
        "".join(["test_xml_dict__from_file__", str(time_ns()), ".xml"])
    )
    p.write_text(test_xml_text, encoding="utf8")
    return p


def test_from_file(test_xml_file, test_json_output):
    result = from_file(test_xml_file)
    assert dumps(result) == test_json_output


def test_from_string(test_xml_text, test_json_output):
    result = from_string(test_xml_text)
    assert dumps(result) == test_json_output
