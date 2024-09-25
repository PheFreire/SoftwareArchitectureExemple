from dtos.dependency_payloads import DependencyPayload


class EnvrionmentVariableService:
    def get_dependency_payload(self) -> DependencyPayload:
        raise NotImplementedError()

