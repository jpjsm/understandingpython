# Sample Data Generation


## Setup your python development environment

Once you have clonned the repo and chaged your working directory to the root of the repo, activate your virtual environment.

### Virtual environment

**Always** activate your virtual environment before starting to work

#### Create your virtual environment

If you have not created your virtual environment...  
Do it now, with the following command at the root folder of the repo:  
&nbsp;&nbsp;&nbsp;&nbsp;`python -m venv .`

> **Note**:  
You only need to create your virtual environment once.

#### Activate your virtual environment

- \[Windows]: `scripts\activate`
- \[Linux, MacOS]: `bin/activate`

    > The prompt should change to `(kulshan) path/to/root/folder ...`

#### Install all ***build*** dependencies

From your virtual environment shell prompt:

- Check the version of *pip*: `pip --version`
- List the contents of `[build-system].requires` in `pyproject.toml` file  

    ```
    "pip>=22.1",
    "setuptools>=60.0.0",
    "setuptools_scm[toml]>=6.4.2",
    "wheel>=0.37",
    "pip-tools>=6.6.2",
    "build>=0.8.0"
    ```

- If your version of *pip* is lesser than the minimum required for the build system, run:  
`python -m pip install --upgrade pip`
- For all other requirements execute:  
`pip install "{tool}>={version-id}"`
    > **Note**  
    The ***greater-equal*** symbol between *tool* and *version*  
    It is **mandatory**, no modifications.

    > **Note**  
    The double-quotes are required, the `>` is the redirection character,  
    both in Windows and *ux*-like operating systems.
- Run `pip list` to verify the minimum requirements for the build system are met.  
The outpul list might contain other tools, outside the ones mentioned in the `[build-system].requires` section of the file; those are the dependencies for the build system tools.

#### Install project dependencies

From your virtual environment shell prompt:

```
pip-compile --output-file=requirements-dev.txt requirements-dev.in requirements.in
pip install -r requirements-dev.txt 
```

Compare the output of `pip list` with the contents of *requirements.in* **+** *requirements-dev.in*.  
Everything in *requirements.in" must be in the output of `pip list`; be aware the output of `pip list` includes all dependencies of*requirements.in*, so it will probably be longer.

## Build

> Delivering the package for your users !  
Make sure no developer dependecies are included in the final product.

From your virtual environment shell prompt, at the root folder:

```
python -m build
```

### Check your build

From your virtual environment shell prompt, at the root folder:

```
pypi-server -p 18080 ./dist
```

Leave the `pypi` server running and open a new virtual environment shell prompt, at the root folder, and run the following command:

```
pip search --index http://localhost:18080 kulshan
```

The output should be similar to the following:

```
kulshan (0.1.dev2+gcd1df0f.d20220626)  - 0.1.dev2+gcd1df0f.d20220626
```

### Test your build is installable and usable

If you don't have you local `pypi` server running, see above *Check your build* to start it.

open a new virtual environment shell prompt, at the root folder, and run the following commands:

```sh
pip install --index-url http://localhost:18080/simple/ kulshan
python -c "import kulshan; print(kulshan.__doc__)"
pip uninstall kulshan
```

Output looks similar to:

```txt
{shell-prompt-here}pip install --index-url http://localhost:18080/simple/ kulshan
Looking in indexes: http://localhost:18080/simple/
Collecting kulshan
  Downloading http://localhost:18080/packages/kulshan-0.1.dev2%2Bgcd1df0f.d20220626-py3-none-any.whl (3.2 kB)
Requirement already satisfied: flake8-executable==2.1.1 in c:\repos\dell\kulshan\lib\site-packages (from kulshan) (2.1.1)
Requirement already satisfied: pipdeptree==2.2.1 in c:\repos\dell\kulshan\lib\site-packages (from kulshan) (2.2.1)
Requirement already satisfied: pep8-naming==0.13.0 in c:\repos\dell\kulshan\lib\site-packages (from kulshan) (0.13.0)

... listing trimmed here ...

Requirement already satisfied: distlib<1,>=0.3.1 in c:\repos\dell\kulshan\lib\site-packages (from virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0->tox==3.25.0->kulshan) (0.3.4)
Requirement already satisfied: sniffio>=1.1 in c:\repos\dell\kulshan\lib\site-packages (from anyio<5,>=3.4.0->starlette==0.19.1->fastapi==0.78.0->kulshan) (1.2.0)
Requirement already satisfied: webencodings in c:\repos\dell\kulshan\lib\site-packages (from bleach>=2.1.0->readme-renderer>=35.0->twine==4.0.1->kulshan) (0.5.1)
Installing collected packages: kulshan
Successfully installed kulshan-0.1.dev2+gcd1df0f.d20220626

{shell-prompt-here}python -c "from kulshan import kulshan; print(kulshan.__doc__)"

APEX Integrated Instrumentation:
Seamlessly add metrics, logging, and tracing to a project without much effort.

{shell-prompt-here}pip uninstall kulshan
Found existing installation: kulshan 0.1.dev2+gcd1df0f.d20220626
Uninstalling kulshan-0.1.dev2+gcd1df0f.d20220626:
  Would remove:
    c:\repos\dell\kulshan\lib\site-packages\kulshan-0.1.dev2+gcd1df0f.d20220626.dist-info\*
    c:\repos\dell\kulshan\lib\site-packages\kulshan\*
Proceed (Y/n)? Y
  Successfully uninstalled kulshan-0.1.dev2+gcd1df0f.d20220626
```

## Code Validation

### Formatting

If you don't have `black` formatter enabled in your preferred IDE,
you need to run the `black` formatting tool before you run the
linter and the code analysis tool. The formatting tool guarantees
check-ins from different developers will not have merge conflicts
due to differences in coding styles.

From your virtual environment shell prompt, at the root folder:

```sh
black src/kulshan
black tests
black debug
```

Should generate an output similar to:

```txt
(kulshan) {shell-prompt-here}>black src/kulshan
reformatted src\kulshan\kmetrics\kotel.py
reformatted src\kulshan\kmetrics\middleware.v2_wip.py

All done! ✨ 🍰 ✨
2 files reformatted, 14 files left unchanged.

(kulshan) {shell-prompt-here}>
```

### Linting and code analysis

From your virtual environment shell prompt, at the root folder:

```sh
black src/sample
black tests
black debug
```

### Unit Tests

From your virtual environment shell prompt, at the root folder:

```sh
.\Scripts\python.exe -m pytest --rootdir . --override-ini junit_family=xunit1 ./tests/
```

### Debugging

When debugging code, setting the environment variable `PYTHON_DEBUG` to anything different than **NO** enables additional console logging. That is very useful before `logging` gets enabled.
