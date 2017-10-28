import semantic_version


def parse_version_number(version):
    """
    Parse a version number of varying lengths into a SemVer instance.

    This function takes a variable length version number and does a 
    reasonably good job of converting it into a valid instance of
    a SemVer object.
    """
    parts = version.split('.')
    number_of_parts = len(parts)
    if number_of_parts == 3:
        v = '.'.join(parts)
    elif number_of_parts == 2:
        v = '{}.0'.format('.'.join(parts))
    elif number_of_parts > 3:
        v = '{}'.format('.'.join(parts[:3]))
    else:
        v = '{}.0.0'.format(parts[1])

    return semantic_version.Version(v)
