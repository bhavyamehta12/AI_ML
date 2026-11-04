class Model():  
    total_model=0
    def __init__(self, model_name, learning_rate, model_status):
        self.validation(model_name, learning_rate, model_status)

        self.model_name = model_name
        self.__learning_rate = learning_rate
        self.model_status = model_status

        self.config = {
            "model_name": model_name,
            "learning_rate": learning_rate,
            "model_status": model_status
        }

        Model.total_model += 1
    @property
    def learning_rate(self):
        return self.__learning_rate

    @learning_rate.setter
    def learning_rate(self, new_value):
        if isinstance(new_value, (int, float)) and not isinstance(new_value, bool) and 0 < new_value <= 1:
            self.__learning_rate = new_value
        else:
            raise ValueError("Learning rate must be between 0 and 1")
    @classmethod
    def from_config(cls, config):

        if not isinstance(config, dict):
            raise TypeError("Configuration must be a dictionary")

        required_keys = ["model_name", "learning_rate", "model_status"]

        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing configuration: {key}")

        return cls(
            model_name=config["model_name"],
            learning_rate=config["learning_rate"],
            model_status=config["model_status"]
        )
        
        
    @staticmethod
    def validation(model_name,learning_rate,model_status):
        if not isinstance(learning_rate,(int,float)) or isinstance(learning_rate,(bool)):
          raise ValueError("Invalid Input")
        if not isinstance(model_name,str) or len(model_name.strip())<=0:
          raise ValueError("Invalid Input")
        if model_status!="Active" and model_status!="Inactive":
          raise ValueError("Invalid Input")
        if 0<learning_rate<=1:
          return learning_rate,model_status,model_name
        else:
            raise ValueError("Invalid Input")
class TrainableModel(Model):
    def __init__(self, model_name, learning_rate, model_status):
        super().__init__(model_name, learning_rate, model_status)
        self.training_status="Not Trained"
    def train(self,X,y):
        if self.model_status=="Inactive":
            raise ValueError("Not Active")
        if len(X)==0 or len(y)==0:
            raise ValueError("Invalid input")
        if len(X)!=len(y):
            raise ValueError("Invalid input")
        
        self.training_status="Training"

class Logger():
    def __init__(self,model_name, learning_rate, model_status):
        super().__init__(model_name, learning_rate, model_status)
        self.logs=[]
    def log_event(self,event):
        self.logs.append(f"{self.model_name}-{event}")
    def show_logs(self):
        return self.logs

class DecisionTree(Logger,TrainableModel):
    def train(self, X, y):
        self.log_event("Training Started")

        try:
            super().train(X, y)

            self.training_status = "Trained"
            self.log_event("Training Completed")

        except Exception:
            self.training_status = "Failed"
            self.log_event("Training Failed")
            raise

        
class RandomForest(Logger,TrainableModel):
    def train(self, X, y):
        self.log_event("Training Started")

        try:
            # Common validation and training workflow
            super().train(X, y)

            # Simulate DecisionTree-specific training
            # Actual algorithm will be implemented later

            self.training_status = "Trained"
            self.log_event("Training Completed")

        except Exception:
            self.training_status = "Failed"
            self.log_event("Training Failed")
            raise
    