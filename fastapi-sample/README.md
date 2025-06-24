# Fastapi silly numbers sample

Fastapi easy to test example code

# Setup your python development environment

Once you have clonned the repo and chaged your working directory to the root of the repo, activate your virtual environment.

## Virtual environment

**Always** activate your virtual environment before starting to work

### Create your virtual environment

If you have not created your virtual environment...  
Do it now, with the following command at the root folder of the repo:  
&nbsp;&nbsp;&nbsp;&nbsp;`python -m venv .`

> **Note**:  
You only need to create your virtual environment once.

### Activate your virtual environment
-  \[Windows]: `scripts\activate`
-  \[Linux, MacOS]: `bin/activate`

    > The prompt should change to `(icecream) path/to/root/folder ...`

### Install all ***build*** dependencies

From your virtual environment shell prompt:
-  Check the version of *pip*: `pip --version`
-  List the contents of `[build-system].requires` in `pyproject.toml` file  
    ```
    "pip>=22.1",
    "setuptools>=60.0.0",
    "setuptools_scm[toml]>=6.4.2",
    "wheel>=0.37",
    "pip-tools>=6.6.2"
    "build>=0.8.0"
    ```
- If your version of *pip* is lesser than the minimum required for the build system, run:  
`python -m pip install --upgrade pip`
-  For all other requirements execute:  
`pip install "{tool}>={version-id}"`
    > **Note** the ***greater-equal*** symbol between *tool* and *version*  
    It is **mandatory**, no modifications.
- Run `pip list` to verify the minimum requirements for the build system are met.  
The outpul list might contain other tools, outside the ones mentioned in the `[build-system].requires` section of the file; those are the dependencies for the build system tools.

### Install project dependencies

From your virtual environment shell prompt:

```
pip-compile
pip install -r requirements.txt 
```
Compare the output of `pip list` with the contents of *requirements.in*.  
Everything in *requirements.in" must be in the output of `pip list`; be aware the output of `pip list` includes all dependencies of *requirements.in*, so it will probably be longer.

# build

From your virtual environment shell prompt, at the root folder:

```
python -m build -s -w 
```

## Check your build

From your virtual environment shell prompt, at the root folder:

```
pypi-server -p 18080 ./dist
```

Leave the `pypi` server running and open a new virtual environment shell prompt, at the root folder, and run the following command:

```
pip search --index http://localhost:18080 icecream
```

The output should be similar to the following:

```
icecream (0.1.dev2+gcd1df0f.d20220626)  - 0.1.dev2+gcd1df0f.d20220626
  INSTALLED: 0.1.dev2+gcd1df0f.d20220626
  LATEST:    0.1.dev11+gf9c6978
```

## Test your build is installable and usable

If you don't have you local `pypi` server running, see above *Check your build* to start it.

open a new virtual environment shell prompt, at the root folder, and run the following commands:

```
pip install --index-url http://localhost:18080/simple/ icecream==<latest-or-required-version-here>
python -c "from icecream import icecream; print(icecream.__doc__)"
pip uninstall icecream
```

> Where `<latest-or-required-version-here>` should be replaced with a value similar to `0.1.dev11`, from the *search* output.

Output looks similar to:

```
{shell-prompt-here}pip install --index-url http://localhost:18080/simple/ icecream==0.1.dev11
Looking in indexes: http://localhost:18080/simple/
Collecting icecream
  Downloading http://localhost:18080/packages/icecream-0.1.dev2%2Bgcd1df0f.d20220626-py3-none-any.whl (3.2 kB)
Requirement already satisfied: flake8-executable==2.1.1 in c:\repos\dell\icecream\lib\site-packages (from icecream) (2.1.1)
Requirement already satisfied: pipdeptree==2.2.1 in c:\repos\dell\icecream\lib\site-packages (from icecream) (2.2.1)
Requirement already satisfied: pep8-naming==0.13.0 in c:\repos\dell\icecream\lib\site-packages (from icecream) (0.13.0)

... listing trimmed here ...

Requirement already satisfied: distlib<1,>=0.3.1 in c:\repos\dell\icecream\lib\site-packages (from virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0->tox==3.25.0->icecream) (0.3.4)
Requirement already satisfied: sniffio>=1.1 in c:\repos\dell\icecream\lib\site-packages (from anyio<5,>=3.4.0->starlette==0.19.1->fastapi==0.78.0->icecream) (1.2.0)
Requirement already satisfied: webencodings in c:\repos\dell\icecream\lib\site-packages (from bleach>=2.1.0->readme-renderer>=35.0->twine==4.0.1->icecream) (0.5.1)
Installing collected packages: icecream
Successfully installed icecream-0.1.dev2+gcd1df0f.d20220626

{shell-prompt-here}python -c "from icecream import icecream; print(icecream.__doc__)"
Ice Cream Shop Around the Corner

{shell-prompt-here}pip uninstall icecream
Found existing installation: icecream 0.1.dev2+gcd1df0f.d20220626
Uninstalling icecream-0.1.dev2+gcd1df0f.d20220626:
  Would remove:
    c:\repos\dell\icecream\lib\site-packages\icecream-0.1.dev2+gcd1df0f.d20220626.dist-info\*
    c:\repos\dell\icecream\lib\site-packages\icecream\*
Proceed (Y/n)? Y
  Successfully uninstalled icecream-0.1.dev2+gcd1df0f.d20220626
```


