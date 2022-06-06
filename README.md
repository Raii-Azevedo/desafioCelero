[API]()
 
## Desafio Celero
 
-  O objetivo era criar uma API rest para servir os dados do dataset “120 years of Olympic history: athletes and results” presente no Kaggle:
- The goal was to create a rest API to serve the data from the “120 years of Olympic history: athletes and results” dataset present in Kaggle:

## Tecnologia
 [Requirements](https://github.com/Raii-Azevedo/desafioCelero/blob/master/requirements.txt)
 
 ### Sendo:
 dj-database-url==0.5.0 -> Para auxiliar na migração do DB para o Heroku.


## Processo:
[Models](https://github.com/Raii-Azevedo/desafioCelero/blob/master/desafio/models.py)
![Models](https://github.com/Raii-Azevedo/desafioCelero/blob/master/desafio/images/models.jpeg)
 - Através da classe Base para determinar data-hora e a classe Athlete para configuração dos dados buscados no arquivo csv.

[Serializer](https://github.com/Raii-Azevedo/desafioCelero/blob/master/desafio/serializers.py)
![Serializer](https://github.com/Raii-Azevedo/desafioCelero/blob/master/desafio/images/serializer.jpeg)
- Para indicar os fields a serem lidos nas viiews.

[Views](https://github.com/Raii-Azevedo/desafioCelero/blob/master/desafio/views.py)
![Views](https://github.com/Raii-Azevedo/desafioCelero/blob/master/desafio/images/views.jpeg)
- Através da  função "upload_data" para a leitura do arquivo csv e modelagem.

[urls](https://github.com/Raii-Azevedo/desafioCelero/blob/master/celero/urls.py)
![url](https://github.com/Raii-Azevedo/desafioCelero/blob/master/desafio/images/rotas.jpeg)
- Rotas padrão e de modelagem da views do Django
 
## Links
 
  - Link of deployed application: (Heroku)
  - [Repository](https://github.com/Raii-Azevedo/desafioCelero)
  - [Deploy](https://celero-rai.herokuapp.com/athletes/)

 
 
## Authors
 
* **RAISSA AZEVEDO**: @Raii-Azevedo (https://github.com/Raii-Azevedo)
 
 
