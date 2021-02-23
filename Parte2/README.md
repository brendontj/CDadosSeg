 Parte 2: Análise de arquivos PE


```Enunciado:
- Obtenha alguns binários de Windows (você pode pegá-los do seu próprio computador, se tiver o sistema operacional instalado, ou de sites de download de programas, como sourceforge e outros). Exemplos de binários: calc.exe, ping.exe, paint.exe, netstat.exe...
- Escreva um script em Python (ou .ipynb) que receba como entrada um arquivo ou diretório e enumere a seções executáveis do(s) binário(s), imprimindo na saída padrão um dicionário de listas, onde a chave é o nome do binário e o valor é uma lista de seções executáveis. Dica: https://github.com/erocarrera/pefile
- Escreva outro script em Python (ou .ipynb) que receba como entrada dois arquivos .exe e os compare, imprimindo na saída padrão quais seções são comuns a ambos os binários, quais somente estão presentes no binário 1 e quais somente estão presentes no binário 2. Siga as regras de formato/apresentação já estabelecidas nesta tarefa.
```
- Script A

Entrada esperada: Diretório com sample de `.exe` para extração das seções executáveis ou arquivo `.exe`. 

Saida esperada: A saida esperada pode ser encontrada no arquivo `output_A.txt`.

- Exemplo de execução:
```
python3 script_A.py <dir or file.exe> 
```

ou com redirecionando a saída:
```
python3 script_A.py <dir or file.exe> >> output.txt
```

-- 

- Script B

Entrada esperada: Dois arquivos `.exe` para que a análise de seções aconteça. 

Saida esperada: A saida esperada pode ser encontrada no arquivo `output_B.txt`.

- Exemplo de execução:
```
python3 script_B.py <file1.exe> <file2.exe>  
```

ou com redirecionando a saída:
```
python3 script_B.py <file1.exe> <file2.exe> >> output.txt
```