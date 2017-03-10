/**
 * Created by LC-3 on 3/8/17.
 */
 $(document).ready(function() {
      console.log("ready()");
   /*
    function vidplay() {
       //var video = document.getElementById("Video1");
      // var button = document.getElementById("play");
       if (video.paused) {
          video.play();
          button.textContent = "||";
       } else {
          video.pause();
          button.textContent = ">";
       }
    }

    function restart() {
     //   var video = document.getElementById("Video1");
        video.currentTime = 0;
    }

//    function skip(value) {
  //      var video = document.getElementById("Video1");
    //    video.currentTime += value;
    //}
   $("#fastForward").on('onclick', fastForward);

    function fastForward() {
        var value = $("#selectTimeValue").val();
        var video = $("#Video1");
        console.log(value);
        video.currentTime += Number(value);
    }
     function rewind() {
        var value = document.getElementById("selectTimeValue").value;
        var video = document.getElementById("Video1");

        video.currentTime -= Number(value);

    }

*/
    //Buttons
    $('menu').on( "click", (displayMenu));

    //Buttons



    var value = $('#selectTimeValue');
    var video = $('#Video1');

    function displayMenu() {
        window.alert("Display Menu")

    }



    console.log("done()");
   });
