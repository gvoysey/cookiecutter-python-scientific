from docopt import docopt
import attr
import unicodedata

"""
Docopt (https://docopt.org) is a powerful command line argument parser.
"""


def from_docopt(argv: str, docstring: str, version=None):
    """
    Convert argv to an attrs-decorated class
    :param argv:
    :param docstring:
    :param version:
    :return: InputArgs
    """
    # get the docopt output
    docopt_dict = docopt(doc=docstring, version=version, argv=argv)
    # sanitize the keys: can't contain '-', must be a valid attribute name.
    temp = {}
    for key in docopt_dict.keys():
        clean = key.lstrip('-')
        if not __is_valid_name(clean):
            raise AttributeError("Cannot convert key '{}' to a valid attribute name".format(clean))
        temp[clean] = attr.ib(default=docopt_dict[key])
    # make a class out of it
    return attr.make_class(name='InputArgs', attrs=temp)()


def __is_valid_name(name):
    if not _is_id_start(name[0]):
        return False
    for character in name[1:]:
        if not _is_id_continue(character):
            return False
    return True  # All characters are allowed.


_allowed_id_continue_categories = {"Ll", "Lm", "Lo", "Lt", "Lu", "Mc", "Mn", "Nd", "Nl", "Pc"}
_allowed_id_continue_characters = {"_", "\u00B7", "\u0387", "\u1369", "\u136A", "\u136B", "\u136C", "\u136D", "\u136E",
                                   "\u136F", "\u1370", "\u1371", "\u19DA", "\u2118", "\u212E", "\u309B", "\u309C"}
_allowed_id_start_categories = {"Ll", "Lm", "Lo", "Lt", "Lu", "Nl"}
_allowed_id_start_characters = {"_", "\u2118", "\u212E", "\u309B", "\u309C"}


def _is_id_start(character):
    return unicodedata.category(
            character) in _allowed_id_start_categories or character in _allowed_id_start_categories or unicodedata.category(
            unicodedata.normalize("NFKC", character)) in _allowed_id_start_categories or unicodedata.normalize("NFKC",
                                                                                                               character) in _allowed_id_start_characters


def _is_id_continue(character):
    return unicodedata.category(
            character) in _allowed_id_continue_categories or character in _allowed_id_continue_characters or unicodedata.category(
            unicodedata.normalize("NFKC", character)) in _allowed_id_continue_categories or unicodedata.normalize(
            "NFKC",
            character) in _allowed_id_continue_characters
