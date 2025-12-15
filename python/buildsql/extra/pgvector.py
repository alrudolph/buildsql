# https://github.com/pgvector/pgvector

from buildsql.base import StrOrTerminal, Terminal


def vector(values: list[float]) -> StrOrTerminal:
    """Create a vector literal for pgvector.

    TODO: link to docs.
    TODO: example usage
    """
    vals = ",".join(str(v) for v in values)
    return Terminal([f"'[{vals}]'"])


def l2_distance(vec1: StrOrTerminal, vec2: StrOrTerminal) -> Terminal:
    """Create an L2 distance expression between two vectors.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{vec1} <-> {vec2}"])


def neg_inner_product(vec1: StrOrTerminal, vec2: StrOrTerminal) -> Terminal:
    """Create a negative inner product expression between two vectors.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{vec1} <#> {vec2}"])


def cosine_distance(vec1: StrOrTerminal, vec2: StrOrTerminal) -> Terminal:
    """Create a cosine distance expression between two vectors.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{vec1} <=> {vec2}"])


def l1_distance(vec1: StrOrTerminal, vec2: StrOrTerminal) -> Terminal:
    """Create an L1 distance expression between two vectors.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{vec1} <+> {vec2}"])


def hamming_distance(vec1: StrOrTerminal, vec2: StrOrTerminal) -> Terminal:
    """Create a Hamming distance expression between two vectors.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{vec1} <~> {vec2}"])


def jaccard_distance(vec1: StrOrTerminal, vec2: StrOrTerminal) -> Terminal:
    """Create a Jaccard distance expression between two vectors.

    TODO: link to docs.
    TODO: example usage
    """
    return Terminal([f"{vec1} <%> {vec2}"])
