import os
import sys
import xml.etree.ElementTree as Et


def print_response(apk_permission):
    print("=======\n\nPermissões por APK\n\n=======\n\n")
    for k, v in apk_permission.items():
        print(k[16:-4] + str(':  ') + str(list(v)) + '\n\n')


def print_1b(apk_permission):
    print("=======\n\nPermissões únicas por APK\n\n=======\n\n")
    repeated_permissions = set()
    for k, v in apk_permission.items():
        unique_permission = v.copy()
        for ki, vi in apk_permission.items():
            if k == ki:
                continue
            unique_permission -= v & vi
        repeated_permissions.update(v - unique_permission)
        print(k[16:-4] + str(':  ') + str(list(unique_permission)) + '\n\n')
    print("=======\n\nPermissões comuns das APKs\n\n=======\n\n")
    print(str(list(repeated_permissions)))


def main():
    apk_permission = {}
    dir = sys.argv[1]
    with os.scandir(dir) as entries:
        for entry in entries:
            apk_permission[entry.name] = set()
            root = Et.parse(entry).getroot()
            permissions = root.findall("uses-permission")
            for perm in permissions:
                for att in perm.attrib:
                    try:
                        apk_permission[entry.name].add(perm.attrib[att].split('permission.')[1])
                    except IndexError:
                        continue

    print_1b(apk_permission)


if __name__ == '__main__':
    main()
