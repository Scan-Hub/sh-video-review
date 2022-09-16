
from models import VideoReviewModel
from config import Config
from bson import ObjectId

class VideoReviewHelper:
    
    @staticmethod
    def get_review(_filter):
        
   
        _reviews = list(VideoReviewModel.find(_filter))
        
        # Replace to embed youtube url
        for review in _reviews:
            if "watch" in review['url']:
                review['url'] = review['url'].replace("watch?v=", "embed/")
            
        return _reviews
    
    
    @staticmethod
    def add_review(_form_data):
        
        _review = {
            **_form_data,
            "created_by": Config.PROJECT
        }
        VideoReviewModel.insert_one(_review)
        
        return _review
    
    
    @staticmethod
    def update_review(_form_data):
        
        _updated = {
            "status": _form_data['status'],
            "updated_by": Config.PROJECT
        }
        VideoReviewModel.update_one(
            filter={ 
               "_id": ObjectId(_form_data['id'])
               },
            obj=_updated)
        
        return _updated