'''
Author: Yokan
'''
import requests
import re
import warnings
import os
from colorama import init
import json
import urllib.parse
warnings.filterwarnings("ignore")
init(autoreset=True)

def local_article_read(file_name):
    file = open("./local_article/"+file_name, 'r', encoding="utf-8").read()
    file = urllib.parse.unquote(file)
    return file

def get_image(file_name):
    short_file_name = file_name.split(".")[0]
    file_content = local_article_read(file_name)
    img_pattern = r'(!\[.*?\]\({0}\.assets/image-.*?.png\))'.format(short_file_name)
    image_list = re.findall(img_pattern, file_content)
    return image_list

def upload_img(file_name):
    img_list = get_image(file_name)
    dir_list = []
    img_path_list = []
    for i in img_list:
        short_file_name = file_name.split(".")[0]
        img_pattern = r'({0}\.assets/image-.*?.png)'.format(short_file_name)
        dir = re.findall(img_pattern, i)
        print(dir)
        dir_list.extend(dir)
    for i in dir_list:
        i = str(i)
        real_file = "./local_article/" + i
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
        "Host": "www.freebuf.com",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Origin": "https://www.freebuf.com",
        "Referer": "https://www.freebuf.com/write"
        }
        pattern = r"(image-.*?.png)"
        img_name = re.search(pattern, i).group()
        res = requests.post(url="https://www.freebuf.com/fapi/frontend/upload/image", headers=headers, files ={"file": open(real_file,"rb")}, verify=False)
        res_json = json.loads(res.text)
        img_url = res_json["data"]["url"]
        print(f"\033[1;35m[+]{file_name} upload success! >> \033[0m" + img_url)
        img_path = f"![{img_name}]" + f"({img_url})"
        img_path_list.append(img_path)
    return img_path_list

def custom_make_translation(text, translation):
    regex = re.compile('|'.join(map(re.escape, translation)))
    return regex.sub(lambda match: translation[match.group(0)], text)

def create_file(file_name):
    content = local_article_read(file_name)
    img_list = get_image(file_name)
    if img_list:
        path_list = upload_img(file_name)
        dicts = dict()
        for i,j in zip(img_list,path_list):
            dicts[i]=j
        content = custom_make_translation(content, dicts)
    freebuf_article = open("./freebuf_article/"+file_name, 'w')
    print(f"\033[1;32m[ok]{file_name} create success!\033[0m")
    freebuf_article.write(content)

def main():
    file_list = os.listdir("./local_article/")
    files = "  ".join(file_list)
    usage = r"""
####################################################    
##Easily upload local markdown articles to Freebuf##
##         usage: python3 ToporaToFreebuf.py      ##
##                 Author: Yokan                  ##
####################################################
"""
    print(usage)
    print(f"\033[1;34m[*]scan file_dir: {files}\033[0m")
    for i in file_list:
        if os.path.exists("./freebuf_article/" + i):
            pass
        elif ".assets" in i:
            pass
        else:
            create_file(i)

if __name__ == '__main__':
    main()