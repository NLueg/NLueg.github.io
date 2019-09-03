# !/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
import collections

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')

tags_dict = {}
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'categories:':
                tmp_tags = current_tags[1:]

                for item in tmp_tags:
                    if item in tags_dict:
                        tags_dict[item] += 1
                    else:
                        tags_dict[item] = 1
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(tags_dict)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:

    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Category: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())

total_tags_string = "\n    "
tags_dict_ordered = sorted(tags_dict.items(), key=lambda x: x[0].lower())

for i, j in sorted(tags_dict.items(), key=lambda x: x[0].lower()): 
    print(i, j)

indent = "    "

for tag, count in tags_dict_ordered:
    total_tags_string += "- " + tag + "," + str(count) + "\n" + indent


filename = "categories.md"
old_categories = glob.glob(filename)
for tag in old_categories:
    os.remove(tag)

f = open(filename, 'a')

layout = "layout: categories"
titles = "title: \"Available Categories\""
categories = "categories: " + total_tags_string
description = "description: On this page you can find every tag that were used in different posts."
permalink = "permalink: /categories/"
pagination = "pagination:\n" + indent + "enabled: true" #\n" + indent "per_page: '5'"

write_str = '---\n' + layout + '\n' + titles + '\n' + permalink + '\n' + categories + '\n' + description + '\n' + pagination + '\n---\n'
f.write(write_str)
f.close()
