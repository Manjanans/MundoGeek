const url = 'https://graph.instagram.com/me/media?fields=id,username,media_url,caption&access_token=IGQVJYbnR0czJaV3k3ZAURxRjl3WENDWm5sZA2NhUDVhTTJPVnNlbFFzcG8yVlVFTWVPZAGhseHA3c1Fpend4YlBpNktJN1RITjduSmZAXcU1qWEJZAVnpWbEdXMGhVdHFOMDdnb2hLZAW5mQmd4LW9kd1g1TQZDZD';
const par = document.getElementById('insta');
fetch(url).then(res=>res.json()).then(data=>mostrarConsola(data.data,2));
const perfil = 'https://www.instagram.com/mundogeek_pmontt/';


function mostrarConsola(data,num){
    var i = 0;
    for (elm of data){
        par.innerHTML+='<div class="card"><a href="'+perfil+'"><img src="'+elm.media_url+'" alt="img-insta" class="img-fluid"></a></div>';
        i+=1;
        if (num==i){
            break;
        }
    }
}