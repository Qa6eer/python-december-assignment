scores = {}
scores["ABDUL"] = 85
scores["ASJAD"] = 90
scores["QADEER"] = 95
scores["TAIF"] = 92
scores.pop("TAIF")
print(scores.get("QADEER", "Not found"))