from xml.etree.ElementTree import ElementTree

from scaling_umbrella import report_from_file


def test_report_from_file():
    assert (
        report_from_file("./fixtures/coverage_1.xml").__class__ is ElementTree
    )


def test_report_from_file_no_lines():
    try:
        r = report_from_file("./fixtures/coverage_no_lines.xml")
        assert False
    except ValueError as e:
        assert e.__str__() == "Empty lines object"
