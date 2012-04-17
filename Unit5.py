def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return None
    else:
        hashtable_add(htable, key, value)

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_add(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])

def hashtable_get_bucket(htable, keyword)
    return htable[hash_string(keyword, len(htable))]

def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out += ord(s)
    return out % buckets

def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

