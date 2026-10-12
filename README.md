# Atividade de Aula — Fluxograma

Tela de fluxograma de Engenharia de Computação integrada ao Django.
Estrutura adaptada do projeto de login fornecido como referência.
O HTML e CSS são os arquivos da tela de fluxograma já testada localmente.

## Executar no Windows

Requer Python compatível com Django 6.1.2 (o ambiente usado na atividade anterior).
Abra esta pasta no VS Code e execute no PowerShell:

```powershell
python -m venv ENG4021
.\ENG4021\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cd fluxograma
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/fluxograma/ ou http://127.0.0.1:8000/.
Se já houver um servidor usando a porta 8000, encerre-o antes ou rode
`python manage.py runserver 8001` e acesse a porta 8001.

## Arquivos principais

- `fluxograma/fluxograma/urls.py`: rotas.
- `fluxograma/fluxogramaapp/views.py`: função que renderiza a tela.
- `fluxograma/fluxogramaapp/templates/fluxograma.html`: HTML.
- `fluxograma/fluxogramaapp/static/fluxograma.css`: CSS.

O projeto serve para execução local de aula, com DEBUG ativado e chave de desenvolvimento.
As marcações da tela não são salvas entre acessos. A publicação do código no
GitHub não hospeda o servidor Django: o link de entrega é o do repositório.
