"""
This module contains functions to fetch SF Symbols and their names from a JSON conversion table.
"""

import json
import os

sf_symbols_conversion_table_path = os.path.join(
    os.path.dirname(__file__),
    "sf_symbols_conversion_table.json"
)

def fetch_symbol(symbol_name: str) -> str:
    """Fetches the SF Symbol with the given name."""

    with open(sf_symbols_conversion_table_path, "r") as file:
        sf_symbols = json.load(file)

    try:
        return sf_symbols[symbol_name].encode("utf-8").decode("unicode_escape")
    except KeyError as e:
        raise KeyError(f"Symbol '{symbol_name}' not found in conversion table.") from e

def fetch_all_symbols() -> list[str]:
    """Fetches all SF Symbols."""

    with open(sf_symbols_conversion_table_path, "r") as file:
        sf_symbols = json.load(file)

    return list(sf_symbols.values())

def fetch_all_names() -> list[str]:
    """Fetches all SF Symbol names."""

    with open(sf_symbols_conversion_table_path, "r") as file:
        sf_symbols = json.load(file)

    return list(sf_symbols.keys())

def fetch_all() -> dict[str, str]:
    """Fetches all SF Symbols and their names."""

    with open(sf_symbols_conversion_table_path, "r") as file:
        sf_symbols = json.load(file)

    return sf_symbols
