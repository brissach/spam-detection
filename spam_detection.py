import re

last_line = None
frequency = 0
frequency_scaler = 0.1
frequency_multiplier = 2

def process(line):
    line = line.strip().lower()
    line = re.sub(r"[^a-z0-9 ]", " ", line)
    global last_line, frequency, frequency_scaler, frequency_multiplier
    if last_line is None:
        last_line = line
        return
    sim = calculate_diff(line)
    if sim > 0.25:
        frequency += frequency_scaler * frequency_multiplier ** frequency
        frequency = min(frequency, 1)
        if frequency >= 1:
            print("Spam detected: %s" % line)
            print(frequency + sim)
        else:
            print("Possible spam detected: %s" % last_line)
        print(frequency)
    else:
        frequency -= frequency_scaler * frequency_multiplier ** frequency
    last_line = line

def calculate_diff(line):
    if last_line is None:
        return 0.0
    similarity = 0.0
    for i in range(min(len(last_line), len(line))):
        if last_line[i] == line[i]:
            similarity += 1.0
    return similarity / max(len(last_line), len(line))

tests = [
    "Spam ^2s¤#c",
    "Spam Xz0<;W",
    "Spam 8-'`-",
    "Hello World!",

]

for test in tests:
    process(test)