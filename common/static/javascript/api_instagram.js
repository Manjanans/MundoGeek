const url = 'https://graph.instagram.com/me/media?fields=id,username,media_url,caption&access_token=IGQVJYbnR0czJaV3k3ZAURxRjl3WENDWm5sZA2NhUDVhTTJPVnNlbFFzcG8yVlVFTWVPZAGhseHA3c1Fpend4YlBpNktJN1RITjduSmZAXcU1qWEJZAVnpWbEdXMGhVdHFOMDdnb2hLZAW5mQmd4LW9kd1g1TQZDZD';
const par = document.querySelector('.card-group');
fetch(url).then(res=>res.json()).then(data=>mostrarConsola(data.data,3));
const perfil = 'https://www.instagram.com/mundogeek_pmontt/';


function mostrarConsola(data,num){
    var i=0;
    for (elm of data){
        i+=1;
        var texto = elm.caption;
        if(texto == undefined){
            texto = "Disfruta esta foto con nosotros!"
        }
        par.innerHTML+=`
        <div class="card" id="post_${i}">
            <a href="${perfil}">
                <img src="${elm.media_url}" alt="img-insta" class="img-fluid">
            </a>
            <div class="card-body" id="texto_${i}" style="display: none;">
                <p class="card-text">
                    ${texto}
                </p>
            </div>
        </div>`;
        if (i==num){
            break;
        }
    }
}

$(document).ready(function() {
    $(".card-group").hover(function(){
        $("#texto_1").show();
        $("#texto_2").show();
        $("#texto_3").show();
    }, function(){
        $("#texto_1").hide();
        $("#texto_2").hide();
        $("#texto_3").hide();
    });
});