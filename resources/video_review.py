# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource

from models import UserModel
from schemas.video_review import VideoReviewItemResponseSchema
from connect import security
from helper.video import VideoReviewHelper

class PublicVideoReviewResource(Resource):

    @security.http(
        login_required=False,
        response=VideoReviewItemResponseSchema()
    )
    def get(self):
        
        _filter = {}
        _reviews_items = VideoReviewHelper.get_review(_filter)
        return {"videos": _reviews_items}

   