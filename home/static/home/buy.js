document.addEventListener('DOMContentLoaded', function(){
  toclick();
})

function toclick(){
  document.querySelectorAll('.toclick').forEach(function(button){
    button.onclick = function(){
     var imagesrc = button.firstElementChild;
     oldnode = document.getElementById('mainimage').firstElementChild
     var newnode = document.createElement("img");
     newnode.setAttribute("src", imagesrc.src);
     newnode.setAttribute('class', 'img_toggler')
     newnode.setAttribute('id', imagesrc.id )
     var space = document.getElementById('mainimage');
     space.replaceChild(newnode, oldnode);
    }
   })
}