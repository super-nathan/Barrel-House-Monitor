<html>
<h1>
Mark, Here is the breakdown of the Barrelhouse
<br>
<br>
</h1>

<a href="https://docs.google.com/spreadsheets/d/1iqns2fvvuPCxKjkG7FUaPh74wjkVwvw14kTHXBd5h58/edit?usp=sharing">Click here for the spreadsheet of the trends</a>
<br>
<br>
<br>




<?php
echo "Current Ceiling Temp is: ";
$myfile = fopen("tmp/CeilingTemp.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/CeilingTemp.txt"));
fclose($myfile);
echo "<br>";
echo "Current Ceiling humidity is: ";
$myfile = fopen("tmp/CeilingHumd.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/CeilingHumd.txt"));
fclose($myfile);

echo "<br>";
echo "<br>";

echo "Current Zone 1 Temp is: ";
$myfile = fopen("tmp/Zone1Temp.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone1Temp.txt"));
fclose($myfile);
echo "<br>";
echo "Current Zone 1 humidity is: ";
$myfile = fopen("tmp/Zone1Humd.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone1Humd.txt"));
fclose($myfile);

echo "<br>";
echo "<br>";

echo "Current Zone 2 Temp is: ";
$myfile = fopen("tmp/Zone2Temp.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone2Temp.txt"));
fclose($myfile);
echo "<br>";
echo "Current Zone 2 humidity is: ";
$myfile = fopen("tmp/Zone2Humd.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone2Humd.txt"));
fclose($myfile);

echo "<br>";
echo "<br>";

echo "Current Zone 3 Temp is: ";
$myfile = fopen("tmp/Zone3Temp.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone3Temp.txt"));
fclose($myfile);
echo "<br>";
echo "Current Zone 3 humidity is: ";
$myfile = fopen("tmp/Zone3Humd.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone3Humd.txt"));
fclose($myfile);

echo "<br>";
echo "<br>";

echo "Current Zone 4 Temp is: ";
$myfile = fopen("tmp/Zone4Temp.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone4Temp.txt"));
fclose($myfile);
echo "<br>";
echo "Current Zone 4 humidity is: ";
$myfile = fopen("tmp/Zone4Humd.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("tmp/Zone4Humd.txt"));
fclose($myfile);

if ($_GET['run']) {
  # This code will run if ?run=true is set.
  exec("sudo /usr/bin/spreadsheet.py");
}

?>

<br>
<br>
<br>
<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
<a href="?run=true">Click Me to take a new reading!</a>


</html>
