from adapters.dependency_bridge.dependency_bridge_adapter import DependencyBridgeAdapter
from adapters.environment_variable.environment_variable_adapter import EnvrionmentVariableAdapter
from dtos.dependency_injections import DependencyInjections


class GetDependencyInjectionsUsecase:
    def __init__(self):
        self.envrionment_variable_service = EnvrionmentVariableAdapter()
        self.dependency_bridge_service = DependencyBridgeAdapter()

    def call(self) -> DependencyInjections:
        dependency_payload = self.envrionment_variable_service.get_dependency_payload()
        return self.dependency_bridge_service.get_dependency_injections(dependency_payload)

