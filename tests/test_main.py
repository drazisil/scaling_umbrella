from xml.etree.ElementTree import ElementTree

from scaling_umbrella import BaseReport


def test_report_from_file():
    b = BaseReport()
    assert (
        b.report_from_file("./fixtures/coverage_1.xml").__class__
        is ElementTree
    )
    assert b.xml_tree.__class__ is ElementTree


def test_report_from_file_no_lines():
    b = BaseReport()
    try:
        r = b.report_from_file("./fixtures/coverage_no_lines.xml")
        assert False
    except ValueError as e:
        assert e.__str__() == "Empty lines object"
