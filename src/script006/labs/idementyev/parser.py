import os
import re
import time

start_time = time.time()

# number of unique URLs to get from file
uniq_number = 10

directory = "C:/_share"
filename = "all.log"

# sanity checks
req_file = os.path.abspath(os.path.normpath(os.path.join(directory, filename)))

# re for URL
url_re = "\[[-_a-zA-Z0-9/а-яА-Я ]+\] "
url_re = re.compile(url_re)

url_popularity = {}

# open file
with open(req_file, encoding='utf-8') as rf:
    # get URL from every line
    lines = rf.readlines()
    # print("Lines in file: {}".format(len(lines)))
    matches = 0
    skips = 0
    matched = []
    skipped = []
    for line in lines:
    #for i, line in enumerate(lines):
        # everybody loves pretty debug
        # if i % 10000 == 0:
        #     print(".", end="")
        # if i % 500000 == 0:
        #     print("X")

        # split by '] '
        sections = line.split('] ')
        try:
            url = sections[4] + "] "
        except IndexError:
            # most likely \n in the line
            skips += 1
            skipped.append(sections)
        else:
            if url_re.match(url):
                matches += 1
                matched.append(url)
                try:
                    url_popularity[url] += 1
                except KeyError:
                    url_popularity[url] = 1

            #else:
                #print("Not able to match: {}".format(url))

parsed = matches + skips
print("\nMatches: {}\nSkips: {} ({:.3f}%)\nParsed: {}".format(matches,
                                                              skips,
                                                              skips / parsed,
                                                              parsed))

uniq = list(set(matched))
print("Found unique URLs: {}".format(len(uniq)))

# for every unique count number of times it's found and append to dict

print("Done with popularity contest\n")

# now we have a dict with a unique key and number as a value
# sort it by value and place in a tuple
popular = sorted(url_popularity.items(), key=lambda kv: kv[1], reverse=True)

# to be sure we did not miss any
total = 0
print("Top {} popular URLs:".format(uniq_number))
for _, p in enumerate(popular):
    if _ > uniq_number:
        break
    print("{number:>6d}  {url}".format(number=p[1], url=p[0].rstrip()[1:-1]))
    total += p[1]

print("{} top unique are {:.2f}%: {}/{}".format(uniq_number,
                                                total / matches * 100,
                                                total, matches))

print("--- %s seconds ---" % (time.time() - start_time))
