import os
import requests
from urllib.parse import urlparse

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False

    return True


def get_file_name_from_cd(cd):
    a = urlparse(cd)
    print(a)
    return os.path.basename(a.path)


def download_from_url(url):
    allowed = is_downloadable(url)

    if allowed:
        try:
            req = requests.get(url, allow_redirects=True)

            filename = get_file_name_from_cd(url)
            fd = open(filename, "wb")

            for buffer in req.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True
        except Exception as Err:
            print("Error at file download:", Err)
            return False
    else:
        return False


# if __name__ == '__main__':
#     url = "https://www.google.com/favicon.ico"
#     result = download_from_url(url)
#
#     if result:
#         print("File successfully Downloaded")
#     else:
#         print("Unable to Download")