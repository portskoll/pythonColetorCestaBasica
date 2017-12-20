<!DOCTYPE html>
<html lang="en">
<head>
  <title>Aprenda aqui</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>{{titulo}}</h1>
  <p>Aqui temos varios conteúdos sobre configuração deste servidor Linux Ubuntu</p>
</div>

<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <img src="{{get_url('static', filename='img/pythonlogo.png')}}" class="img-rounded" alt="lamp" width="320" height="240">
      <h3>Sobre Python</h3>
      <h4>Abaixo varios links sobre Python:</h4>
      <a href="http://pingmind.com.br">PingMind</a>
      <p>Otimo site para aprender Python</p>


    </div>
    <div class="col-sm-4">
      <img src="{{get_url('static', filename='img/lamp3.png')}}" class="img-rounded" alt="lamp" width="320" height="240">
      <h3>Sevidor Apache (PHP + MYSQL)</h3>
      <a href="{{get_url('static', filename='pdf/lamp.pdf')}}">Aprenda como instalar</a>

    </div>
    <div class="col-sm-4">
      <img src="{{get_url('static', filename='img/tomcat.png')}}" class="img-rounded" alt="lamp" width="320" height="240">
      <h3>Apache TomCat</h3>
      <p>JDK JAVA - TonCat</p>
      <a href="{{get_url('static', filename='pdf/toncat.pdf')}}">Aprenda como instalar</a>
    </div>
  </div>
</div>

</body>
</html>
