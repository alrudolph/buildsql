# https://www.postgresql.org/docs/current/pgtrgm.html

from buildsql.base import StrOrTerminal, Terminal


def similarity(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a similarity expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"similarity({str1}, {str2})"])


def show_trgm(str1: StrOrTerminal) -> Terminal:
    """Create a show_trgm expression for a string.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"show_trgm({str1})"])


def word_similarity(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a word_similarity expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"word_similarity({str1}, {str2})"])


def strict_word_similarity(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a strict_word_similarity expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"strict_word_similarity({str1}, {str2})"])


def show_limit() -> Terminal:
    """Create a show_limit expression.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal(["show_limit()"])


def set_limit(value: float) -> Terminal:
    """Create a set_limit expression.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"set_limit({value})"])


def is_similar(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create an is_similar expression between two strings with a threshold.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{str1} % {str2}"])


# TODO: <%
# TODO: %>
# TODO: <<%
# TODO: %>>


def distance(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a distance expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{str1} <-> {str2}"])


def left_word_distance(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a left_word_distance expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{str1} <<-> {str2}"])


def right_word_distance(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a right_word_distance expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{str1} <->> {str2}"])


def strict_left_word_distance(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a strict_left_word_distance expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{str1} <<<-> {str2}"])


def strict_right_word_distance(str1: StrOrTerminal, str2: StrOrTerminal) -> Terminal:
    """Create a strict_right_word_distance expression between two strings.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{str1} <->>> {str2}"])
