% rebase("base.tpl", title="Home")

<h1>Bottle MySQL Starter Example</h1>

<p>
    Hello there, welcome! This is a starter example from
    <a href="https://github.com/jgujerry/python-web-examples" target="_blank">https://github.com/jgujerry/python-web-examples</a>.
    Happy coding!
</p>

<b>MySQL databases available here:</b>
<ul>
% for db in databases:
  <li>{{db}}</li>
% end
</ul>
