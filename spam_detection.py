import re

last_line = None
frequency = 0
frequency_scaler = 0.1
frequency_multiplier = 2
frequency_decay = 0.08

def process(line):
    line = line.strip().lower()
    line = re.sub(r"[^a-z0-9 ]", "", line)
    global last_line, frequency, frequency_scaler, frequency_multiplier, frequency_decay
    if last_line is None:
        last_line = line
        return
    sim = calculate_sim(line)
    match = []
    for i in range(min(len(last_line), len(line))):
        if last_line[i] == line[i]:
            match.append(last_line[i])
        else: 
            break
    match = "".join(match)
    if len(match) > 0:
        sim *= 1.0 + (len(match) / max(len(last_line), len(line)))
    if sim > 0.25:
        frequency += frequency_scaler * frequency_multiplier ** frequency
        frequency = min(frequency, 1)
        if frequency >= 0.5:
            print("Spam detected: %s" % line)
        else:
            print("Possible spam detected: %s" % last_line)
    else:
        frequency -= max(frequency_decay, frequency_scaler * frequency)
    last_line = line

def calculate_sim(line):
    if last_line is None: return 0.0
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
    "Spam ^2s¤#c",
    "Spam Xz0<;W",
    "Spam 8-'`-",
    "Spam ^2s¤#c",
    "Spam Xz0<;W",
    "Spam 8-'`-",
]

for test in tests:
    process(test)