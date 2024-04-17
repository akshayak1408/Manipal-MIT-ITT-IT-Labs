var str= document.getElementById("tno").value;

function submit(){
  var a=str.split(" ");
  var ac=a[0].substring(1,a[0].length-1);
  var p1=a[1];
  var p2=a[3];
  var p=p1.concat(p2);
  document.getElementById("areacode").value = ac;
  document.getElementById("phoneno").value = p;

}