$(document).ready(function(){
var tex_link = "https://texisle.com/"
var red = '+system'
var header = 
'<div id="kt_header">'+
    '<div>'+
       '<div class="row" style="width: 100%;">'+
            '<div class="float-left" style="width: 50%; padding-left: 3%;">'+
                '<a onclick="app_end(window.location.pathname)" class="text-light mt-2 mb-1 mr-5 ml-4" style="color: white; font-weight: bold; font-size: 25px;">Pipe Intel</a>'+
            '</div>'+
            '<div class="float-left" style="width: 50%; padding-right: 0%;">'+
                // '<p onclick="window.open(\''+ tex_link +'\',\''+ red +'\')" class="font-weight-bold power" style="text-align: right; color: #9bb556;">Powered by Tex-Isle Inc.</p>'+
            '</div>'+
        '</div>'+
    '</div>'+
    '<hr style="border-top: 2px solid #7a7772; margin-top: 0px; margin-bottom: 0rem;">'+
'</div>'

$('#header-id').append(header);
});