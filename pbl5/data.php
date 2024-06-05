<?php

// Database connection parameters
$dbHost="localhost";         
$dbUsername="root";           
$dbPassword="";                
$dbName="sv";   

// Create connection
$conn = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Select data from the table
$sql = "SELECT * FROM your_table";
$result = $conn->query($sql);

// Check if query was successful
if ($result->num_rows > 0) {
    // Start table output
    echo "<table>";
    echo "<thead>";
    echo "<tr>";

    // Get column names
    $row = $result->fetch_assoc();
    foreach ($row as $key => $value) {
        echo "<th>" . $key . "</th>";
    }

    echo "</tr>";
    echo "</thead>";
    echo "<tbody>";

    // Iterate over each row and display data
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        foreach ($row as $key => $value) {
            echo "<td>" . $value . "</td>";
        }
        echo "</tr>";
    }

    echo "</tbody>";
    echo "</table>";
} else {
    echo "No results found";
}

// Close database connection
$conn->close();