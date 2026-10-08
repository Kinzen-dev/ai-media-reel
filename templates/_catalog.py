#!/usr/bin/env python3
# Append (or update) passing templates in _manifest.json, then re-run _categorize.py.
# Usage (from showcase/templates/):  python3 _catalog.py <entries.json>
# entries.json = [{"slug","title","archetype","ref","palette","whenToUse","signature","fps",
#                  "builtBy","lane"}, ...]   ("file" and "thumb" are derived; status = "pass").
# Idempotent: an entry whose slug already exists is UPDATED in place, never duplicated.
# Refuses to catalog a slug whose HTML or thumbnail is missing, or that still contains a banned dash.
import json, os, subprocess, sys

BAD = {0x2012, 0x2013, 0x2014, 0x2015, 0x2500, 0x2501}
FIELDS = ["slug", "title", "archetype", "ref", "file", "thumb", "palette", "category", "lane",
          "whenToUse", "signature", "fps", "fpsMode", "status", "builtBy"]

def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 _catalog.py <entries.json>")
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    entries = json.load(open(sys.argv[1], encoding="utf-8"))
    d = json.load(open("_manifest.json", encoding="utf-8"))
    by_slug = {t["slug"]: t for t in d["templates"]}
    added, updated, refused = [], [], []
    for e in entries:
        slug = e["slug"]
        html, thumb = f"{slug}.html", f"_thumbs/{slug}.png"
        if not os.path.exists(html) or not os.path.exists(thumb):
            refused.append(f"{slug}: missing {'html' if not os.path.exists(html) else 'thumb'}")
            continue
        src = open(html, encoding="utf-8").read()
        if any(ord(c) in BAD for c in src):
            refused.append(f"{slug}: banned dash in file")
            continue
        meta = " ".join(str(e.get(k, "")) for k in ("title", "archetype", "ref", "palette", "whenToUse", "signature"))
        if any(ord(c) in BAD for c in meta):
            refused.append(f"{slug}: banned dash in catalog metadata")
            continue
        rec = {"slug": slug, "file": html, "thumb": thumb, "status": "pass", "category": e.get("lane", "interaction")}
        rec.update({k: e[k] for k in e if k in FIELDS})
        rec = {k: rec[k] for k in FIELDS if k in rec}
        if slug in by_slug:
            by_slug[slug].clear(); by_slug[slug].update(rec); updated.append(slug)
        else:
            d["templates"].append(rec); by_slug[slug] = rec; added.append(slug)
    json.dump(d, open("_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"manifest: {len(d['templates'])} templates | added {added} | updated {updated}")
    for r in refused:
        print("REFUSED", r)
    subprocess.run([sys.executable, "_categorize.py"], check=True)

if __name__ == "__main__":
    main()
