<!DOCTYPE html>
<html>
<head>
    <title>MD5 Hash Generator 2.0</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }

        h1 {
            text-align: center;
            background-color: #007bff;
            color: #fff;
            padding: 20px;
            margin: 0;
        }

        p {
            text-align: center;
            margin-top: 10px;
        }

        form {
            text-align: center;
            margin-top: 20px;
        }

        label {
            font-weight: bold;
        }

        input[type="text"] {
            width: 300px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        input[type="submit"] {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }

        p.result {
            text-align: center;
            font-size: 18px;
            margin-top: 20px;
        }

        .error {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>MD5 Hash Generator 2.0</h1>
    <p>FREE STRING HASH GENERATOR!</p>
    <form method="post">
        <label for="input">Enter Text:</label>
        <input type="text" name="input" id="input" required>
        <input type="submit" value="Generate MD5 Hash">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $input = $_POST["input"];
        // Sanitize user input to block /
        if (strpos($input, '/') !== false) {
            echo "<p class='error'>Bad command</p>";
        } else if(strpos($input, 'bash') !== false){
        }else {
	    $input = urldecode($input);	
            $command = 'echo ' . $input . ' | md5sum ';
            ob_start();
            system($command, $return_var);
            $md5Hash = ob_get_clean();
            echo "<p class='result'>MD5 Hash: $md5Hash</p>";
        }
    }
    ?>
</body>
</html>
