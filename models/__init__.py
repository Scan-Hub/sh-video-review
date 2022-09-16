# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from config import Config
from lib import DaoModel, AsyncDaoModel
from connect import connect_db, redis_cluster, asyncio_mongo

__models__ = ['']

from models.user import UserDao

UserModel = UserDao(connect_db.db.users, redis=redis_cluster) # broker for write db with queue

VideoReviewModel = UserDao(connect_db.db.video_review, redis=redis_cluster)

# AsyncUserModel = AsyncDaoModel(asyncio_mongo.db.users)
