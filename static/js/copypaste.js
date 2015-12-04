$(document).ready(function(){
    $(document).keydown(function(event) {
        if (event.ctrlKey==true && (event.which == '118' || event.which == '86')) {
            alert('COPY-PASTE is not allowed! This shall be reported to the game admin. Future such event may lead to disqualification.');
            event.preventDefault();
         }
    });
});
