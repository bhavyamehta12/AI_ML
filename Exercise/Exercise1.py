class MLModel:
    total_models=0
    registry={}
    def __init__(self,model_name,accuracy):
        self.validate(accuracy)
        self.model_name=model_name
        self.accuracy=accuracy
        MLModel.total_models+=1
        MLModel.registry={
            "model_name":self.model_name,
            "accuracy":self.accuracy
        }
    @staticmethod
    def validate(accuracy):
        if not isinstance(accuracy,(int,float)) and isinstance(accuracy,bool):
            raise ValueError("Invalid Input")
        if 0<accuracy<1:
            return accuracy
        
    def updating(self,new_value):
        if not 0<new_value<1:
            raise ValueError("Invalid Input")
        if isinstance(new_value,(int,float)) and not isinstance(new_value,bool):
            self.accuracy=new_value
            return self.accuracy
    @classmethod
    def from_config(cls,config):
        pass