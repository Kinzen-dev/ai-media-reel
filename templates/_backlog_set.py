#!/usr/bin/env python3
# Set the status of world-class backlog directions.  Usage: python3 _backlog_set.py <status> <backlog-slug>=<template-slug> ...
# (plain <backlog-slug> keeps the same template slug). status: todo | building | built | parked
import json, sys
p = "_backlog-worldclass.json"
d = json.load(open(p, encoding="utf-8"))
status, pairs = sys.argv[1], sys.argv[2:]
by = {x["slug"]: x for x in d["directions"]}
for pair in pairs:
    b, _, t = pair.partition("=")
    if b not in by:
        print("UNKNOWN", b); continue
    by[b]["status"] = status
    if t: by[b]["templateSlug"] = t
    print(status, b, "->", t or b)
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
todo = [x for x in d["directions"] if x["status"] == "todo"]
print("remaining todo:", len(todo), "| S5 todo:", sum(1 for x in todo if x["strength"] == 5))
