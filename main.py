entry = "Tonight in Zarnwick, rain falls upward at 14 miles per hour through midnight, with a high of 61 and a low of Tuesday, so bring an umbrella and a calendar."

assert 1 <= len(entry) <= 160
assert "\n" not in entry

with open("/output/entry.txt", "w") as f:
    f.write(entry + "\n")
