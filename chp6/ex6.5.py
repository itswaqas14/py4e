text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")

sliced = text[pos+1:]
sliced = sliced.strip()
sliced = float(sliced)
print(sliced)