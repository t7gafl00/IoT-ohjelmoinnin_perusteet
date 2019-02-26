<!DOCTYPE html>
<html lang="en">

<head>
    <title>IoT</title>
    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="<?php echo base_url(); ?>bootstrap-4.1.3-dist\css\bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="<?php echo base_url(); ?>bootstrap-4.1.3-dist\js\bootstrap.min.js">

    <link rel="stylesheet" href="<?php echo base_url(); ?>css/own.css">

    <!-- PWA enabled -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <!-- Disable zooming -->
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
    <!-- App icon -->
    <link rel="apple-touch-icon" href="<?php echo base_url(); ?>images\apple-touch-icon.png">
    <!-- Disable opening urls in Safari -->
    <script type="text/javascript">
    var iWebkit;if(!iWebkit) {
        iWebkit=window.onload=function() {
            function fullscreen() {
                var a=document.getElementsByTagName("a");
                for(var i=0;i<a.length;i++) {
                    if(a[i].className.match("noeffect")) {}
                    else {
                        a[i].onclick=function() {
                            window.location = this.getAttribute("href");
                            return false}
                        }
                    }
                }
                function hideURLbar() {
                    window.scrollTo(0,0.9)
                }
                iWebkit.init = function() {
                    fullscreen();
                    hideURLbar()
                }
                ;
                iWebkit.init()
            }
        }
    </script>

    <!-- Automatically refresh page every 15 seconds -->
    <meta http-equiv="refresh" content="15">

</head>

<body style="position: fixed">  <!-- Disable scrolling-->
