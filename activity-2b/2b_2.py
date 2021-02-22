import sys
import pefile


def enum_sections(executable):
    pe = pefile.PE(executable)
    sections_executable = set()
    for section in pe.sections:
        sections_executable.add(section.Name.decode('utf-8'))
    return sections_executable


def main():
    first_file = sys.argv[1]
    second_file = sys.argv[2]

    sections_first_file = enum_sections(first_file)
    sections_second_file = enum_sections(second_file)

    print("Seções comuns aos dois .exe: " + str(*sections_first_file.intersection(sections_second_file)))
    print("Seções que estão presentes somente no primeiro .exe: " +
          str(*sections_first_file.difference(sections_second_file)))
    print("Seções que estão presentes somente no secundo .exe: " +
          str(*sections_second_file.difference(sections_first_file)))


if __name__ == '__main__':
    main()
