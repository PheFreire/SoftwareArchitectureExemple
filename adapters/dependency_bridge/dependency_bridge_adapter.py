from adapters.animal_service.animal_cachorro_adapter import AnimalCachorroAdapter
from adapters.animal_service.animal_gato_adapter import AnimalGatoAdapter
from dtos.dependency_injections import DependencyInjections
from dtos.dependency_payloads import DependencyPayload


class DependencyBridgeAdapter:
    def __init__(self):
        self.adapters = {
            "animal_cachorro_adapter": AnimalCachorroAdapter(),
            "animal_gato_adapter": AnimalGatoAdapter(),
        }

    def get_dependency_injections(self, dependency_payload: DependencyPayload) -> DependencyInjections:
        animal_adapter = self.adapters[dependency_payload.animal_service]
        return DependencyInjections(animal_adapter)

