import json

sep = " : "
export = {}
id = 4
# dict = {"1": []}
# dict["1"] = ({ 'fr': 'essaie','en' : 'try'})
# print(dict)
# exit()

with open("raw.txt") as f:
    for i in f.readlines():
        cut = i.split(sep)
        cut[1] = cut[1].replace('\n', '').strip()

        header = ['fr', 'en']

        cards = dict(zip(header,cut))

        export[str(id)] = cards

        id += 1

tt = json.dumps(export, ensure_ascii=False, indent=4).encode("utf-8")

with open("sample.json", "w") as outfile:
    outfile.write(tt.decode())


print(tt.decode())