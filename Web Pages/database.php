<?php
	//phpinfo();
    //$fullname = $_POST['fullname'];
    //$email = $_POST['email'];
    //$mobilenumber = $_POST['mobilenumber'];
    //$password = $_POST['password'];

    //Database connection
    $conn = mysqli_connect('dbos','Ashish','Maheshwari','mydb') or die(mysqli_error($conn));
    $sqlquery1 = "CREATE TABLE IF NOT EXISTS registration (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,fullname VARCHAR(30) NOT NULL,email VARCHAR(30) NOT NULL , mobilenumber VARCHAR(10) NOT NULL , password VARCHAR(30) NOT NULL)";
    $sqlquery2 = "INSERT INTO registration(fullname, email, mobilenumber, password) VALUES ('$fullname', '$email', '$mobilenumber', '$password')";
    $submit = mysqli_query($conn, $sqlquery2) or die(mysqli_error($conn));
    echo "Registration Sucessfully...\nRedirecting to Login Page in 2 seconds....";
    header("refresh:2; url=Homepage.html");
?>
