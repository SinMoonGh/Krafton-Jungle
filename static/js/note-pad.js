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

function memoSave() {
    let url = document.getElementById('article-url').value;
    let comment = document.getElementById('comment').value;

    if (url == "") {
        alert("url을 입력해주세요!");
        return;
    }

    if (comment == "") {
        alert("코멘트를 입력해주세요!");
        return;
    }

    $.ajax({
        type: "POST",
        url: "/api/save",
        data: { url_give: url, comment_give: comment },
        success: function (response) {
            alert(response['msg']);
            location.reload();
        }
    });
}

$(document).ready(function () {
    $("#cards-box").html("");
    showArticles();
});

function showArticles() {
    $.ajax({
        type: "GET",
        url: "/api/memo",
        data: {},
        success: function (response) {
            if (response["result"] == "success") {
                for (let i = 0; i < response["memo_list"].length; i++) {
                    createCard(response["memo_list"][i]);
                }
            }
        }
    })
}

function deleteMemo(id) {
    if (confirm('정말 삭제하시겠습니까?')) {
        $.ajax({
            type: "POST",
            url: "/api/delete",
            data: { id_give: id },
            success: function (response) {
                alert(response['msg']);
                location.reload();
            }
        });
    }
}

function createCard(memo) {
    let card = `<div class="card">
                    <img src="${memo.url_image}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title"><a href="${memo.url}">${memo.url_title}</a></h5>
                        <p class="card-text">${memo.url_description}</p>
                        <p class="card-text"><small class="text-muted">${memo.comment}</small></p>
                    </div>
                    <button id="delete-button" type="submit" class="btn btn-primary" onclick="deleteMemo('${memo._id}')">삭제</button>
                </div>`;

    $("#cards-box").append(card);
}
