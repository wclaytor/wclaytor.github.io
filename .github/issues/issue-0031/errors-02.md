bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io
> $ cd tests/playwright
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ uv sync
Resolved 32 packages in 147ms
      Built wclaytor-playwright-tests @ file:///home/bpc/Pro
Prepared 2 packages in 15.14s
Installed 26 packages in 65ms
 + axe-playwright-python==0.1.7
 + certifi==2025.11.12
 + charset-normalizer==3.4.4
 + execnet==2.1.2
 + greenlet==3.3.0
 + idna==3.11
 + iniconfig==2.3.0
 + jinja2==3.1.6
 + markupsafe==3.0.3
 + packaging==25.0
 + playwright==1.57.0
 + pluggy==1.6.0
 + pyee==13.0.0
 + pygments==2.19.2
 + pytest==9.0.2
 + pytest-base-url==2.1.0
 + pytest-html==4.1.1
 + pytest-metadata==3.1.1
 + pytest-playwright==0.7.2
 + pytest-xdist==3.8.0
 + python-slugify==8.0.4
 + requests==2.32.5
 + text-unidecode==1.3
 + typing-extensions==4.15.0
 + urllib3==2.6.2
 + wclaytor-playwright-tests==1.0.0 (from file:///home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright)
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ uv run playwright install
BEWARE: your OS is not officially supported by Playwright; downloading fallback build for ubuntu24.04-x64.
Downloading Chromium 143.0.7499.4 (playwright build v1200) from https://cdn.playwright.dev/dbazure/download/playwright/builds/chromium/1200/chromium-linux.zip
(node:214868) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
164.7 MiB [====================] 100% 0.0s
Chromium 143.0.7499.4 (playwright build v1200) downloaded to /home/bpc/.cache/ms-playwright/chromium-1200
BEWARE: your OS is not officially supported by Playwright; downloading fallback build for ubuntu24.04-x64.
Downloading Chromium Headless Shell 143.0.7499.4 (playwright build v1200) from https://cdn.playwright.dev/dbazure/download/playwright/builds/chromium/1200/chromium-headless-shell-linux.zip
(node:214985) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
109.7 MiB [====================] 100% 0.0s
Chromium Headless Shell 143.0.7499.4 (playwright build v1200) downloaded to /home/bpc/.cache/ms-playwright/chromium_headless_shell-1200
BEWARE: your OS is not officially supported by Playwright; downloading fallback build for ubuntu24.04-x64.
Downloading Firefox 144.0.2 (playwright build v1497) from https://cdn.playwright.dev/dbazure/download/playwright/builds/firefox/1497/firefox-ubuntu-24.04.zip
(node:215186) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
98.4 MiB [====================] 100% 0.0s
Firefox 144.0.2 (playwright build v1497) downloaded to /home/bpc/.cache/ms-playwright/firefox-1497
BEWARE: your OS is not officially supported by Playwright; downloading fallback build for ubuntu24.04-x64.
Downloading Webkit 26.0 (playwright build v2227) from https://cdn.playwright.dev/dbazure/download/playwright/builds/webkit/2227/webkit-ubuntu-24.04.zip
(node:215323) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
95.9 MiB [====================] 100% 0.0s
Webkit 26.0 (playwright build v2227) downloaded to /home/bpc/.cache/ms-playwright/webkit-2227
BEWARE: your OS is not officially supported by Playwright; downloading fallback build for ubuntu24.04-x64.
Downloading FFMPEG playwright build v1011 from https://cdn.playwright.dev/dbazure/download/playwright/builds/ffmpeg/1011/ffmpeg-linux.zip
(node:215874) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
2.3 MiB [====================] 100% 0.0s
FFMPEG playwright build v1011 downloaded to /home/bpc/.cache/ms-playwright/ffmpeg-1011
Playwright Host validation warning: 
╔══════════════════════════════════════════════════════╗
║ Host system is missing dependencies to run browsers. ║
║ Please install them with the following command:      ║
║                                                      ║
║     sudo playwright install-deps                     ║
║                                                      ║
║ Alternatively, use apt:                              ║
║     sudo apt-get install libicu74\                   ║
║         libevent-2.1-7t64\                           ║
║         libavif16                                    ║
║                                                      ║
║ <3 Playwright Team                                   ║
╚══════════════════════════════════════════════════════╝
    at validateDependenciesLinux (/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/playwright/driver/package/lib/server/registry/dependencies.js:269:9)
    at async Registry._validateHostRequirements (/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/playwright/driver/package/lib/server/registry/index.js:990:14)
    at async Registry._validateHostRequirementsForExecutableIfNeeded (/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/playwright/driver/package/lib/server/registry/index.js:1112:7)
    at async Registry.validateHostRequirementsForExecutablesIfNeeded (/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/playwright/driver/package/lib/server/registry/index.js:1101:7)
    at async r.<anonymous> (/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/playwright/driver/package/lib/cli/program.js:176:7)
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ uv run pytest
Traceback (most recent call last):
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/bin/pytest", line 10, in <module>
    sys.exit(console_main())
             ~~~~~~~~~~~~^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 223, in console_main
    code = main()
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 193, in main
    config = _prepareconfig(new_args, plugins)
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 361, in _prepareconfig
    config: Config = pluginmanager.hook.pytest_cmdline_parse(
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        pluginmanager=pluginmanager, args=args
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
    ~~~~~~~~~~~~~~^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/helpconfig.py", line 124, in pytest_cmdline_parse
    config = yield
             ^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 1186, in pytest_cmdline_parse
    self.parse(args)
    ~~~~~~~~~~^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 1556, in parse
    self.hook.pytest_load_initial_conftests(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        early_config=self, args=args, parser=self._parser
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
    ~~~~~~~~~~~~~~^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/warnings.py", line 128, in pytest_load_initial_conftests
    return (yield)
            ^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
    ~~~~~~~~~~~~~~^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/capture.py", line 173, in pytest_load_initial_conftests
    yield
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 1270, in pytest_load_initial_conftests
    self.pluginmanager._set_initial_conftests(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        args=args,
        ^^^^^^^^^^
    ...<8 lines>...
        ),
        ^^
    )
    ^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 602, in _set_initial_conftests
    self._try_load_conftest(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        anchor,
        ^^^^^^^
    ...<2 lines>...
        consider_namespace_packages=consider_namespace_packages,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 640, in _try_load_conftest
    self._loadconftestmodules(
    ~~~~~~~~~~~~~~~~~~~~~~~~~^
        anchor,
        ^^^^^^^
    ...<2 lines>...
        consider_namespace_packages=consider_namespace_packages,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 680, in _loadconftestmodules
    mod = self._importconftest(
        conftestpath,
    ...<2 lines>...
        consider_namespace_packages=consider_namespace_packages,
    )
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 756, in _importconftest
    self.consider_conftest(mod, registration_name=conftestpath_plugin_name)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 837, in consider_conftest
    self.register(conftestmodule, name=registration_name)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/__init__.py", line 522, in register
    plugin_name = super().register(plugin, name)
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 169, in register
    hook._maybe_apply_history(hookimpl)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_hooks.py", line 580, in _maybe_apply_history
    res = self._hookexec(self.name, [method], kwargs, False)
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/conftest.py", line 47, in pytest_addoption
    parser.addoption(
    ~~~~~~~~~~~~~~~~^
        "--base-url",
        ^^^^^^^^^^^^^
    ...<2 lines>...
        help=f"Base URL for tests (default: {LOCAL_URL})",
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/argparsing.py", line 123, in addoption
    self._anonymous.addoption(*opts, **attrs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/bpc/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright/.venv/lib/python3.13/site-packages/_pytest/config/argparsing.py", line 429, in addoption
    raise ValueError(f"option names {conflict} already added")
ValueError: option names {'--base-url'} already added
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ ^C
bpc@bpc-ubuntu:
>> ~/Projects/GitHub/Repos/wclaytor.github.io/branches/main/wclaytor.github.io/tests/playwright
> $ 