from scrape_pics import get_flags_threads, get_flags, get_flags_process

if __name__ == "__main__":
    print('Sequentially')
    get_flags.main()
    print('\nConcurrently with Processes')
    get_flags_process.main()
    print('\nConcurrently with Thread Processes')
    get_flags_threads.main()
