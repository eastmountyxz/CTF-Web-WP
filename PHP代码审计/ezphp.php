<?php
error_reporting(0);
highlight_file(__file__);
$string_1 = $_GET['str1'];
$string_2 = $_GET['str2'];

//1st
if($_GET['num'] !== '23333' && preg_match('/^23333$/', $_GET['num'])){
    echo '1st ok'."<br>";
}
else{
    die('会代码审计嘛23333');
}

//2nd
if(is_numeric($string_1)){
    $md5_1 = md5($string_1);
    $md5_2 = md5($string_2);

    if($md5_1 != $md5_2){
        $a = strtr($md5_1, 'pggnb', '12345');
        $b = strtr($md5_2, 'pggnb', '12345');
        if($a == $b){
            echo '2nd ok'."<br>";
        }
        else{
            die("can u give me the right str???");
        }
    } 
    else{
        die("no!!!!!!!!");
    }
}
else{
    die('is str1 numeric??????');
}

//3nd
function filter($string){
    return preg_replace('/x/', 'yy', $string);
}

$username = $_POST['username'];

$password = "aaaaa";
$user = array($username, $password);

$r = filter(serialize($user));
if(unserialize($r)[1] == "123456"){
    echo file_get_contents('flag.php');
}
会代码审计嘛23333

?>
