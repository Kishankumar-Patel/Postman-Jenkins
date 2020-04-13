import os 
import sys


def main(argv):

    test = argv[0].lower()

    switcher = {
        "templateservice": "newman run TemplateService-Automate.postman_collection.json -d data.csv"
    }
    
    os.system(switcher.get(test,"echo No such job"))

if __name__ == "__main__":
    main(sys.argv[1:])