from sqlmap_only_get import SQLtest
from dork_parser import DorkParser
import argparse

banner = '''
 ▄▄· ▄ •▄ ▄▄▄▄· ▄• ▄▌ ▄▄▄·▄▄▄▄▄    • ▌ ▄ ·.  ▄▄▄·  ▄▄▄·
▐█ ▌▪█▌▄▌▪▐█ ▀█▪█▪██▌▐█ ▄█•██      ·██ ▐███▪▐█ ▀█ ▐█ ▄█
██ ▄▄▐▀▀▄·▐█▀▀█▄█▌▐█▌ ██▀· ▐█.▪    ▐█ ▌▐▌▐█·▄█▀▀█  ██▀·
▐███▌▐█.█▌██▄▪▐█▐█▄█▌▐█▪·• ▐█▌·    ██ ██▌▐█▌▐█ ▪▐▌▐█▪·•
·▀▀▀ ·▀  ▀·▀▀▀▀  ▀▀▀ .▀    ▀▀▀     ▀▀  █▪▀▀▀ ▀  ▀ .▀   
'''

def main():
    scan = SQLtest()
    search = DorkParser()

    parser = argparse.ArgumentParser(description="EXxX0RCIST E6AJI BCEM PTbI U }I{0nbI")

    # Добавляем аргументы
    parser.add_argument('-p', '--parsing', type=str, help='only parsing and collecting entry points')
    parser.add_argument('-s', '--scan', type=str, help='only sqli scan targets')
    parser.add_argument('-d', '--dorkresult', type=int, help='number of search results for dorks')
    parser.add_argument('-t', '--timesleep', type=int, help='time between google queries')

    # Парсим аргументы
    args = parser.parse_args()

    print(banner)

    # Обработка аргументов
    if args.parsing:
        if args.timesleep is not None:
            search.set_time_sleep(args.timesleep)
        if args.dorkresult is not None:
            search.set_result_search(args.dorkresult)
        search.main_pars()

    elif args.scan:
        scan.main_scan()
    else:
        if args.timesleep is not None:
            search.set_time_sleep(args.timesleep)
        if args.dorkresult is not None:
            search.set_result_search(args.dorkresult)
        search.main_pars()
        scan.main_scan()

if __name__ == '__main__':
    main()