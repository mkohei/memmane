# coding=utf-8
""" transform CSV to JSON """

import csv
import json

with open('../data/krlab.member.csv') as f:
    reader = csv.reader(f)
    header = next(reader)

    members = []
    for row in reader:
        m = {}
        for i,d in enumerate(row):
            m[header[i]] = d
        members.append(m)

    text = json.dumps(members, ensure_ascii=False)
    f2 = open('../data/krlab.member.json', 'w')
    f2.write(text)
