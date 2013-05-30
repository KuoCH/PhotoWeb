$.ajax({
    type: "GET",
    url: "/album/pictures/"+picture_id
}).done(function(resource){
    document.getElementById("title").innerHTML = resource.title;
    document.getElementById("img").src = '/media/'+resource.image;
    document.getElementById("description").innerHTML = resource.description;
});

$.ajax({
    type: "GET",
    url: "/album/comments/",
    data: {pic_id: picture_id}
}).done(function(resource){
    msg = resource;
    for(i=0;i<resource.length;i++){
        document.getElementById("comments_table").innerHTML += "<tr id='comment'"+i+"><td>"+resource[i].author+"</td><td>"+resource[i].description+"</td><td>"+resource[i].pub_date+"</td></tr>";
    }
});


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
    console.log(json);
    $.ajax({
        type: "POST",
        url: "/album/comments/",
        data: json,
        contentType: "application/json"
    })
}
