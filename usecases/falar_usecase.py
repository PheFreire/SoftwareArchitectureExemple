from services.animal_service import AnimalService


class FalarUsecase:
    # Aqui ele está definindo uma entrada para uma injeção de dependencia
    def __init__(self, animal_service: AnimalService):
        self.animal_service = animal_service

    def call(self, texto: str) -> str:
        return self.animal_service.falar(texto)
