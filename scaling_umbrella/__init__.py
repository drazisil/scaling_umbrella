from xml.etree.ElementTree import parse


def xml_from_file(file_path):
    xml_tree = parse(file_path)
    lines = list(xml_tree.find("./packages/package/classes/class/lines"))
    if len(lines) == 0:
        raise Exception('Empty lines object')
    print(
        "{} has {} lines.".format(
            file_path,
            len(lines),
        )
    )
    return xml_tree
