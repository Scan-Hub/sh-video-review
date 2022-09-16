# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource

from models import UserModel
from schemas.video_review import VideoReviewItemResponseSchema, VideoReviewSchema, VideoReviewUpdateSchema
from connect import security
from helper.video import VideoReviewHelper

class VideoReviewResource(Resource):

    @security.http(
        login_required=False,
        response=VideoReviewItemResponseSchema()
    )
    def get(self):
       
        _filter = {}
        _reviews_items = VideoReviewHelper.get_review(_filter)
        return {"videos": _reviews_items}

    @security.http(
        form_data=VideoReviewSchema(), 
        login_required=False  # user
        
    )
    # def post(self, form_data, user):
    def post(self, form_data):
    
        VideoReviewHelper.add_review(form_data)
        return {}
    
    @security.http(
        form_data=VideoReviewUpdateSchema(),  # form_data
        login_required=False  # user
    )
    # def put(self, form_data, user):
    def put(self, form_data):
    
        VideoReviewHelper.update_review(form_data)
        return {}

