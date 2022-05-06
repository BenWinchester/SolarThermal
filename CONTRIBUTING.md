# Contributing to SolarThermal

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to **SolarThermal**, which is hosted [on GitHub](https://github.com/BenWinchester/SolarThermal). These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[How to contribute to SolarThermal](#how-to-contribute-to-solar-thermal)
  * [Reporting bugs](#reporting-bugs)
  * [Merging patches](#merging-patches)
    * [Cosmetic patches](#cosmetic-patches)
  * [Questions](#questions)
  * [Contributing to the documentation](#contributing-to-the-documentation)

[Styleguides](#styleguides)
  * [Git commit messages](#git-commit-messages)
  * [Python styleguide](#python-styleguide)
  * [YAML styleguide](#yaml-styleguide)
  * [Changing styleguides](#changing-styleguides)

[Additional Notes](#additional-notes)
  * [Issue and pull request labels](#issue-and-pull-request-labels)


### Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the development team.

## How to contribute to SolarThermal

### Reporting bugs

**Did you find a bug?** Bugs make it into our code from time to time. If you spot a bug, report it as follows:

* **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/BenWinchester/SolarThermal/issues).

* If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/BenWinchester/SolarThermal/issues/new/choose). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

  * If the issue is a **bug**, use the [Bug report](https://github.com/BenWinchester/SolarThermal/issues/new?assignees=&labels=bug&template=bug_report.md&title=) template,

  * If the issue is a **feature** request for something new that you would like to see introduced into SolarThermal, use the [Feature request](https://github.com/BenWinchester/SolarThermal/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=) template.

### Merging patches

**Did you write a patch that fixes a bug?** If you have coded a solution for a bug that you have found or for an open issue, open a pull request for it as follows:

* Open a new GitHub pull request with the patch.

* Ensure the PR description clearly describes the problem and solution:

  * Include the relevant issue number if applicable,

  * Follow the template information presented, filling in all the fields requested which are relevant to your patch.

* Ensure that you include at least one administrator reviewer for your pull request. Without an appropriate review, you will be unable to merge your pull request.

#### Cosmetic patches

**Did you fix whitespace, format code, or make a purely cosmetic patch?** Changes that are cosmetic in nature and do not add anything substantial to the stability, functionality, or testability of SolarThermal will generally not be accepted. Contact the developers directly, or save your cosmetic changes until you are able to merge them as part of a feature or bug issue.

### Questions

**Do you have questions about the source code?** Ask any question about how to use SolarThermal on the [Discussions](https://github.com/BenWinchester/SolarThermal/discussions) page.

### Contributing to the documentation

**Do you want to contribute to the SolarThermal documentation?** SolarThermal is an ever-evolving piece of software. If you want to contribute to the SolarThermal documentation, get in touch with the development team. SolarThermal documentation updates are usually produced for major releases.

## Styleguides

### Git commit messages

* Git Commit Messages
* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include [ci skip] in the commit title
* Consider starting the commit message with an applicable emoji:
  * 🎨 `:art:` when improving the format/structure of the code
  * 🐎 `:racehorse:` when improving performance
  * 📝 `:memo:` when writing docs
  * 🐧 `:penguin:` when fixing something on Linux
  * 🍎 `:apple:` when fixing something on macOS
  * 🏁 `:checkered_flag:` when fixing something on Windows
  * 🐛 `:bug:` when fixing a bug
  * 🔥 `:fire:` when removing code or files
  * 💚 `:green_heart:` when fixing the CI build
  * ✅ `:white_check_mark:` when adding tests
  * 🔒 `:lock:` when dealing with security
  * ⬆️ `:arrow_up:` when upgrading dependencies
  * ⬇️ `:arrow_down:` when downgrading dependencies
  * 👕 `:shirt:` when removing linter warnings

### Python styleguide

All `Python` code must conform to [mypy](https://github.com/python/mypy) and [pylint](https://github.com/PyCQA/pylint) coding standards and must be formatted with the [black](https://github.com/psf/black) formatter:
* A `mypy.ini` file within the root of the repository sets out the requirements that must be met by any code. Use `python -m mypy src/` to ensure that your code complies with the guidelines.
  * The `pandas` package used throughout SolarThermal does not correctly lint with `mypy`. As such, it is acceptable to use the `# type: ignore` comment at the end of any pandas lines to avoid `mypy` errors, though these should be kept to a minimum.
* A `.pylintrc` file within the root of the repository sets out the linting requirements. Use `python -m pylint src/` to ensure that your code complies with the guidelines.
* All code must be formatted with `black`.

These tests must pass for any pull request to be successfully approved and merged. You can run these tests from the root of the repository with `./bin/test-solar-thermal.sh`.

### YAML styleguide

All `.yaml` files which are modified are linted with [yamllint](https://github.com/adrienverge/yamllint). You can use `yamllint -c .yamllint-config.yaml` to run `yamllint` over any `.yaml` files that you have modified.

### Changing styleguides

If you have any changes for the styleguides, make these **very clear** within your pull request message. It is unusual to have to change the styleguides to make your code pass the required tests.

## Additional notes

### Issue and pull request labels

| Label name | `BenWinchester/SolarThermal` :mag_right: | Description |
| --- | --- | --- |
| `bug` | [search](search-solar-thermal-repo-label-bug) | Confirmed bugs or reports that are very likely to be bugs. |
| `documentation` | [search](search-solar-thermal-repo-label-documentation) | Improvements or additions to documentation. |
| `duplicate` | [search](search-solar-thermal-repo-label-duplicate) | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `enhancement` | [search](search-solar-thermal-repo-label-enhancement) | New feature or request. |
| `feature` | [search](search-solar-thermal-repo-label-feature) | A new feature for SolarThermal, considerably more important than an enhancement. |
| `good first issue` | [search](search-solar-thermal-repo-label-good-first-issue) | Less complex issues which would be good first issues to work on for users who want to contribute to SolarThermal. |
| `good masters issue` | [search](search-solar-thermal-repo-label-good-masters-issue) | More complex issues which would be good issues to work on as part of an MSc project. |
| `helpwanted` | [search](search-solar-thermal-repo-label-help-wanted) | The feature or bug requires more work or attention than would be used for an ordinary issue. |
| `invalid` | [search](search-solar-thermal-repo-label-invalid) | Issues which aren't valid (e.g. user errors). |
| `needs-reproduction` | [search](search-solar-thermal-repo-label-needs-reproduction) | Likely bugs, but haven't been reliably reproduced. |
| `not-urgent` | [search](search-solar-thermal-repo-label-not-urgent) | Not an urgent fix, can be sorted down the line. |
| `question` | [search](search-solar-thermal-repo-label-question) | Questions more than bug reports or feature requests (e.g. how do I do X). You should **raise questions in the discussions page** rather than raising an issue if possible. |
| `wontfix` | [search](search-solar-thermal-repo-label-wontfix) | The SolarThermal core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |

Thanks! :heart: :heart: :heart:

SolarThermal Team
