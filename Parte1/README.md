 Parte 1: Análise de APKs


```Enunciado:
- Obtenha ao menos 10 APKs de, no mínimo, três categorias diferentes (https://www.apkmirror.com/categories/) para compor seu dataset cru
- Para cada APK coletada, extraia o arquivo AndroidManifest.xml em um diretório "manifests", lembrando de identificar o arquivo resultante (por exemplo, se sua APK se chama 'BancoX-v01.apk', nomeie o manifesto como 'AndroidManifest_BancoX-v01.xml').
- Escreva um script em Python (ou um ipynb) que, dado um diretório como argumento de entrada, retorne a lista de permissões de cada AndroidManifest.xml sob a forma de um dicionário (chave: nome da APK, valor: lista de permissões). Exemplo de saída impressa no terminal desta parte do script:
```

Entrada esperada: Diretório com sample de `AndroidManifest.xml` que serão analisados. 

Saida esperada: A saida esperada pode ser encontrada no arquivo `output.txt`.

- Exemplo de execução:
```
python3 script_A.py <dir> 
```

ou com redirecionando a saída:
```
python3 script_A.py <dir> >> output.txt
```