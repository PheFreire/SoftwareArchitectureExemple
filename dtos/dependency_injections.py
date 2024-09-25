from dataclasses import dataclass

from services.animal_service import AnimalService

@dataclass
class DependencyInjections:
    animal_service: AnimalService

