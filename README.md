## Developer Note

While developing CodeGuardian itself, the pre-commit hook may block commits because the repository contains sample files with intentional architecture violations and circular dependencies.

To temporarily disable the hook:

### Windows (PowerShell)

```powershell
Rename-Item .git\hooks\pre-commit pre-commit.bak
```

### Linux/macOS

```bash
mv .git/hooks/pre-commit .git/hooks/pre-commit.bak
```

After committing, restore the hook:

### Windows (PowerShell)

```powershell
Rename-Item .git\hooks\pre-commit.bak pre-commit
```

or reinstall it:

```bash
python install_hook.py
```

