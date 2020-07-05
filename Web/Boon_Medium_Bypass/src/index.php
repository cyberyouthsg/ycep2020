<?php
if(isset($_GET['SRC'])){
	show_source("index.php");
	die();
}
if(isset($_GET['file'])){
	$a = $_GET['file'];
	$b = str_replace("../","",$a);
	if (strpos($b, "Gladiator") !== false){
		include $b;	
	}
}

?>

<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	Truth shall unfold when I GET a SouRCe.<br>
	<!-- Try making a GET request for SRC ?-->
</body>
</html>