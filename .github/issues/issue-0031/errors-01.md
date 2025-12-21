bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io
> $ cd tests/playwright
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ uv sync
Using CPython 3.13.3 interpreter at: /usr/bin/python3
Creating virtual environment at: .venv
Resolved 32 packages in 1.66s
  × Failed to build `wclaytor-playwright-tests @
  │ file:///home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `hatchling.build.build_editable` failed (exit status: 1)

      [stderr]
      Traceback (most recent call last):
        File "<string>", line 11, in <module>
          wheel_filename =
      backend.build_editable("/home/bpc/.cache/uv/builds-v0/.tmpnZDCDC", {}, None)
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/build.py",
      line 83, in build_editable
          return os.path.basename(next(builder.build(directory=wheel_directory,
      versions=["editable"])))
      
      ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/builders/plugin/interface.py",
      line 157, in build
          artifact = version_api[version](directory, **build_data)
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/builders/wheel.py",
      line 522, in build_editable
          return self.build_editable_detection(directory, **build_data)
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/builders/wheel.py",
      line 534, in build_editable_detection
          for included_file in self.recurse_selected_project_files():
                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/builders/plugin/interface.py",
      line 182, in recurse_selected_project_files
          if self.config.only_include:
             ^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.13/functools.py", line 1026, in __get__
          val = self.func(instance)
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/builders/config.py",
      line 715, in only_include
          only_include = only_include_config.get("only-include",
      self.default_only_include()) or self.packages
                                                                 ~~~~~~~~~~~~~~~~~~~~~~~~~^^
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/builders/wheel.py",
      line 268, in default_only_include
          return self.default_file_selection_options.only_include
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.13/functools.py", line 1026, in __get__
          val = self.func(instance)
        File
      "/home/bpc/.cache/uv/builds-v0/.tmpA0mNGz/lib/python3.13/site-packages/hatchling/builders/wheel.py",
      line 256, in default_file_selection_options
          raise ValueError(message)
      ValueError: Unable to determine which files to ship
      inside the wheel using the following heuristics:
      https://hatch.pypa.io/latest/plugins/builder/wheel/#default-file-selection

      The most likely cause of this is that there is no directory that matches the name of
      your project (wclaytor_playwright_tests).

      At least one file selection option must be defined
      in the `tool.hatch.build.targets.wheel` table, see:
      https://hatch.pypa.io/latest/config/build/

      As an example, if you intend to ship a directory named `foo` that resides within a
      `src` directory located at the root of your project, you can define the following:

      [tool.hatch.build.targets.wheel]
      packages = ["src/foo"]

      hint: This usually indicates a problem with the package or the build environment.
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ ^C
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ 