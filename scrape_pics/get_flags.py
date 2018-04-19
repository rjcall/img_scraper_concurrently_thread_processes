import requests, os, time
from functools import reduce
from scrape_pics.flags import flags


def seq(x):
    s = '%s-lgflag.gif' %x
    path_to_flag = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/%s' %s
    img = requests.get(path_to_flag)
    return img


def main():
    start_cpu = time.clock()
    start = time.time()
    res = []
    for x in flags:
        s = seq(x)
        res.extend(s)
        url = s.url
        path, file = os.path.split(url)
        with open('flags/'+file, 'wb') as img:
            img.write(s.content)

    print('bytes: %s' %reduce(lambda x, y: x+y, [len(x) for x in res]))
    stop = time.time()
    print('CPU time:', time.clock() - start_cpu)
    print('Execution time:', stop-start)

if __name__ == '__main__':
    main()

