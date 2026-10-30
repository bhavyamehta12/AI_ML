
import math


class MLModel:

    default_framework = "Scikit-learn"
    total_models = 0
    registry = {}

    def __init__(self, name, accuracy, framework=None):

        cls = type(self)

        if not isinstance(name, str):
            raise TypeError("Model name must be a string.")

        name = name.strip()

        if not name:
            raise ValueError("Model name cannot be empty.")

        model_key = name.casefold()

        if model_key in cls.registry:
            raise ValueError("Model name already exists.")

        if not cls.validate_accuracy(accuracy):
            raise ValueError("Invalid accuracy. Must be between 0 and 1.")

        if framework is None:
            framework = cls.default_framework
        else:
            if not isinstance(framework, str):
                raise TypeError("Framework must be a string.")

            framework = framework.strip()

            if not framework:
                raise ValueError("Framework cannot be empty.")

        self.name = name
        self.accuracy = accuracy
        self.framework = framework

        self.accuracy_history = [accuracy]

        cls.registry[model_key] = self
        cls.total_models += 1

    @staticmethod
    def validate_accuracy(accuracy):

        if isinstance(accuracy, bool):
            return False

        if not isinstance(accuracy, (int, float)):
            return False

        try:
            if not math.isfinite(accuracy):
                return False
        except OverflowError:
            return False

        return 0 <= accuracy <= 1

    def update_accuracy(self, new_accuracy):

        if not type(self).validate_accuracy(new_accuracy):
            raise ValueError("Invalid accuracy value.")

        self.accuracy = new_accuracy

        self.accuracy_history.append(new_accuracy)

        return self.accuracy

    def display_info(self):

        return {
            "name": self.name,
            "accuracy": self.accuracy,
            "framework": self.framework,
            "accuracy_history": self.get_accuracy_history()
        }

    def get_accuracy_history(self):

        return self.accuracy_history.copy()

    @classmethod
    def change_default_framework(cls, new_framework):

        if not isinstance(new_framework, str):
            raise TypeError("Framework must be a string.")

        new_framework = new_framework.strip()

        if not new_framework:
            raise ValueError("Framework cannot be empty.")

        cls.default_framework = new_framework

    @classmethod
    def get_best_model(cls):

        if not cls.registry:
            return None

        return max(
            cls.registry.values(),
            key=lambda model: model.accuracy
        )

    @classmethod
    def get_registry_summary(cls):

        framework_count = {}

        for model in cls.registry.values():

            framework_count[model.framework] = (
                framework_count.get(model.framework, 0) + 1
            )

        best_model = cls.get_best_model()

        return {
            "total_models": cls.total_models,
            "default_framework": cls.default_framework,
            "models_by_framework": framework_count,
            "highest_accuracy": (
                best_model.accuracy if best_model else None
            ),
            "best_model": (
                best_model.name if best_model else None
            )
        }


model_a = MLModel("DecisionTree", 0.91)
model_b = MLModel("RandomForest", 0.95)
model_c = MLModel("NeuralNetwork", 0.97)

model_a.update_accuracy(0.94)
model_b.update_accuracy(0.96)

MLModel.change_default_framework("TensorFlow")

model_d = MLModel("DeepLearning", 0.98)

print("\n--- MODEL INFORMATION ---")

for model in MLModel.registry.values():
    print(model.display_info())

print("\n--- BEST MODEL ---")

best = MLModel.get_best_model()

if best:
    print(best.display_info())

print(MLModel.get_registry_summary())
