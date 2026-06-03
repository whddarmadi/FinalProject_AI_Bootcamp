import json

with open("data/sop.json", "r", encoding="utf-8") as f:
    SOP_DATA = json.load(f)

def get_response(text):

    text = text.lower()

    for keyword, response in SOP_DATA.items():
        if keyword in text:
            return response

    return "Maaf, informasi belum tersedia."
