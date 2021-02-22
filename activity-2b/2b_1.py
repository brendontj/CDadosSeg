import sys
import os
import pefile


def format_print(sections):
    for k, v in sections.items():
        print(k + ':', end='')
        for value in v:
            print('\t' + value)


def enum_sections(executable):
    pe = pefile.PE(executable)
    executable_sections = dict()
    executable_sections[executable.name] = []
    for section in pe.sections:
        if section.IMAGE_SCN_MEM_EXECUTE:
            executable_sections[executable.name].append(section.Name.decode('utf-8'))
    return executable_sections


def main():
    file = sys.argv[1]
    if os.path.isdir(file):
        with os.scandir(file) as files:
            for exe in files:
                format_print(enum_sections(exe))
    elif os.path.isfile(file):
        format_print(enum_sections(file))


if __name__ == '__main__':
    main()