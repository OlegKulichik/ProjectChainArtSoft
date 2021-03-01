import time,sys


t = time.time()

def decoder():
    with open(sys.argv[-1], "r") as file:
        for text in file:
            if len(set(text)) == len(text):
                return text
            texts = []
            first = text[0]
            second = text[1]
            last = ""
            for txt in text[2:]:
                if txt != second and second != first:
                    if second != last:
                        texts.append(second)
                        last = second
                    else:
                        del texts[-1]
                first = second
                second = txt
            result =  "".join(texts)
            return result

print(decoder())
print(time.time() - t)