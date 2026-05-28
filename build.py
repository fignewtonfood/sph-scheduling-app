#!/usr/bin/env python3
"""
SPH Scheduling App — Build Script
Injects SEED_DATA from data.json into index.html.
Run: python3 build.py

For GitHub Pages deployment:
  1. Run this script to generate index.html with embedded seed
  2. Push index.html + data.json to your GitHub Pages repo
  3. data.json is the live data store (read/written by admin mode)
  4. SEED_DATA in index.html is only used if data.json is unreachable
"""
import json, shutil, sys
from pathlib import Path

HERE = Path(__file__).parent
SRC  = HERE / 'index_template.html'  # unbuilt template (optional)
DATA = HERE / 'data.json'
OUT  = HERE / 'index.html'

if not DATA.exists():
    print(f"ERROR: {DATA} not found", file=sys.stderr)
    sys.exit(1)

with open(DATA) as f:
    seed = json.load(f)

seed_js = 'const SEED_DATA=' + json.dumps(seed) + ';'

# Read current index.html (which has the placeholder or old seed)
with open(OUT) as f:
    html = f.read()

# Replace either the placeholder or old seed
import re
html = re.sub(r'const SEED_DATA=.*?;', seed_js, html, count=1, flags=re.DOTALL)

with open(OUT, 'w') as f:
    f.write(html)

print(f"Built {OUT}")
print(f"  {len(seed.get('courses',[]))} courses, {len(seed.get('instructors',[]))} instructors, {len(seed.get('offerings',[]))} offerings")
print(f"  File size: {OUT.stat().st_size:,} bytes")
