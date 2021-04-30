document.addEventListener('DOMContentLoaded', function(){
  document.querySelector('#currency').onchange = function(){
  if (document.querySelector('#currency').value == "AED"){
    document.querySelector('#rcurrency').value = "USD"
  }else{
    document.querySelector('#rcurrency').value = "AED"
   }
  }
   document.querySelector('#amount').onchange = function(){
    if (document.querySelector('#currency').value == "AED"){
      document.querySelector('#ramount').value = document.querySelector('#amount').value / 3.66
    }else{
      document.querySelector('#ramount').value = document.querySelector('#amount').value * 3.66
      }
}
window.onload = function() {
  //Check File API support
  let counter = 0;
  if (window.File && window.FileList && window.FileReader) {
    var filesInput = document.getElementById("files");
    filesInput.addEventListener("change", function(event) {
      var files = event.target.files; //FileList object
      var output = document.getElementById("result");
      for (var i = 0; i < 5; i++) {
        var file = files[i];
        if (file.type.match('image'))
        {
        var picReader = new FileReader();
        picReader.addEventListener("load", function(event) {
          var picFile = event.target;
          output.innerHTML += "<img class='contentone' src='" + picFile.result + "'" +
            "title='" + picFile.name + "'/>";
          output.insertBefore(div, null);
        });
      } else
      {
        var picReader = new FileReader();
        picReader.addEventListener("load", function(event) {
          var picFile = event.target;
          var div = document.createElement("span");
          div.innerHTML = "<i class='fas fa-file-pdf'></i>Document"
          output.insertBefore(div, null);
        });
      }
        picReader.readAsDataURL(file);
      }
    });
  } else {
    console.log("Your browser does not support File API");
  }
}
document.addEventListener('DOMContentLoaded', function(){
  let counter = 0;
  document.querySelector('.addimage').onclick = function(){
       if (counter < 5){
          document.getElementById('files').id ="files";
          document.getElementById('formset').innerHTML= "Add Another Image";
        }else{
           document.getElementById('files').id = "none";
           document.getElementById('formset').innerHTML= "Maximum 5 Images";
        }
      counter++;
  } 
});
});