from Obfuscatr import Obfuscatr
import sys

# ниже - небольшая обёртка для запуска руками
if __name__ == '__main__':
    print("Usage: ./script.py [words_count] [delimiter]")
    obf = Obfuscatr()
    if len(sys.argv) > 1:
        if isinstance(sys.argv[1], int):
            obf.words_count = sys.argv[1]
        else:
            print("'{}' cannot be words count".format(sys.argv[1]))
        if len(sys.argv) > 2:
            obf.delimiter = sys.argv[2]
    from_outer_space = input("Print string to obfuscate: ")
    final_string = obf.obfuscate(from_outer_space)
    print("Final result is: {}".format(final_string))



