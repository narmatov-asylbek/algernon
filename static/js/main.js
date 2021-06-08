
$( document ).ready(function() {

    var modal = document.getElementById("myModal");


    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }



    function upload(event) {
        event.preventDefault();
        var data = new FormData($('form').get(0));

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: data,
            csrfmiddlewaretoken: csrftoken,
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
                modal.style.display = "block";
                document.getElementById('modal_content').classList.add('success_modal')
            },
            error: function (data) {
                modal.style.display = "block";
            }
        });
        return false;
    }

    $(function () {
        $('#update_book_form').submit(upload);
    });
    $(function () {
        $('#update_cycle_settings').submit(upload);
    });
})