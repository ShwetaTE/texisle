function err_pop(){
    version_modal = 
        '<div class="modal-pos modal-content">'+
            '<div>'+
                '<h2 style="font-weight: bold; color: white; text-align: center; padding: 3%; margin-top: 4px;">Error</h2>'+
            '</div>'+
            '<p style="color: white; text-align: center; font-size: 15px; margin-bottom: 3px;">There seems to be an issue.</p>'+
            '<p style="color: white; text-align: center; font-size: 15px; margin-bottom: 18px;">Kindly reload the app.</p>'+
            '<div>'+
                '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">'+
                '<a href="#" type="button" class="up-btn" onclick ="location.reload()">Reload</a>'+
            '</div>'+
        '</div>'
    
    
    $('#err-modal').append(version_modal);
    var modal = document.getElementById("err-modal");
    modal.style.display = "block";
}

function err_pop_1(err){
    version_modal = 
        '<div class="modal-pos modal-content">'+
            '<div>'+
                '<h2 style="font-weight: bold; color: white; text-align: center; padding: 3%; margin-top: 4px;">Error</h2>'+
            '</div>'+
            '<p style="color: white; text-align: center; font-size: 15px; margin-bottom: 3px;">There seems to be an issue.</p>'+
            '<p style="color: white; text-align: center; font-size: 15px; margin-bottom: 3px;">'+ err +'</p>'+
            '<p style="color: white; text-align: center; font-size: 15px; margin-bottom: 18px;">Kindly reload the app.</p>'+
            '<div>'+
                '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">'+
                '<a href="#" type="button" class="up-btn" onclick ="location.reload()">Reload</a>'+
            '</div>'+
        '</div>'
    
    
    $('#err-modal').append(version_modal);
    var modal = document.getElementById("err-modal");
    modal.style.display = "block";
}