"""
Docopt (https://docopt.org) is a powerful command line argument parser.
"""
import attr
import unicodedata

from docopt import docopt


def from_docopt(argv: str, docstring: str, version=None):
    """
    Convert argv to an attrs-decorated class.

    Use docopt and the given docstring and an optional version.
    """
    # get the docopt output
    docopt_dict = docopt(doc=docstring, version=version, argv=argv)
    # sanitize the keys: can't contain '-', must be a valid attribute name.
    temp = {}
    for key in docopt_dict.keys():
        clean = key.lstrip('-')
        if not __is_valid_name(clean):
            raise AttributeError(f"'{clean}' is an invalid attribute name")
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


def _is_id_start(character):
    allowed_id_start_categories = {"Ll", "Lm", "Lo", "Lt", "Lu", "Nl"}
    allowed_id_start_characters = {"_", "\u2118", "\u212E", "\u309B", "\u309C"}

    return (unicodedata.category(character) in allowed_id_start_categories
            or character in allowed_id_start_categories
            or unicodedata.category(unicodedata.normalize("NFKC", character)) in allowed_id_start_categories
            or unicodedata.normalize("NFKC", character) in allowed_id_start_characters)


def _is_id_continue(character):
    allowed_id_continue_categories = {"Ll", "Lm", "Lo", "Lt", "Lu",
                                      "Mc", "Mn", "Nd", "Nl", "Pc"}
    allowed_id_continue_characters = {"_", "\u00B7", "\u0387", "\u1369",
                                      "\u136A", "\u136B", "\u136C", "\u136D",
                                      "\u136E", "\u136F", "\u1370", "\u1371",
                                      "\u19DA", "\u2118", "\u212E", "\u309B",
                                      "\u309C"}

    return (unicodedata.category(character) in allowed_id_continue_categories
            or character in allowed_id_continue_characters
            or unicodedata.category(unicodedata.normalize("NFKC", character)) in allowed_id_continue_categories
            or unicodedata.normalize("NFKC", character) in allowed_id_continue_characters)
