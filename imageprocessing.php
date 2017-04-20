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




    ///
    /// Convert Base64 images to filesystem images
    ///
    function base64_to_jpeg($base64_string, $output_file) {
        $ifp = fopen($output_file, "wb"); 

        $data = explode(',', $base64_string);

        fwrite($ifp, base64_decode($data[1])); 
        fclose($ifp); 

        return $output_file; 
    }

    for($i = 0; $i < count($images); $i++){
        base64_to_jpeg($images[$i], ($i + 1).".png");
    }

    ///
    /// Call python median blending algorithm
    ///
    $scriptName = '/var/www/html/blend.py';
    $options = $method;
    exec ("/usr/bin/python3 {$scriptName} {$options} > /var/www/html/blend_log.txt 2>&1");

    echo "[".json_encode($images[1])."]";
?>