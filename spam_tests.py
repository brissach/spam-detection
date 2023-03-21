import spam_detection as spam_detector

words = [
    "Spam ^2s¤#c",
    "Spam Xz0<;W",
    "Spam 8-'`-",
    "Lorem ipsum",
    "is simply dummy text of the printing",
    "and typesetting industry",
    "Spam ^2s¤#c",
    "Spam Xz0<;W",
    "Spam 8-'`-",
    "Spam ^2s¤#c",
    "Spam Xz0<;W",
    "Spam 8-'`-",
    "Spam ^2s¤#c",
    "Spam Xz0<;W",
    "Spam 8-'`-",
    "Spam ^2s¤#c",
    "Lorem Ipsum has been the industry's standard",
    "Spam Xz0<;W",
    "dummy text ever since the 1500s",
    "Spam 8-'`-",
    "Spam ^2s¤#c",
]

def test_spam_detection():
    for word in words:
        print(word, spam_detector.process(word))

if __name__ == "__main__":
    test_spam_detection()