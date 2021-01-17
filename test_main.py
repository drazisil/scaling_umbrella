import defusedxml

from main import xml_from_file

defusedxml.defuse_stdlib()


def test_xml_from_file():
    assert xml_from_file('fixtures/coverage_1.xml')
