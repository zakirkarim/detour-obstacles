import argparse
import load

def main():
    #Включение дебаг режима
    parser = argparse.ArgumentParser(description='Use --debug')
    parser.add_argument('--debug', default=False, action='store_true')
    parser.add_argument('com', default=1, action='store')
    args = parser.parse_args()
    if args.debug == True:
        load.load(args.debug)
    load.load(False)

if __name__ == '__main__':
    main()