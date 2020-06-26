
function openCity(evt, subcat,cat) {
  var i, tabcontent, tablinks, defaultopen;
  tabcontent = document.getElementsByClassName(cat+"-tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].setAttribute("style", "display: none;padding: 6px 12px;border:1px solid #ccc; border-top: none;");
  }
  tablinks = document.getElementsByClassName(cat+"-tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cat+"-"+subcat).setAttribute("style", "display: block;");
  evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
defaultopen = document.getElementsByClassName("defaultOpen");
for (i=0; i<defaultopen.length; i++) {
  defaultopen[i].click()
}
