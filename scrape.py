import re
import subprocess
import os


PAGES = [
    'https://en.wikipedia.org/wiki/File:Chess_klt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_qlt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_rlt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_blt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_nlt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_plt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_kdt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_qdt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_rdt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_bdt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_ndt45.svg',
    'https://en.wikipedia.org/wiki/File:Chess_pdt45.svg',
]


def main():
    print('Fetching and scraping HTML pages to find image URLs to download')
    image_urls = []
    for page in PAGES:
        text = subprocess.check_output(['curl', page], stderr=subprocess.DEVNULL).decode()

        lines = text.split('\n')
        lines = [l for l in lines if 'Original file' in l]
        assert len(lines) == 1
        line = lines[0]

        match = re.search(r'href="([^"]+)"', line)
        assert match

        url = match.group(1)
        assert url.startswith('//')
        url = 'https:' + url

        image_urls.append(url)
        print(url)

    answer = input('\nDownloading the images listed above. Continue? (y/N) ').strip().lower()
    if answer != 'y':
        return

    for url in image_urls:
        subprocess.run([
            'curl',
            url,
            '--remote-name',  # short form: -O
        ])

    print('\nDone.')


if __name__ == '__main__':
    main()
