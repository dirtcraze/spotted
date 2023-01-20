title = document.getElementsByClassName('label-text')[0]
tip = document.getElementsByClassName('tip')[0]
input = document.getElementById('input-1')

window.addEventListener("load", function() {
    input.style.opacity = "1";
    input.style.transform = "translate(-50%, -100%)";
    input.style.pointerEvents = "auto";
    input.style.transition = "all .4s cubic-bezier(.1, .45, .1, .85) .5s";
    input.style.zIndex = "10";
    tip.style.opacity = "1";
    title.style.opacity = "1";
    title.style.transform = "translate(-50%, -100%)";
    title.style.transition = "all .3s cubic-bezier(.1, .45, .1, .85) .4s";
});

  $(document).ready(function() {
    $("#form").submit(function(e) {
      e.preventDefault();
      $.ajax({
        type: "POST",
        data: $("#form").serialize(),
        success: function() {
          $("#form")[0].reset();
        }
      });
    });
  });