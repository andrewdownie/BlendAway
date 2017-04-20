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
    for($i = 0; $i < 20; $i++){
        $imgname = $i.".png";

        if(file_exists($imgname)){
            unlink($imgname);
        }
    }

    $resultImage = "results.jpg";
    if(file_exists($resultImage)){
        unlink($resultImage);
    }

    echo "[".json_encode($images[1])."]";



    ///
    /// Convert Base64 images to filesystem images
    ///



?>