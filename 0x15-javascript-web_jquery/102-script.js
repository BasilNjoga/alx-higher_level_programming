#!/usr/bin/node

$(document).ready(function(){
    $("INPUT#btn_translate").click(function(){
        $.get("https://www.fourtonfish.com/hellosalut/hello/", function(data, status){
            $.("DIV#hello").text("Hello" + data);
        });
    });
});