import os
#import pandas  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYREPO"]

    my_output = str(my_input)

    print(f"::set-output name=myOUTPUTt::{my_output}")


if __name__ == "__main__":
    main()
