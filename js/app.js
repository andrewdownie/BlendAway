imageList = [] 

$(document).ready(function(){
    ImageListLength()

    $("#Median").click(function(){
        ProcessImages("median", imageList)
    });

    $("#Mean").click(function(){
        ProcessImages("mean", imageList)
    });

    $("#Mode").click(function(){
        ProcessImages("mode", imageList)
    });


    $("#ClearPhotos").click(function(){
        imageList = []
        $("#photoInsertion").html("")
        ImageListLength()
    });

});

function ImageListLength(){
    $("#processingMethodsGroup").hide()

    if(imageList.length < 5){
        $("#photoInsertionText").html("Add more photos, exactly 5 photos are required.")
        $("#photoOutput").html("")
    }
    else if(imageList.length > 5){
        $("#photoInsertionText").html("Too many photos, clear the photos and start over.")
        $("#photoOutput").html("")
    }
    else{
        $("#photoInsertionText").text("")
        $("#processingMethodsGroup").show()
    }

}

// handle input changes
$("#imageSelector").change(function() {
    
    for(var i = 0; i < this.files.length; i++){
        renderImage(this.files[i])
    }

});


// render the image in our view
function renderImage(file) {

  // generate a new FileReader object
  var reader = new FileReader();

  // inject an image with the src url
  reader.onload = function(event) {
    the_url = event.target.result
    imageList.push(the_url)
    $('#photoInsertion').append("<div style='margin-bottom:30px' class='col-md-4'><img style='width:100%; height:20vh' src='" + the_url + "' /></div>")

    ImageListLength()
  }
 
  // when the file is read it triggers the onload event above.
  reader.readAsDataURL(file);
}


function ProcessImages(algo, imageList){
    if(imageList.length < 5){
        alert("Currently EXACTLY 5 photo are required as input. You have " + imageList.length + " input photos. Please add more photos until you have 5.")
        return
    }
    else if(imageList.length > 5){
        alert("Currently EXACTLY 5 photo are required as input. You have " + imageList.length + " input photos. Please clear the photos and start over.")
        return
    }

    $("#outputPhotoHeader").show()
    $("#Loading").show()

    //$("#photoOutput").html(algo)

    if(algo == null || algo == ""){
        console.log("ERROR: algo was empty")
    }

    $.ajax({
        type: "POST",
        url: "/imageprocessing.php",
        data: {
            "method": algo,
            "images": JSON.stringify(imageList)
        },
        error: function(xhr, status, error) {
            alert("AJAX ERROR:: " + error);    

        }
    
    }).done(function(response) {
        $("#Loading").hide()
        console.log(response)
        
       images = JSON.parse(response)

        for(var i = 0; i < images.length; i++){
            $("#photoOutput").html("<div class='col-md-12'><img style='width:100%;' src='" + images[i] + "' /></div>")
        }

    });
}