#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
"""Package the declarative Forge mod catalog. No executable payloads."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def package():
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    if catalog['format'] != 1 or type(catalog['revision']) is not int or catalog['revision'] < 1:
        raise ValueError('Unsupported catalog format or revision')
    mods = catalog['mods']
    if not isinstance(mods, list) or len(mods) > 128:
        raise ValueError('Invalid mod count')
    ids = set()
    for mod in mods:
        if mod['id'] in ids or mod['section'] not in ('panel', 'lock_screen') or not mod['controls'] or mod['engine_revision'] < 1:
            raise ValueError('Invalid or duplicate mod')
        ids.add(mod['id'])
    data = (json.dumps(catalog, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    if len(data) > 2 * 1024 * 1024:
        raise ValueError('Catalog exceeds 2 MiB')
    return data

if __name__ == '__main__':
    output = ROOT / 'build/release/cosmic-forge-mods.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(package())
    print(output)
