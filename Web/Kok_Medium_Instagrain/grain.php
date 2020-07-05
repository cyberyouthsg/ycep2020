<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Instagrain</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    </script>
  </head>
  <body>
<div class="container">

  <?php error_reporting(0); ?>

   <!-- Page Layout here -->
   <div class="row">

     

     <div class="col s12">
       <h3>Instagrain</h3>
       <b>The New-Gen Social Network for Farmers</b>
       <p>Welcome to your Instagrain account upload page! You can upload all your images of grain here :) (We only accept images! Don't play play :))</p>
       <div class="card red lighten-1">
            <div class="card-content white-text">
              <span class="card-title">Upload</span>
              <form enctype="multipart/form-data" action="grain.php" method="POST">
                <input type="hidden" name="MAX_FILE_SIZE" value="100000" />
                <input name="uploadedfile" type="file" />
                <input type="submit" value="Upload File" />
              </form>

            </div>
            <div class="card-action">
              <?php
                    $imageinfo = getimagesize($_FILES['uploadedfile']['tmp_name']);
                    if($imageinfo['mime'] != 'image/gif' && $imageinfo['mime'] != 'image/jpeg') {
                    if(isset($_FILES['uploadedfile'])){echo "Sorry, we only accept GIF and JPEG images\n";}
                    exit;
                    }
                    $uploaddir = 'uploads/';
                    $uploadfile = $uploaddir . basename($_FILES['uploadedfile']['name']);
                    if (move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $uploadfile)) {
                    echo "File is valid, and was successfully uploaded.\n";
                    } else {
                    echo "File uploading failed.\n";
                    }
                ?>
                <?php if($uploadfile!= '') { echo "<b><a href=\"$uploadfile\">See your new post here!</a></b>"; } ?>
            </div>
          </div>

     </div>

   </div>

</div>
  </body>
</html>
