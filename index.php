<?PHP
$content = "";

if (count($_GET) != 0)
{
	$content = "?";
}

foreach($_GET AS $key => $value)
{
	$content .= $key . "=" . $value . "&";
}

$content = rtrim($content, '&'); 

header('Location: index.py'.$content);
?>
