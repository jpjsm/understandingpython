from bson import ObjectId
from datetime import datetime, timedelta, date, time
import json
from typing import Any, List, Dict, Tuple


def Decode(o: Any) -> str:
    if isinstance(o, ObjectId):
        return str(o)
    if isinstance(o, datetime):
        return o.isoformat()
    if isinstance(o, timedelta):
        return str(0)
    if isinstance(o, date):
        return o.isoformat()
    if isinstance(o, time):
        return o.isoformat()

    return str(o)


def Traverse(search_dict: Dict[str, Any], keys: List[str]) -> List[Tuple[str, str]]:
    """
    Recursively traverses all keys and and extracts the values in the keys list
    """

    if not isinstance(search_dict, dict):
        return None

    kvp_found = []
    for k, v in search_dict.items():
        if k in keys:
            r = Decode(v).strip()
            if r:
                kvp_found.append((k, r))

        elif isinstance(v, dict):
            inner_values = Traverse(v, keys)
            kvp_found += inner_values

        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    more_values = Traverse(i, keys)
                    kvp_found += more_values

    return kvp_found
