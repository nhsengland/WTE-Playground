# WTE-Playground

A playground for members of the Workforce Training and Education team. This is a **public** repository.

# Table of Contents

- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

# Repository Structure

The repository is organized as follows:

- **datasets/**: Directory for storing datasets locally. Files in this directory are ignored by Git to prevent them from being committed.
- **scripts/**: Directory for individual contributor scripts. Each contributor can create and store their scripts here.
- **libs/**: Directory for shared code snippets and utility functions. Contributors can share reusable code snippets in this directory.
- **README.md**: This file, provides an overview of the repository and instructions for its use.
- **LICENSE**: License file specifying the terms under which the repository is distributed.
- **.gitignore**: Configuration file specifying files and directories to ignore in version control.
- **.gitattributes**: Configuration file specifying Git attributes, such as filters for Jupyter notebooks.

# Getting Started

To ensure no outputs from Jupyter Notebooks are committed to the repo, a filter has been created and is located within the .gitattributes file to remove outputs upon staging of the file. To add this filter to your local git configuration, open a terminal, navigate to the local repo and enter the following line:

```cmd
git config filter.clear_notebook_output.clean "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to notebook --inplace"
```

_Note: This filter runs on a file every time it is staged._

# Contributing

To contribute to this repository:

1. Clone the repository
2. Create a feature branch - be descriptive
3. Ensure you have configured git correctly
4. Commit your changes
5. Publish your branch/push your most recent changes
6. Open a pull request into main - each request **must** be reviewed by a team maintainer

Ensure you follow best practices when using Git/GitHub, such as:

1. Never commit anything sensitive such as passwords or real data
2. Use meaningful commit messages
3. Commit frequently
4. Do not commit Jupyter Notebook outputs

# License

Unless stated otherwise, the codebase is released under [the MIT Licence][mit].
This covers both the codebase and any sample code in the documentation.

_See [LICENSE](./LICENSE) for more information._

The documentation is [© Crown copyright][copyright] and available under the terms
of the [Open Government 3.0][ogl] license.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
