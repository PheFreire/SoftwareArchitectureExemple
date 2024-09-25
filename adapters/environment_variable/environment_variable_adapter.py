from dtos.dependency_payloads import DependencyPayload
import os

class EnvrionmentVariableAdapter:
    def get_dependency_payload(self) -> DependencyPayload:
        return DependencyPayload(os.getenv("ANIMAL_SERVICE", "animal_cachorro_adapter"))

