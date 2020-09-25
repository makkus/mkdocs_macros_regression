# Test repo for mkdocs macros plugin regression

Issue link: https://github.com/fralau/mkdocs_macros_plugin/issues/43

Steps to reproduce:

- clone this repo
- change into newly checked out repo
- create & activate virtualenv
- run: ``pip install -e '.[docs]'``
- run: ``mkdocs build``

Results in:

```
 mkdocs build
[macros] Macros arguments: {'module_name': 'ci.docs', 'include_dir': '', 'include_yaml': [], 'j2_block_start_string': '', 'j2_block_end_string': '', 'j2_variable_start_string': '', 'j2_variable_end_string': ''}
Traceback (most recent call last):
  File "/tmp/tingex/.direnv/python-3.8.5/bin/mkdocs", line 8, in <module>
    sys.exit(cli())
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/click/core.py", line 829, in __call__
    return self.main(*args, **kwargs)
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/click/core.py", line 1259, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/click/core.py", line 1066, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/mkdocs/__main__.py", line 152, in build_command
    build.build(config.load_config(**kwargs), dirty=not clean)
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/mkdocs/commands/build.py", line 236, in build
    config = config['plugins'].run_event('config', config)
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/mkdocs/plugins.py", line 94, in run_event
    result = method(item, **kwargs)
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/macros/plugin.py", line 314, in on_config
    self._load_module()
  File "/tmp/tingex/.direnv/python-3.8.5/lib/python3.8/site-packages/macros/plugin.py", line 242, in _load_module
    raise ImportError("Macro plugin could not find custom '%s' "
ImportError: Macro plugin could not find custom 'ci.docs' module in '/tmp/tingex'.
```


