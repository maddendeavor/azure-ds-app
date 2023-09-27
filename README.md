[![testcoverage](/doc/testcoverage_badge.svg)](/doc/testcoverage.txt)
[![maintainability](/doc/maintainability_badge.svg)](/doc/maintainability.txt)
[![docstring_coverage](/doc/docstringcoverage_badge.svg)](/doc/docstringcoverage.txt)
[![doc_style](https://img.shields.io/badge/%20style-numpy-459db9.svg)](https://numpydoc.readthedocs.io/en/latest/format.html)

# azure-ds-app
This project is using Azure Functions to develop a Basic Data Science app.

## Installation/Build Instructions
First you must create an azure account with the correct credentials.
And install [Azure Core function tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-csharp#install-the-azure-functions-core-tools)


## References
* https://learn.microsoft.com/en-us/azure/azure-functions/machine-learning-pytorch?tabs=bash
* https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators#publish-the-project-to-azure
* https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v1%2Cin-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-python#example
* https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators#development-options

## Contributing
* To contribute to the repository use the following:
```commandline
git clone <ENTER SSH HERE>
cd reponame
git lfs install
git checkout -b feature/feature_name
git add <files>
git commit -m "Add my feature"
git push origin feature/feature_name
```

* Create virtual environment
```commandline
python3 -m venv .venv
source .venv/bin/activate (linux) or source .venv/Scripts/activate (windows)
```

