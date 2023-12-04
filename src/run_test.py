import sys
import json

from medcat.cat import CAT


def reorder_alphabetical_in_dicts(output: list) -> list:
    """Need to reorder the keys in alphabetical order in dicts
       because otherwise the orders can be different
       thus making the comparison useless

    Args:
        output (list): The original list

    Returns:
        list: The output list
    """
    def _reorder(d: dict) -> dict:
        nd = {}
        keys = sorted(list(d.keys()))
        for k in keys:
            nd[k] = d[k]
        return nd
    return [
        _reorder(el) if isinstance(el, dict) else el
        for el in output
    ]


def do_print_stats(cat: CAT, mct_data: dict):
    output = cat._print_stats(mct_data)
    output = reorder_alphabetical_in_dicts(output)
    print(f"RECEIVED:\n{json.dumps(output, indent=2)}")


def main(model_pack_path: str, mct_export_path: str):
    print("Loading", model_pack_path)
    cat = CAT.load_model_pack(model_pack_path)
    print("Loading MCT data from", mct_export_path)
    with open(mct_export_path) as f:
        mct_data = json.load(f)
    print("Starting _print_stats")
    do_print_stats(cat, mct_data)


if __name__ == "__main__":
    main(*sys.argv[1:])