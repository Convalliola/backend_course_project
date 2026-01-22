from models.predict import PredictRequest
from errors import BusinessLogicError

class ModerationService:
    def predict(self, req: PredictRequest) -> bool:
        """
        True есть нарушение
        False нарушений нет
        """

        # # для теста бизнес-ошибки
        # if req.name.strip().lower() == "__raise__":
        #     raise BusinessLogicError("Simulated business logic error")

        if req.is_verified_seller:
            return False

        if req.images_qty > 0:
            return False

        return True