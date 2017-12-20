<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>{{titulo}}</h1>
<p>Esta página e desenvolvida usando: Server Linux Ubuntu, Python3.6, Bottle(mini Framework Phython)</p>
  <p>Serviços configurados : MySql, Apache + PHP, Apache TomCat, ssh, ftp.</p>
</div>

<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3>Ip Servidor</h3>
      <p>Ip atual:</p>
      <h4>{{ip_atual}}</h4>
      <br><br>
      <a href="http://{{ip_atual}}:9091/aprender">Aprender mais - Click AQUI</a>
    </div>
    <div class="col-sm-4">
      <img src="{{get_url('static', filename='img/lamp3.png')}}" class="img-rounded" alt="lamp" width="320" height="240">
      <h3>Sevidor Apache (PHP + MYSQL)</h3>
      <a href="http://{{ip_atual}}:8080">HomePage</a>
      <br><br>
      <a href="http://{{ip_atual}}:8080/phpmyadmin">PHPMyADM - MySQL</a>
    </div>
    <div class="col-sm-4">
      <img src="{{get_url('static', filename='img/tomcat.png')}}" class="img-rounded" alt="lamp" width="320" height="240">
      <h3>Apache TomCat</h3>
      <p>Servidor Java TOMCAT</p>
      <a href="http://{{ip_atual}}:8081">HomePage</a>
       <br><br>
      <a href="http://{{ip_atual}}:8081//manager/html">Tomcat Web Application Manager</a>
    </div>
  </div>
</div>

</body>
</html>
