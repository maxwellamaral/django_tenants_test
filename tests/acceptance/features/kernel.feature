# Created by max at 25/08/2022
Feature: Executando testes
  Para provar que o behavior-django funciona
  Como o Mantenedor
  Eu quero testar o comportamento de execução neste diretório

  Scenario: O Teste
    Given Dado que este passo existe
    When Quando eu executar 'python manage.py behave'
    Then Então eu deveria ver os testes de comportamento serem executados
