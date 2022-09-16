# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, EXCLUDE, RAISE, fields, validate
from schemas.base import ObjectIdField, NotBlank, IsObjectId

_source_type = [
    "youtube"
]

_status_type = [
    "review",
    "enable",
    "disable"
]

_review_type = [
    "video"
]


class VideoReviewSchema(Schema):
    class Meta:
        unknown = RAISE

    form_id = fields.Str(required=True, validate=IsObjectId())
    name = fields.Str(required=True, validate=NotBlank())
    description = fields.Str(required=False)
    url = fields.Str(required=True, validate=NotBlank())
    source = fields.Str(required=False, default="youtube", validate=validate.OneOf(_source_type))
    status =  fields.Str(required=False, default="enable", validate=validate.OneOf(_status_type))
    type = fields.Str(required=False, default="video", validate=validate.OneOf(_review_type))

    
class VideoReviewUpdateSchema(Schema):
    class Meta:
        unknown = RAISE

    id = fields.Str(required=True, validate=IsObjectId())
    status = fields.Str(required=True, validate=validate.OneOf(_status_type))


class VideoReviewItemResponseSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id =  ObjectIdField()
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    description = fields.Str(required=False)
    url = fields.Str(required=True)
    source = fields.Str(required=False, default="youtube")
    form_id = ObjectIdField()



class VideoReviewItemResponseSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    videos =  fields.List(fields.Nested(VideoReviewItemResponseSchema))
  
