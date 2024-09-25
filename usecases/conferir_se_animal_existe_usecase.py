from services.animal_service import AnimalService


class ConferirSeAnimalExisteUsecase:
    def call(self, animals_service: list[AnimalService]) -> bool:
        return any(animals_service)

