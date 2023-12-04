import sys

import re


START_END = """==========================================="""
SPLIT_TARGET = "\n".join((START_END, START_END))

_DOC_FINDER_PATTERN = re.compile("^(Docs with false (positives|negatives):((?: Doc \d+;)+ Doc \d+)$)",
                                 flags=re.MULTILINE)
_DOC_FINDER_PATTERN_2 = re.compile("^(Docs with false (positives|negatives):((?: \d+;)+ \d+)$)",
                                 flags=re.MULTILINE)

_DOC_NR_FINDER = re.compile("Doc (\d+)")


def _reorder_docs(docs_found: str, target: str = "; ") -> str:
    def get_nr(doc: str) -> int:
        try:
            return int(doc)
        except ValueError:
            return int(_DOC_NR_FINDER.match(doc).group(1))
    all_docs = docs_found.split(target)
    return target.join(sorted(all_docs, key=get_nr))


def clean_part(part: str) -> str:
    """Need to clean parts because of lines like this:
    ```
    Docs with false positives: Doc 3; Doc 5; Doc 4; Doc 2; Doc 1
    ```
    The order in which depends on random seed at the start of execution.
    So this will try and reorder the docs so that they're in numeric order.

    Args:
        part (str): The input part

    Returns:
        str: The output part
    """
    replacements: list[tuple[str, str]] = []
    found_matches = _DOC_FINDER_PATTERN.findall(part) + _DOC_FINDER_PATTERN_2.findall(part)
    for match_all, pos_neg, docs_part in found_matches:
        # this removes the preceding space and puts it back
        new_docs_part = " " + _reorder_docs(docs_part.strip())
        # replacing old docs part with new ordering
        new_match_content = match_all.replace(docs_part, new_docs_part)
        # mark this line to be replaced with the re-arranged one
        if match_all != new_match_content:
            replacements.append((match_all, new_match_content))
    if replacements:
        print("[CLEAN] Doing", len(replacements), "re-arrangements")
    for target, replacement in replacements:
        part = part.replace(target, replacement)
    return part


def find_parts(file_path: str) -> tuple[str, str]:
    with open(file_path) as f:
        contents = f.read().strip()
    if contents.startswith(START_END):
        contents = contents[len(START_END):].strip()
    if contents.endswith(START_END):
        contents = contents[:-len(START_END)].strip()
    return [p.strip() for p in contents.strip().split(SPLIT_TARGET)]


def main(file_path: str):
    one, two = find_parts(file_path)
    one, two = clean_part(one), clean_part(two)
    if one == two:
        print("Outputs identical for", file_path)
    else:
        print("Outputs DIFFER for", file_path)
        print(f"ONE\n{one[:100]}\n...\n{one[-100:]}\nTWO\n{two[:100]}\n...\n{two[-100:]}")


if __name__ == "__main__":
    main(*sys.argv[1:])
