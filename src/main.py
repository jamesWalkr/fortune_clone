import os
import random
import argparse

fortune_path = "/usr/share/fortune/"


def main():
    # Intialize argument parser
    parser = argparse.ArgumentParser(description="a fortune clone in python")

    # add optional positional argument
    parser.add_argument(
        "fortune_file", type=str, nargs="?", help="provide a furtune file "
    )

    # parse the arguments
    args = parser.parse_args()

    # add arguments to a dict
    # args_dict = vars(args)

    only_files = [
        f
        for f in os.listdir(fortune_path)
        if os.path.isfile(os.path.join(fortune_path, f))
    ]

    text_file_list = [file for file in only_files if not file.endswith(".dat")]

    basename = text_file_list[random.randint(0, len(text_file_list))]

    if args.fortune_file in text_file_list:
        basename = args.fortune_file
        get_random_quote(basename)
    else:
        get_random_quote(basename)


def get_random_quote(base_name):
    random_file = f"{fortune_path}{base_name}"

    # print(f"This is quote is coming from {random_file}")

    with open(random_file, "r") as f:
        text = f.read().split("%")
    print(text[random.randint(0, len(text))])


if __name__ == "__main__":
    main()
