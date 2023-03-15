<h1 align="center">To Do List</h1>

<h3 align="center">Site de Gerenciamento de Tarefas Concluídas e Não Concluídas</h3> 
<div align="center">

![My Skills](https://skills.thijs.gg/icons?i=python,django,vue,html,js,css)

</div>

<div align="center">

[![Deploy on Railway](https://railway.app/button.svg)](https://todolisteudson.up.railway.app/)

</div>

## Tópicos

1. [Sobre o projeto](#sobre-o-projeto)
2. [Tecnologias usadas](#tecnologias-usadas)
3. [Layout](#layout)
4. [Instalar o projeto localmente](#instalar-o-projeto-localmente)
5. [Licença](#license)

## Sobre o projeto

Eu criei esse projeto com o objetivo de praticar vue.js, uma tecnologia que estava estudando. Inicialmente, o projeto seria apenas em vue.js, mas decidi criar uma API com o Django REST Framework para consumir.

Mesmo o front-end e o back-end funcionando de forma independente, eles estão no mesmo repositório. Decidi fazer isso para facilitar a hospedagem do projeto em uma plataforma que oferece hospedagem gratuita, como o Railways. Para fazer isso, executei o comando <code>npm run build</code>, gerando uma pasta "dist" contendo todos os arquivos estáticos e configurei o Django para redirecionar para essa pasta.

## Tecnologias usadas

<ul>
  <li>Back-end</li>
  
   <ul>
      <li>Python</li>
      <li>Djando Rest framework</li>
      <li>PostgreSQL</li>
   </ul>
   
  <li>Front-end</li>
  
  <ul>
      <li>Javascript</li>
      <li>Vue.js</li>
      <li>Html</li>
      <li>Css</li>
  </ul>
  
</ul> 

## Layout

### Web

<img src="https://github.com/SobrancelhaDoDragao/To_Do_List/blob/main/Web.png" width="500">

### Mobile
#instalar-o-projeto-localmente
<img src="https://github.com/SobrancelhaDoDragao/To_Do_List/blob/main/mobile.png">

## Instalar o projeto localmente

### Pré-requisitos

- [Python 3.8.10](https://www.python.org/downloads/)
- [Venv](https://docs.python.org/pt-br/3/library/venv.html)

### Execute os seguintes comandos

1. Baixe o repositório no seu computador
2. Agora abra a pasta 'Django' pelo terminal
3. Digite: <code>python -m venv env</code>, para criar um ambiente virtual para instalar as bibliotecas
4. Ative o ambiente virtual: <code>source env/bin/activate</code>
5. Agora digite: <code>pip install -r requirements.txt</code>, para instalar as bibliotecas
6. E finalmente rode o projeto:<code>python manage.py runserver</code>

### Configurando Banco de dados
xeḱde

## License

The scripts in this project are released under the [MIT License](./LICENSE.md) 
