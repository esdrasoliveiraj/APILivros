API simples escrita em python com flask para consulta de dados de livros e manipulação dos mesmos para o formato .JSON. As manipulações implementadas são:
 1. consulta de todos os registros ou de um id específico, 
 2. criação de novos registros, 
 3. edição de registros,
 4. exclusão de registros.

A aplicação faz consulta em um banco de dados postgresql através de atributos de conexão passados em um arquivo .JSON existente em um diretório nomeado "databaseConnect".
