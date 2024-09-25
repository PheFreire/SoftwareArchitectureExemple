from services.animal_service import AnimalService


class AnimalGatoAdapter(AnimalService):
    def falar(self, texto: str) -> str:
        return "mia" + "u" * len(texto)


