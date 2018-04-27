import sys
script, encoding, error = sys.argv


def main (language, encoding, errors):
    line = language.read()

    if line:
        print_line(line, encoding, errors)
        return main(language, encoding, errors)


def print_line (line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "\n\n\n******\n<==>\n", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)
