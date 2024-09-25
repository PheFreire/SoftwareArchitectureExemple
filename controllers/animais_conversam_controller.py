from usecases.get_dependency_injections_usecase import GetDependencyInjectionsUsecase
from usecases.falar_usecase import FalarUsecase

class AnimaisConversamController:
    def call(self):
        text = input("-> ")

        dependency_injections_usecase = GetDependencyInjectionsUsecase()
        dependency_injections = dependency_injections_usecase.call()
       
        # Recebendo injeção de dependencia
        falar_usecase = FalarUsecase(dependency_injections.animal_service)
        print(falar_usecase.call(text))
