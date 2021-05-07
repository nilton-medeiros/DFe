# DFe

### API REST FULL DFe - Documento Fiscal Eletrônico em DRF

Webservice (API) para emissão de Documentos Eletrônicos Fiscais (DFe)
- [ ] NFe
- [ ] NFCe
- [ ] CTe
- [ ] MDFe

## Dependências

- [Python](https://www.python.org/downloads/ "Python Download") - Versão 3.7.10 (security)
- [Django](https://www.djangoproject.com/download/ "Django Download") - Versão 3.2 LTS
- [DjangoRestFramework](https://www.django-rest-framework.org/ "Django REST Framework")
- [Python-Decouple](https://pypi.org/project/python-decouple/ "Python-decouple")
- [dj-database-url](https://pypi.org/project/dj-database-url/ "Use Database URLs in your Django Application")
- [PyNFe](https://github.com/msbrogli/PyNFe/ "pip install git+https://github.com/msbrogli/PyNFe") - Atualizado para a versão 4.00 NF-e/NFC-e  
(pip install git+https://github.com/msbrogli/PyNFe)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/nilton-medeiros/DFe.git
cd DFe
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```
