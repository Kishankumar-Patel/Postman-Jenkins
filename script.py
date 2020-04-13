import os 
import sys


def main(argv):

    test = argv[0].lower()
    print(f"*****************************Job Triggered : {test.upper()} *****************************")
    switcher = {
        "templateservice": "npm run templateService-test"
    }
    os.system("npm install")
    os.system("npm install newman-reporter-html")
    os.system(switcher.get(test,"echo No such job"))

if __name__ == "__main__":
    main(sys.argv[1:])
