# Olá, seja bem vindo ao meu repositório de estudos para o curso de Analytics da DIO.me!

## Desafio relatório de vendas e lucro
<p align="center">
  <img witdh="470" src="DIO.me - PowerBI/Report de Vendas/src/Relatório de vendas.png">
</p>
<p align="center">
  <img witdh="470" src="DIO.me - PowerBI/Report de Vendas/src/Relatório de lucro.png">
</p>

## Desafio de transformação e limpeza de dados
Descrição do desafio módulo 3 – Processamento de Dados Simplificado com Power BI

1. Criação de uma instância na Azure para MySQL
2. Criar o Banco de dados com base disponível no github
3. Integração do Power BI com MySQL no Azure
   R: Em relação a esse requisito do desafio, acabei não conseguindo fazer a integração do PowerBI com um servidor em nuvem.
   Realizei tentativas pelo banco de dados da Azure e de uma plataforma gratuita chamada Aiven, sem sucesso pois na hora de integração com o Power BI um erro era acusado e eu não consegui soluciona-lo, por esse motivo criei um localhost junto ao MySQL.

4. Verificar problemas na base a fim de realizar a transformação dos dados
   R: Foram identificadas inconsistências com o formato dos dados, estas que foram corrigidas diretamente pelo PowerQuery.

Diretrizes para transformação dos dados

1. Verifique os cabeçalhos e tipos de dados - Tipos de dados modificados e corrigidos para a formação do relatório.

2. Modifique os valores monetários para o tipo double preciso - Tipo de dado corrigido.

3. Verifique a existência dos nulos e analise a remoção - Sem necessidade de remoção de nulos, já que a única instância "null" se referia ao supervisor de um colaborador que tinha o cargo de gerente.

4. Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente - Verificado, dados corretos.

5. Verifique se há algum departamento sem gerente - Verificado, tudo ok.

6. Verifique o número de horas dos projetos - Horas corrigidas para o seu devido formato.

7. Separar colunas complexas -  Realizada a transformação dos dados da tabela de colaboradores: A coluna Address continha informações como: Rua, número, cidade e estado. Foi feita a separação
com a mesma lógica porém com uma coluna para cada dado. A estrutura do nome dos colaboradores estava distribuído nas colunas: Fname, Minit e Lname. Criei uma nova coluna concatenando os nomes.

8. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee - Mesclagem feita.

9. Realize a junção dos colaboradores e respectivos nomes dos gerentes - Mesclagem feita diretamente pelo PowerQuery;

10. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único - Mesclagem feita

## Relatório gerado!
<p align="center">
  <img witdh="470" src="DIO.me - PowerBI/Transformação e limpeza de dados/src/transformacao.png">
</p>
