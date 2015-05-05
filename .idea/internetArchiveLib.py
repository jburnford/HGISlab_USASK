__author__ = 'jimclifford'

import internetarchive
import time
path = "/Users/jimclifford/Documents/botarchive/"
error_log = open('botan-marcs-errors.log', 'a')

search = internetarchive.Search('collection:jstor_botanicalgazette')

for result in search.results():
    itemid = result['identifier']
    item = internetarchive.Item(itemid)
    print item
    meta = item.file(itemid + '_meta.xml')
    print meta
    txt = item.file(itemid[6:] + '_djvu.txt')
    print txt

    try:
       txt.download()
    except Exception as e:
       error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
       print "There was an text error; writing to log."
    try:
        meta.download()
    except Exception as e:
            error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
            print "There was an meta error; writing to log."
    else:
        print "Downloading " + itemid + " ..."
        time.sleep(1)


"""""
for result in search.results():
    itemid = result['identifier']
    item = internetarchive.Item(itemid)
    txt = item.file(itemid + '_djvu.txt')
    try:
       txt.download()
    except Exception as e:
       error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
       print "There was an error; writing to log."
    else:
       print "Downloading " + itemid + " ..."
       time.sleep(1)

error_log.close()

for result in search.results():
    itemid = result['identifier']
    item = internetarchive.Item(itemid)
    marc = item.file(itemid + '_marc.xml')
    marc.download()"""