# IA como Assistente no Treinamento para Maratonas de Programação e Olimpíadas — códigos

Códigos em Python do capítulo do minicurso apresentado no XIV ERCEMAPI 2026.
Eles são publicados aqui porque a indentação, essencial em Python, pode se perder ao copiar código de um PDF.

Todos foram testados com Python 3.13. Para executar um código com um dos exemplos:

```
python3 codigo_1_2_tabuas.py < exemplos/1_2.txt
```

Também é possível digitar a entrada no terminal. Nesse caso, depois da última linha, encerre a entrada com `Ctrl+D` (Linux e macOS) ou `Ctrl+Z` seguido de `Enter` (Windows); sem isso, os Códigos 1.2, 1.5 e 1.6 ficam esperando, porque leem a entrada inteira de uma vez.

| Arquivo | No capítulo | Exemplo | Saída esperada |
| --- | --- | --- | --- |
| `codigo_1_1_media_com_bug.py` | Código 1.1 (Seção 1.5.6) | `exemplos/1_1_pequeno.txt` | `8` |
| | | `exemplos/1_1_grande.txt` | `1000000000000000000` (o correto seria `999999999999999999`) |
| `codigo_1_2_tabuas.py` | Código 1.2 (Seção 1.6.2) | `exemplos/1_2.txt` | `200` |
| `codigo_1_3_troco.py` | Código 1.3 (Seção 1.6.3) | `exemplos/1_3.txt` | `2` |
| `codigo_1_4_bfs_grade.py` | Código 1.4 (Seção 1.6.4) | `exemplos/1_4.txt` | `6` |
| `codigo_1_5_problema_A.py` | Código 1.5 (Apêndice) | `exemplos/1_5.txt` | `2`, `4`, `0` |
| `codigo_1_6_problema_B.py` | Código 1.6 (Apêndice) | `exemplos/1_6.txt` | `4`, `3`, `0` |

**Atenção:** o Código 1.1 contém um erro proposital, usado no capítulo como exemplo de depuração guiada.

**Para instrutores:** os Códigos 1.5 e 1.6 são as soluções dos problemas da atividade prática. Não os mostre aos participantes antes da atividade.
