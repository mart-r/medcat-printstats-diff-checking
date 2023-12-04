from typing import Optional
import sys

import json


def get_cuis(d: dict, start_set: Optional[set] = None)-> set:
    if start_set is None:
        start_set = set()
    for k, v in d.items():
        if k == 'cui':
            start_set.add(v)
        elif isinstance(v, list):
            for el in v:
                if isinstance(el, dict):
                    get_cuis(el, start_set=start_set)
        elif isinstance(v, dict):
            get_cuis(v, start_set=start_set)
    return start_set



def main(file_path: str):
    with open(file_path) as f:
        data = json.load(f)
    cuis = get_cuis(data)
    print("CUIS:\n", cuis)


if __name__ == "__main__":
    main(*sys.argv[1:])
