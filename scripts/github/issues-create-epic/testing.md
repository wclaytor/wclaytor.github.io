# testing

scripts/github/create-epic/create-epic.py

```bash
python3 scripts/github/create-epic/create-epic.py test-epic.md --dry-run
```

Please update the create epic script so that the --repo argument is optional and assume if it is not provided we should default to the current repo. The gh command line tool does not require the repo to be specified so we should only specify it in the script when calling gh if the user specifies it when calling this script.

Please provide an example usage of the gh command line tool to create a new issue in the current repo with the minimum arguments

---

python3 scripts/github/create-epic/create-epic.py scripts/github/create-epic/test-epic.md --dry-run

----

We got the following output when we ran the create-epic.py script:

```
@wclaytor ➜ /workspaces/project-template (46-github-issues-automation) $ python3 scripts/github/create-epic/create-epic.py scripts/github/create-epic/test-epic.md
📚 Parsing scripts/github/create-epic/test-epic.md
🎯 Creating Epic: Epic: Test Epic for Script Validation
  ❌ Command failed: gh issue create --title Epic: Test Epic for Script Validation --body This is a test epic created to validate the create-epic.py script functionality.

Success Criteria:
- Script successfully parses the markdown file
- Epic issue is created in GitHub
- Child issues are created and linked to the epic

## Child Issues
*Will be updated with ticket links* --json number --label epic --label test
  Error: unknown flag: --json

Usage:  gh issue create [flags]

Flags:
  -a, --assignee login   Assign people by their login. Use "@me" to self-assign.
  -b, --body string      Supply a body. Will prompt for one otherwise.
  -F, --body-file file   Read body text from file (use "-" to read from standard input)
  -e, --editor           Skip prompts and open the text editor to write the title and body in. The first line is the title and the remaining text is the body.
  -l, --label name       Add labels by name
  -m, --milestone name   Add the issue to a milestone by name
  -p, --project title    Add the issue to projects by title
      --recover string   Recover input from a failed run of create
  -T, --template name    Template name to use as starting body text
  -t, --title string     Supply a title. Will prompt for one otherwise.
  -w, --web              Open the browser to create an issue
  

  ❌ Failed to create epic

```

It feels like the output is giving us too much generic info that we would get by running it with no args, and no details on the actual error. So I think we need to get tactical and add some logging in the right places so we know what is happening when this script is running, and not just a list of all of the calling options.

---

python3 scripts/github/issues-create-epic/create-epic.py scripts/github/issues-create-epic/test-epic.md

---

We made huge progress! I ran the script and it failed because we did not have the 'epic' label in our project. We need to create the label if it does not exist. I went ahead and created it. Then it failed for the 'test' label. I created it. And it actually created the Epic! But then it failed with the error below:

```

@wclaytor ➜ /workspaces/project-template (46-github-issues-automation) $ python3 scripts/github/issues-create-epic/create-epic.py scripts/github/issues-create-epic/test-epic.md
🔍 Verifying GitHub CLI installation and authentication...
✅ GitHub CLI verified and authenticated

============================================================
GitHub Epic & Issues Creator
============================================================

📖 Reading and parsing scripts/github/issues-create-epic/test-epic.md
  ✓ Found epic: Epic: Test Epic for Script Validation
  ✓ Found 2 ticket(s)

🎯 Creating Epic: Epic: Test Epic for Script Validation
  ✅ Created Epic: #47
  🔗 URL: https://github.com/wclaytor/project-template/issues/47

📋 Creating 2 ticket(s)...

Traceback (most recent call last):
  File "/workspaces/project-template/scripts/github/issues-create-epic/create-epic.py", line 467, in <module>
    main()
  File "/workspaces/project-template/scripts/github/issues-create-epic/create-epic.py", line 463, in main
    creator.create_issues_from_file(args.file)
  File "/workspaces/project-template/scripts/github/issues-create-epic/create-epic.py", line 412, in create_issues_from_file
    logger.info(f"[{i}/{len(data['tickets'])}] ", end='')
  File "/home/codespace/.python/current/lib/python3.12/logging/__init__.py", line 1539, in info
    self._log(INFO, msg, args, **kwargs)
TypeError: Logger._log() got an unexpected keyword argument 'end'

```