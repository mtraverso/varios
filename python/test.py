import sys

def main():
    result = ""
    for value in sys.argv[1:]:
        result += value[:1].upper() + value[1:].lower()+ " "
    print result
    

if __name__ == '__main__':
    main()