import sys
import pefile


def enum_sections(executable):
    pe = pefile.PE(executable)
    sections_executable = set()
    for section in pe.sections:
        sections_executable.add(section.Name.decode('utf-8').rstrip('\x00'))
    return sections_executable


def set_to_str(set_data):
    str_to_return = ''
    for el in set_data:
        str_to_return = str_to_return.join(str(el) + ',')
    return str_to_return


def main():
    first_file = sys.argv[1]
    second_file = sys.argv[2]

    sections_first_file = enum_sections(first_file)
    sections_second_file = enum_sections(second_file)

    print("Seções comuns aos dois executáveis:", end=' ')
    [print(y, end=' ') for y in sections_first_file.intersection(sections_second_file)]
    print()
    print("Seções que estão presentes somente no primeiro executável: ", end='')
    [print(y, end=' ') for y in sections_first_file.difference(sections_second_file)]
    print()
    print("Seções que estão presentes somente no secundo executável: ", end='')
    [print(y, end=' ') for y in sections_second_file.difference(sections_first_file)]
    print()


if __name__ == '__main__':
    main()
