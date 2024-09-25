# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Interface -> Abstração que define a assinatura de um metodo ou estrutura de dados

DTO ou Dataclasses -> Interface de uma classe de estrutura de dados
Service -> Interface de uma classe de métodos

Adapter -> Implementação de uma interface service

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Entrypoints: Gatilho de ativação de um fluxo (Chamam um controller) 

Groups (Controllers): Abstração acima dos fluxos que permite a interação e agrupação dos mesmos, é onde ocorre a injeção de dependencia "controllers/animais_conversam_controller.py" 
 
Fluxos ou Usecases: Abstração acima dos serviços, que permite a interação e agrupamento dos mesmos e é nela onde definimos a entrada da injeção de dependencia
  
Services: Nivel mais baixo de abstração, onde compoem a interface das funções que realizam processos no nosso fluxo
  
Adapters: Impementação das interfaces (são elas que serão injetadas)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## Hot Topics:
- A estrutura de dados mais segura por conseguir manter a sua assinatura de entrada é a dataclasse
- As unicas abstrações que podem ter dependencias são os Entrypoints e os Adapters
- A injeção de dependencia é sempre recebida no metodo inicialziador de uma classe usecase
    -  Um usecase bem feito tem:
        - a classe segue o principio de responsabilidade unica
        - o nome da classe é auto explicativa com o comportamento unico da classe (Metodo) 
        - apena um metodo que é chamado de "call"

