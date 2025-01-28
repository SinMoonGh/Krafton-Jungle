function memoCreate() {
    alert("메모 작성 완료!");
}

function onClose() {
    let status = $("#memo-create-form").css("display");

    if (status == "none") {
        $("#memo-create-form").show();
        $("#memo-create-button").text("메모 작성 닫기");
    } else {
        $("#memo-create-form").hide();
        $("#memo-create-button").text("메모 작성하기");
    }
}
