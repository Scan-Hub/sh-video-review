# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.health_check import HealthCheck
from resources.video_review import PublicVideoReviewResource
from resources.iapi import iapi_resources

api_resources = {
    '/video': PublicVideoReviewResource,
    '/common/health_check': HealthCheck,
    **{f'/iapi{k}': val for k, val in iapi_resources.items()}
}
