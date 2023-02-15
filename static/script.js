function ajaxError() {
    requestOver();
    alert('ajax error');
}

function ajaxSuccess(result) {
    if (result.error) {
        alert('操作失败');
        return;
    }
    location.reload();
}
function handleASKSucc(result) {
     requestOver()

    if (result.error) {
        alert('操作失败');
        return;
    }
      $("#text").text('');
    let str=result.result;
      var newStr = str.replace(/\n/g, "<br>");
      $(".result").html(newStr);
}


function beginTranslation() {
    let eassy = $("#text").val()
    let lang = $("#lang").val()
    var data = JSON.stringify({'text': eassy, 'lang': lang});

    $.ajax({
        'url': '/api/Traslation',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': handleSucc
    });
    return false;
}
function beginAsk() {
    let eassy = $("#text").val()
    var data = JSON.stringify({'yourWant': eassy});
    beginHandleAskButtons()
    $.ajax({
        'url': '/api/',
        'type': 'POST',
        'contentType': 'application/json',
        'data': data,
        'dataType': 'json',
        'error': ajaxError,
        'success': handleASKSucc
    });
    return false;
}
function requestOver() {
    let ab=$("#submit");
    if (ab){
      ab.show()
    }
   $("#tishi").hide()
        $("#result").show()

}
function  beginHandleAskButtons(){
    $("#submit").hide()
    $("#tishi").show()
    $("#result").hide()
}
function handleSucc(result) {
    if (result.error) {
        alert('操作失败');
        return;
    }
    $(".result").text(result.result);
}

