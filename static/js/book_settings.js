var modal = document.getElementById("myModal");


window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

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


$("#delete_cycle_button").click(function () {
    let object_id = $(this).attr('data-object-id');
    let url = `${object_id}/delete/`;

    $.ajax({
        url: url,
        type: 'post',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        success: function (data) {
            alert('it worked')
        },
        failure: function (data) {
            alert('Got an error dude');
        }
    })
})
