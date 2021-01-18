from xml.etree.ElementTree import ElementTree

from scaling_umbrella import report_from_file


def test_xml_from_file():
    assert report_from_file("./fixtures/coverage_1.xml").__class__ is ElementTree
