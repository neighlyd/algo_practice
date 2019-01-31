"""
It's important to understand hashing as regards searching, because it lets us do O(1) searches on hash tables.

Open Addressing: When a generated hash collides with an existing hash, walk through the table (circularly) until you
find an open slot to fit your new hash into. This technique is called Linear Probing.

Some problems with Open Addressing are that you can find yourself in a position where hashes don't line up with
their values.  You may often need to iterate through the hash table to find a value as well.

You can also get Clustering, which is where items become clustered around certain values. This will have a cascading
impact on other items being inserted. One way to combat clustering is to skip slots when doing Linear Probing, e.g. every third.
In general, rehash(pos) = (pos + skip) \% sizeoftablerehash(pos)=(pos+skip)%sizeoftable.

It is important that a number be chosen for the skip such that every cell is visited via cycling. This is why prime
numbers are often chosen for hash table sizes.

"""


def gen_hash(astring, tablesize):
    # multiply the ordinal number of the character by its position in a string to prevent collision between anagrams.
    the_sum = sum(ord(c)*idx for idx, c in enumerate(astring))
    return the_sum % tablesize

