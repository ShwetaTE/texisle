$(document).ready(function(){
    let MU_check = getCookie("MU_check");
    if (MU_check!=1){
        mu_modal()
    }

    function mu_modal() {
        var expiryDate = new Date();
        expiryDate.setMonth(expiryDate.getMonth() + 1);
        var block_ch = "document.getElementById('marketUpdate-modal').style.display='none'; document.cookie = 'MU_check=1; expires="+expiryDate+"';"
        marketUpdate_modal = 
            '<div class="modal-pos-MU modal-content">'+
                '<div>'+
                    '<h2 style="font-weight: bold; color: white; text-align: center; padding: 3%; margin-top: 4px;">Weekly Market Update</h2>'+
                '</div>'+
                '<div class="contaier" style="text-align: center;">'+
                    '<iframe width="90%" height="200" src="https://www.youtube.com/embed/VvhsC8L5t6M?controls=0&showinfo=0"></iframe>'+
                '</div>'+
                '<br>'+
                '<div class="container text-white bold"><p>This is how weekly updates can be pushed to the end-users.</p></div>'+
                '<div class="container text-white"><p lang="en" dir="ltr">The third and the last day of the SteelOrbis Fall 2022 Conference &amp; 87th IREPAS Meeting started with the IREPAS committees panel.<br><br>Jens Björkman, Stena Metal International<br>F.D. Baysal, Seba International<br>Murat Cebecioglu, ICDAS<a class="text-white" href="https://twitter.com/hashtag/87irepas?src=hash&amp;ref_src=twsrc%5Etfw">#87irepas</a> <a class="text-white" href="https://t.co/GFB6JsCaWX">pic.twitter.com/GFB6JsCaWX</a></p>&mdash; SteelOrbis (@SteelOrbis) <a class="text-white" href="https://twitter.com/SteelOrbis/status/1579750267771584517?ref_src=twsrc%5Etfw">October 11, 2022</a></div>'+
                // '<ul style="color: white; font-size: 15px;margin-left: 16%;margin-right: 7%">'+changelog+'</ul>'+
                '<br>'+
                '<div>'+
                    '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">'+
                    // '<button href="#" type="button" class="up-btn" onclick ="open_update_link(\''+ red_url +'\')">Update Now</button>'+
                    '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">'+
                    '<button type="button" class="up-btn" onclick="'+block_ch+'">Dismiss</button>'+
                '</div>'+
            '</div>'
        $('#marketUpdate-modal').append(marketUpdate_modal);
        var modal = document.getElementById("marketUpdate-modal");
        modal.style.display = "block";
    }

    function getCookie(cname) {
        let name = cname + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
    
});