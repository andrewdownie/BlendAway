<?php
    ///
    /// Read ajax data
    ///
    $method = $_POST["method"];
    $imagesJSON = $_POST["images"];
    $imagesHTML = html_entity_decode($imagesJSON);
    $images = json_decode($imagesHTML);

    ///
    /// Delete the old images
    ///

    echo "[".json_encode($images[0])."]";



?>