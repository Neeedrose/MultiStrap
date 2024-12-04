<p align="center">
    <img src="https://raw.githubusercontent.com/Neeedrose/MultiStrap/refs/heads/main/multistrap.ico" align="center" width="30%">
</p>
<p align="center"><h1 align="center">MultiStrap</h1></p>
<p align="center">
	<em><code>❯ MultiStrap</code></em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Selenium-43B02A.svg?style=default&logo=Selenium&logoColor=white" alt="Selenium">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>
<br>

##  Table of Contents

- [ Overview](#overview)
- [ Notes](#notes)
- [ Getting Started](#getting-started)
  - [ Prerequisites](#prerequisites)
  - [ Installation](#installation)
  - [ Usage](#usage)
- [ Project Roadmap](#project-roadmap)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)

---

##  Overview

❯ This script creates a GUI application using tkinter to automate the launch of multiple ROBLOX accounts. It uses Selenium to log in and save cookies, which are then used to authenticate and launch the accounts. The application allows the user to specify a Place ID, Game/Job ID, and the number of accounts to launch. It supports background threading for launching accounts with a delay between each, and can stop active ROBLOX processes. The script also handles Windows-specific message loops for continuous operation and includes error handling for common issues.

---

##  Notes

❯ With a lot of Roblox clients your computer may lag, you can add Fast Flags to BloxStrap that can make it perform better.

---
##  Getting Started

###  Prerequisites

[**BloxStrap**](https://github.com/bloxstraplabs/bloxstrap) - Uses BloxStrap because it made everything more simple to launch.

###  Installation

Install MultiStrap using one of the following methods:

**Build from source:**

1. Clone the MultiStrap repository:
```sh
❯ git clone https://github.com/Neeedrose/MultiStrap.git
```

2. Navigate to the project directory:
```sh
❯ cd MultiStrap
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

**Run EXE:**

1. Go to the releases tab and click the latest version. From there you will find the exe to download and run.



###  Usage
Run MultiStrap using the following command:
**Using `python`** &nbsp; [<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">](https://www.python.org/)

```sh
❯ python {entrypoint}
```

---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Add a GUI.</strike>
- [ ] **`Task 2`**: Add joining users.
- [ ] **`Task 3`**: Add joining private servers.

---

##  Contributing

- **💬 [Join the Discussions](https://discord.gg/e4d5bxZQ)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Neeedrose/MultiStrap/issues)**: Submit bugs found or log feature requests for the `MultiStrap` project.
- **💡 [Submit Pull Requests](https://github.com/Neeedrose/MultiStrap/pulls)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your LOCAL account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone MultiStrap
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to LOCAL**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributors</summary>
<br>
<p align="left">
    <a href="https://github.com/neeedrose/multistrap/graphs/contributors">
  	<img src="https://contrib.rocks/image?repo=neeedrose/multistrap" />
    </a>

Made with [contrib.rocks](https://contrib.rocks).
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE]() file.

---

##  Acknowledgments

- Used some parts of [ROBLOX-desktop-launcher by pizzaboxer](https://github.com/pizzaboxer/ROBLOX-desktop-launcher)
- Thanks for explaining this pizzaboxer. [A deep dive on how the Roblox bootstrapper works](https://github.com/bloxstraplabs/bloxstrap/wiki/A-deep-dive-on-how-the-Roblox-bootstrapper-works)

---
