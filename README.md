# **Sistema de Gerenciamento de uma Biblioteca Acadêmica**

![badge-python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![badge-django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![badge-html5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![badge-css3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![badge-javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![badge-jquery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)


Olá a todos, sejam muito bem vindos a mais um projetinho de um aspirante a desenvolvedor de aplicações web. Neste repositório, assim como outros no meu perfil, você encontrará um projeto desenvolvido com o queridíssimo framework django, um pouco de javascript, html, css e claro, bastante python. Neste projetinho eu busquei implementar e exercitar outras tecnologias as quais tenho conhecimento, como JQuery, porém muito pouco por enquanto.

Como o nome sujere e usando como base um projeto desenvolvido em equipe na disciplina de Bancos de Dados do curso de Engenharia de Computação da Universidade Federal do Ceará, este é mais um projeto para o meu portfólio, porém um pouco mais completo e mais complexo do que outros que foram desenvolvidos por mim nesse percurso de tentar se tornar um desenvolvedor web (com conhecimentos em back-end e front-end porém puxando mais para o back-end) utilizando Python como linguagem principal.

Apresento aqui a vocês um pequeno sistema de gerenciamento de uma biblioteca acadêmica com suas entidades básicas (Livros, Autores, Alunos, Professores, Funcionários, Reservas etc.) e seus relacionamentos, implementados, é claro, usando as regras de negócio do django e levando em conta muito do que aprendi até aqui com meus estudos em sala de aula e fora dela. 

Mais adiante mostrarei como instalar o projeto, desde instalar as suas dependencias até executá-lo na sua máquina. Tentarei ser sucinto e ao mesmo tempo cobrir todos os pontos que achar fundamental quanto ao funcionamento do projeto e seus pequenos detalhes.

## **A Estrututa do Projeto**

Antes de apresentar a estrutura básica do projeto, para ser mais didático, explicarei a estrutura basica do framework utilizado para desenvolver esta aplicação, o Django. 

A versão do Django utilizada aqui foi a 4.2, versão esta compativel com o Python 3.9. 

Se você não é programador ou ainda está iniciando nos estudos de programação e não tem uma noção muito clara do que é um framework, do que é o django e como podemos trabalhar com ele, aqui vai uma leve introdução do que foi utilizado nesta aplicação e um pouco do que aprendi no meu tempo de estudo.

Primeiramente iremos começar respondendo a seguinte pergunta: **O que é um framework?** Pois bem, se utilizarmos uma tradução direta das palavras da lingua inglesa que formam essa palavra teremos: Frame = moldura e work = trabalho. Ou seja, framework é uma ferramenta que te dá um molde de trabalho, uma serie de bibliotecas e facilidades que você possa usar para desenvolver sua aplicação, além disso te dá uma receita de bolo de como seguir uma estrutura de organização de diretórios e pacotes e como estes devem se relacionar entre si.

O **Django** é um framework que funciona utilizando o padrão MVT (Model -> View -> Template). Onde os **Models** são classes que descrevem como serão as tabelas do seu banco de dados e os relacionamentos entre elas. As **Views** são funcões ou classes que controlarão diversas funcionalidades da aplicação, inclusive, como e quando os dados do banco de dados serão acessados e modificados. E, por ultimo mas não menos importante, os **Templates** são basicamente páginas HTML renderizadas que serão a porta de entrada do usuário com a aplicação, ou seja, os templates são o front-end da aplicação.


## **Referências**

* [Descrição do Projeto](./docs/Descri%C3%A7%C3%A3o%20do%20Trabalho%20de%20Banco%20de%20Dados.pdf)



