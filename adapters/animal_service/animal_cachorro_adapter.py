from services.animal_service import AnimalService


class AnimalCachorroAdapter(AnimalService):
    def falar(self, texto: str) -> str:
        div = texto.split(" ")
        div = ["auau" for _ in div]
        return " ".join(div)


