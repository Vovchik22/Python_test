SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    if size < 0:
        raise ValueError('number must not be negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(6464646194964645646, False))
    print(approximate_size(1000000000))
