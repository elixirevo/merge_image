from openpyxl import load_workbook
import os
import json

load_wb = load_workbook("./hidden_rarity.xlsx", data_only=True)

load_ws = load_wb['Sheet1']

metadata = {}
metadata['metadata'] = []

for i in range(97, 123):
    search_shell = chr(i).upper()
    metadata['metadata'].append({
        "background": load_ws[f'B{search_shell}2'].value,
        "body": load_ws[f'B{search_shell}3'].value,
        "tatto": load_ws[f'B{search_shell}4'].value,
        "hat": load_ws[f'B{search_shell}5'].value,
        "eye": load_ws[f'B{search_shell}6'].value,
        "clothe": load_ws[f'B{search_shell}7'].value,
        "mouth": load_ws[f'B{search_shell}8'].value,
        "back": load_ws[f'B{search_shell}9'].value,
        "weapon": load_ws[f'B{search_shell}10'].value,

    })
with open(f"./hidden3.json", "w") as outfile:
    json.dump(metadata, outfile)
