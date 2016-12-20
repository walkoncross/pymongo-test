#!/usr/bin/env python

import pymongo
import datetime
import pprint

client = pymongo.MongoClient('mongodb://115.238.147.153:27017,115.238.147.141:27017,115.238.147.148:27017')
# client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
#client = pymongo.MongoClient('mongodb://115.238.147.153:27017')
#client1 = pymongo.MongoClient('mongodb://115.238.147.153:27017')
#client2 = pymongo.MongoClient('mongodb://115.238.147.141:27017')
#client3 = pymongo.MongoClient('mongodb://115.238.147.148:27017')

print "===> client.data_names"
pprint.pprint(client.data_names)

print "===> client.database_names()"
pprint.pprint(client.database_names())

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

db = client.test_database
posts = db.posts
post_id = posts.insert_one(post).inserted_id

print "===> db.collection_names(include_system_collections=False)"
pprint.pprint(db.collection_names(include_system_collections=False))

print '===> posts.find_one()'
pprint.pprint(posts.find_one())

print '===> posts.find_one({"author": "Mike"})'
pprint.pprint(posts.find_one({"author": "Mike"}))

print '===> posts.find_one({"author": "Eliot"})'
pprint.pprint(posts.find_one({"author": "Eliot"}))

print '===> post_id: '
pprint.pprint(post_id)

print '===> posts.find_one({"_id": post_id})'
pprint.pprint(posts.find_one({"_id": post_id}))
