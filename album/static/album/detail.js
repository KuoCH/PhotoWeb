function refresh_picture(){
    $.ajax({
        type: "GET",
    url: "/album/pictures/"+picture_id
    }).done(function(resource){
        document.getElementById("title").innerHTML = resource.title;
        document.getElementById("img").src = '/media/'+resource.image;
        document.getElementById("description").innerHTML = resource.description;
    });
}
function refresh_comments(){
    $.ajax({
        type: "GET",
    url: "/album/comments/",
    data: {pic_id: picture_id}
    }).done(function(resource){
        msg = resource;
        document.getElementById("comments_table").innerHTML = "";
        for(i=0;i<resource.length;i++){
            arow = "<tr id='comment'"+i+"><td>"+resource[i].author+"</td><td>"+resource[i].description+"</td><td>"+resource[i].pub_date+"</td>";
            if(ifadmin){
                arow += "<td><button onclick='onDelete("+resource[i].id+")'>Delete</button></td>"
            }
            arow += "</tr>";
            document.getElementById("comments_table").innerHTML += arow;
        }
    });
}

refresh_picture();
refresh_comments();
function onSubmit(){
    var comment = {
        picture: picture_id,
        author: document.getElementById("author_input").value,
        description: document.getElementById("description_input").value};
    if(comment.author == ""){
        document.getElementById("author_err").innerHTML = "Your name should not be empty!!";
        return;
    }
    json = JSON.stringify(comment);
    $.ajax({
        type: "POST",
        url: "/album/comments/",
        data: json,
        contentType: "application/json"
    }).done(refresh_comments);
}

function onDelete(pk){
    $.ajax({
        type: "DELETE",
        url: "/album/comments/"+pk,
    }).done(refresh_comments);
}
