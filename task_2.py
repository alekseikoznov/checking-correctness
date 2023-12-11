from collections import defaultdict


def group_versions(list_version):
    version_count = defaultdict(int)

    for pair in list_version:
        id, version = pair
        version_count[(id, version)] += 1

    result = [
        [id, version, count] for (id, version), count in version_count.items()
    ]
    return result


def main():
    list_version = [
        ["665587", 2],
        ["669532", 1],
        ["669537", 2],
        ["669532", 1],
        ["665587", 1],
    ]
    result = group_versions(list_version)
    print(result)


if __name__ == "__main__":
    main()
