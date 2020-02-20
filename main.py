import os
#import pandas  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYREPO"]

    #my_output = str(my_input)

    #print(f"::set-output name=myOUTPUT::{my_output}")
    print(f"www.github.com/{my_input}")
    
if __name__ == "__main__":
    main()
