from dtos.dependency_injections import DependencyInjections
from dtos.dependency_payloads import DependencyPayload


class DependencyBridgeService:
    def get_dependency_injections(self, dependency_payload: DependencyPayload) -> DependencyInjections:
        raise NotImplementedError()

