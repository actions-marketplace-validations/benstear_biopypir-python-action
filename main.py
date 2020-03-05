import os
#import pandas  # noqa We are just importing this to prove the dependency installed correctly


def main():
    '''
    repo_name = os.environ["INPUT_MYREPO"]
    python_version = os.environ["INPUT_PYTHON_VERSION"]
    os = os.environ["INPUT_OS"]
    lint = os.environ["INPUT_LINT"]
    package_name = os.environ["INPUT_PACKAGE_NAME"]
    '''
    os.system('echo $PWD')
    os.system('ls -a')
    
    #my_output = str(my_input)
    #print(f"::set-output name=myOUTPUT::{my_output}")
    #print(f"www.github.com/{my_input}")
    
if __name__ == "__main__":
    main()
