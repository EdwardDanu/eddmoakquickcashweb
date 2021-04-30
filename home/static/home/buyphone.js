document.addEventListener('DOMContentLoaded', function(){
  if (document.querySelector('#phone').innerHTML == "buyiphone") {
      document.querySelector('#buyiphone').style.display = "block";
      document.querySelector('#buysamsung').style.display = "none";
      document.querySelector('#buyhuawei').style.display = "none";
      load_index('iphone/')
    }
    else if (document.querySelector('#phone').innerHTML == "buysamsung") {
    document.querySelector('#buysamsung').style.display = "block";
    document.querySelector('#buyiphone').style.display = "none";
    document.querySelector('#buyhuawei').style.display = "none";
    load_index('samsung/')
    }
    else {
    document.querySelector('#buyhuawei').style.display = "block";
    document.querySelector('#buyiphone').style.display = "none";
    document.querySelector('#buysamsung').style.display = "none";
    load_index('huawei/')
    }
  });
  function load_index(postlink){
    fetch(postlink)
    .then(response => response.json())
    .then(results => {
      if (postlink ==  'iphone/'){
        var sidebarid = "buyiphonesidebar";
        var contentid = 'buyiphonecontent';

      }
      else if (postlink  == 'samsung/'){
        var sidebarid = "buysamsungsidebar";
        var contentid = 'buysamsungcontent';
      }
      else{
        var sidebarid = "buyhuaweisidebar";
        var contentid = 'buyhuaweicontent';
      }
        for (var brand = 0; brand < results[1].length; brand++){
            var brandlists = document.createElement("center");
            brandlists.className = "brand-item";
            brandlists.innerHTML = results[1][brand].brand;
            document.querySelector(`#${sidebarid}`).appendChild(brandlists);
            
        }
        for (var color = 0; color < results[2].length; color++){
            var colorlists = document.createElement("center");
            colorlists.className = "color-item";
            colorlists.innerHTML = results[2][color].color;
            document.querySelector(`#${sidebarid}`).appendChild(colorlists);

        }
        for (var image = 0; image < results[0].length; image++){
            var animage = document.createElement("a");
            animage.id = `single-image${results[0][image].id}`;
            animage.className = "imagelinks";
            animage.href = `${contentid}/${results[0][image].entry.entryid}`;
            animage.innerHTML = `<h6 class="hiddenbrand">${results[0][image].entry.brand}</h6>
            <img src ="${results[0][image].images}" class="listingimages" id="${results[0][image].id}">
            <span class="infomation"><hr class="hrclass"><h6>${results[0][image].entry.brand}</h6>
            <h6>${results[0][image].entry.memory}, ${results[0][image].entry.network},</h6><h6>${results[0][image].entry.color}</h6>
            <h6>International Version</h6></span>`
            document.querySelector(`#${contentid}`).appendChild(animage)
        }
        
          document.querySelectorAll('.brand-item').forEach(function(button){
            button.onclick = function(){
              var brand = this.innerHTML;
              for (var image = 0; image < results[3].length; image++){
                console.log(results[3][0][0].length)
                console.log(results[3][image][0].entry.brand)
              }
               }
          })
        
    })
    }

    function to(){
      document.querySelectorAll('.brand-item').forEach(function(button){
        button.onclick = function(){
          document.querySelector(`#${contentid}`).innerHTML ='';
          var brand = this.innerHTML;
          document.querySelectorAll(".imagelinks").forEach( function(link){
            if(link.firstElementChild.innerHTML == brand){
              document.querySelector(`#${contentid}`).innerHTML += this.innerHTML;
            }
          })
         
        }
       })
    }