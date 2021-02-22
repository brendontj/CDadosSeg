import sys
import os
import pefile


def enum_sections(executable):
    pe = pefile.PE(executable)
    # print(pe.dump_info())
    for section in pe.sections:
        print(section.Name.decode('utf-8'))

        print(hex(bytes(section.Characteristics) - b'0x00000020'))



def main():
    file = sys.argv[1]
    if os.path.isdir(file):
        with os.scandir(file) as files:
            for file in files:
                enum_sections(file)
    elif os.path.isfile(file):
        pass


if __name__ == '__main__':
    main()