// Czyszczenie pola tekstowego po wysłaniu wiadomości
$('#message-area').val('');

// Autodopasowywanie wysokości pola tekstowego
autosize(document.querySelector('textarea'));

// Nasłuchiwanie wysyłania formularza
$(document).ready(function() {
    $("#form").submit(function(e) {
        // Zatrzymanie domyślnego zachowania formularza
        e.preventDefault();
        $.ajax({
            type: "POST",
            data: $("#form").serialize(),
            success: function() {
                $("#counter").text("0/600 znaków");
                // Czyszczenie formularza
                $("#form")[0].reset();
                // Powrót do domyślnej wysokości pola tekstowego
                $("#message-area")[0].style.height = '55px';
                // Dodanie div z komunikatem o wysłaniu wiadomości
                $("#alert-box").append(successAlert);
                successAlert.hide().fadeIn(1000);
            },
            error: function() {
                // Dodanie div z komunikatem o błędzie wysłania wiadomości
                $("#alert-box").append(successAlert);
                dangerAlert.hide().fadeIn(1000);
            }
        });
    });
});

// Tworzenie div z komunikatem o wysłaniu wiadomości
var successAlert = $("<div>", {
    class: "alert success-alert",
    html: "<h3>Wiadomość została wysłana</h3><a class=\"close\">&times;</a>"
});

// Tworzenie div z komunikatem o błędzie
var errorAlert = $("<div>", {
    class: "alert error-alert",
    html: "<h3>Wystąpił problem z wysłaniem</h3><a class=\"close\">&times;</a>"
});

// Nasłuchiwanie kliknięcia na przycisk "x"
$("body").on("click", ".close", function(){
    // Usuwanie div z komunikatem po kliknięciu na przycisk "x"
    $(this).closest("div.alert").fadeOut(1000, function(){
        $(this).remove();
    });
});

// Automatyczne usuwanie div z komunikatem po 3 sekundach
setInterval(function(){
    $("div.alert").fadeOut(1000, function(){
        $(this).remove();
    });
}, 9000);


$(document).ready(function() {
    $("#message-area").on("input", function() {
        $("#counter").text($(this).val().length + "/600 znaków")
    });
});

$(document).ready(function(){
  var colors = ['#111E25', '#1a1a1a', '#111'];
  var randomColor = colors[Math.floor(Math.random() * colors.length)];
  $('body').css('background', 'linear-gradient(to bottom right, ' + randomColor + ' 0%, #111 100%)');
});