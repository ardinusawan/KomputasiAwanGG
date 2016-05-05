from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = '12345678'
DATA_DB_NAME = 'gridfs_server_test'

DATABASE = MongoClient(["localhost:27017"])[DATA_DB_NAME]
POSTS_COLLECTION = DATABASE.posts
USERS_COLLECTION = DATABASE.users
SETTINGS_COLLECTION = DATABASE.settings

DEBUG = True