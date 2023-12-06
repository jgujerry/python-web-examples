% rebase("base.tpl", title="Home")

<h1>Bottle MySQL Starter Template</h1>

<p>
    Hello there, welcome! This is a starter template from
    <a href="https://github.com/jgujerry/PythonWebStarters" target="_blank">https://github.com/jgujerry/PythonWebStarters</a>.
    Happy coding!
</p>

<b>MySQL databases available here:</b>
<ul>
% for db in databases:
  <li>{{db}}</li>
% end
</ul>
