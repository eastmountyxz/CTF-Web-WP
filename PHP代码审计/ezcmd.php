<?php
if(isset($_GET['ip'])){
  $ip = $_GET['ip'];
  if(preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{1f}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){
    echo preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{20}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match);
    die("fxck your symbol!");
  } else if(preg_match("/ /", $ip)){
    die("no space!");
  } else if(preg_match("/.*f.*l.*a.*g.*/", $ip)){
    die("no flag");
  } else if(preg_match("/tac|rm|echo|cat|nl|less|more|tail|head/", $ip)){
    die("cat't read flag");
  }
  $a = shell_exec("ping -c 4 ".$ip); 
  echo "<pre>";
  print_r($a);
}
highlight_file(__FILE__);
?>
