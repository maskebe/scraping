ORIGINAL = [
    [
        ['one', 'two'],
        ['seven', 'eight']
    ],
    [
        ['nine', 'four'],
        ['three', 'one']
    ],
    [
        ['two', 'eight'],
        ['seven', 'four']
    ],
    [
        ['five', 'one'],
        ['four', 'two']
    ],
    [
        ['six', 'eight'],
        ['two', 'seven']
    ]
]

dict = {}

for item in ORIGINAL:
    dict.keys = item
    for i in item:
        i+= i
    dict.values = i

print(dict)
