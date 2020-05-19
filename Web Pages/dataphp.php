<?php
	//phpinfo();
	system("php database.php");
	echo "Registration Sucessfully...\nRedirecting to Login Page in 2 seconds....";
    header("refresh:2; url=Homepage.html");
?>

