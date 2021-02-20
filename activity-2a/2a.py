import os
import xml.etree.ElementTree as ET


def print_response(apk_permission):
    print("==============================================\n\nPermissões por APK\n\n==============================================\n\n")
    for k, v in apk_permission.items():
        print(k[16:-4] + str(':') + list(v))


def main():
    apk_permission = {}
    with os.scandir('manifests/') as entries:
        for entry in entries:
            apk_permission[entry] = set()
            root = ET.parse(entry).getroot()
            permissions = root.findall("uses-permission")
            for perm in permissions:
                for att in perm.attrib:
                    try:
                        apk_permission[entry].add(perm.attrib[att].split('permission.')[1])
                    except IndexError:
                        continue

    print_response(apk_permission)


if __name__ == '__main__':
    main()