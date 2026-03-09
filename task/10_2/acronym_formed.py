from typing import List


def main() -> None:
    names: List[str] = [input().strip() for _ in range(4)]
    answer = ''.join(name[0].upper() for name in names)
    print(answer)


if __name__ == '__main__':
    main()
