$("#predict").mousedown(function(){
    $("#predict").css("background-color", "rgb(140, 200, 235)");
})

$("#predict").mouseup(function(){
    $("#predict").css("background-color", "rgb(150, 210, 245");
})



$("#predict").click(function(){
    let gender = $("#gender").val();
    let age = $("#age").val();
    let salary = $("#salary").val();
    

    $("#predict").animate({
        opacity: "0%"
    }, 200, function(){
        $("#predict").remove()
    })
    $("#subtitle").animate({
        opacity: "0%"
    }, 200, function(){
        $("#subtitle").remove()
    })
    $(".inputs").animate({
        opacity: "0%"
    }, 200, function(){
        $(".inputs").remove()
    })


    $("#title").animate({
        top: "-50px",
        fontSize: "50px",
    }, 500, function(){
        $.ajax({
            url:"/call",
            data: {gender:gender, age:age, salary:salary},
            success: function(data){
                console.log(data)

                let htmlstr = "<h1 style='font-family: Raleway; font-weight: 600; font-size:100px; color: rgb(255, 255, 255); margin-top: 100px;'>" + data['msg'] + "</h1>"
                $(".intf").append(htmlstr)



            }
        })

    })



})