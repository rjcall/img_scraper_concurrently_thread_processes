import concurrent.futures
import time, os, requests
from scrape_pics.flags import flags


# return img obj
def seq(x):
    s = '%s-lgflag.gif' % x
    path_to_flag = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/%s' % s
    img = requests.get(path_to_flag)
    return img



def main():
    bytes_downloaded = 0
    start_cpu = time.clock()
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as process_ex:
        f_t_u = {process_ex.submit(seq, flag): flag for flag in flags}

        for x in concurrent.futures.as_completed(f_t_u):
            url = f_t_u[x]

            try:
                data = x.result()
                u = data.url
                path, file = os.path.split(u)

                with open('flags_p/' + file, 'wb') as img:
                    img.write(data.content)
            except Exception as exc:

                print('%r generated an exception: %s' % (url, exc))
            else:
                bytes_downloaded += len(data.content)

    print('Total Bytes Downloaded:', bytes_downloaded)
    stop = time.time()
    print('CPU time:', time.clock() - start_cpu)
    print('Execution time:', stop - start)
