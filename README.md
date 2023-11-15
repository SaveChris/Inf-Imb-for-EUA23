# Supplementary material for the paper "Investigating the price determinants of the European Carbon Trading System: a non-parametric approach" by C. Salvagnin, A. Glielmo, M.E. De Giuli, A. Mira
This repository contains the supplementary material for the paper "Investigating the price determinants of the European Carbon Trading System: a non-parametric approach" by C. Salvagnin, A. Glielmo, M.E. De Giuli, A. Mira. The paper is available at **[link]**.

## Overview
The European carbon market (EU ETS), a carbon emission allowance trading system designed by the European Union, is one of the most important instruments that should allow to achieve carbon neutrality by 2050. The total emissions of greenhouse gases that can be emitted by the operators within the market is known as the cap, which is reduced over time in order to reduce the total EU emissions. The amount of carbon emissions caused by production activities is closely related to the environmental, social, and economic framework. The identification of the key elements driving the carbon market price is crucial for implementing all the possible actions to supervise, identify trends in the market and avoid the arises of inefficiencies - like speculative behaviours - that can reduce the ability of the instrument to pursue the objective of carbon neutrality. The Information Imbalance is a recently introduced nonparametric measure to quantify the information content that sets of variables contain with respect to target variables and can thus be used to identify the most informative set of features out of a pool of candidates without specific assumptions on the relation existing between predictors and a target. In our work, we exploit the Information Imbalance to investigate the relevance and the (causal) relationships amongst macroeconomic, economic, uncertainty and energy variables, and the EU ETS price.

## Table of contents
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Code](#code)
  - [Data](#data)
- [Documentation](#documentation)
   - [f_Docs](#f_Docs)
- [Figures](#figures)
- [Contributing](#contributing)
- [License](#license)

## Getting started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- [Python](https://www.python.org/) = 3.11
- [dadapy](https://dadapy.readthedocs.io/en/latest/#) = 0.2.0
- [scikit-learn](https://scikit-learn.org/stable/) = 1.3.0
- [pandas](https://pandas.pydata.org/) = 2.0.3
- [numpy](https://numpy.org/) = 1.24.3
- [scipy](https://www.scipy.org/) = 1.11.1
- [statsmodels](https://www.statsmodels.org/stable/index.html) = 0.14.0
- [matplotlib](https://matplotlib.org/) = 3.7.2
- [seaborn](https://seaborn.pydata.org/) = 0.12.2

### Installation
1. **Clone the repository:**

   ```bash
   git clone https://github.com/SaveChris/Inf-Imb-for-EUA23.git

    cd Inf-Imb-for-EUA23
    ```
2. **Navigate to the project directory:**

   ```bash
   cd Inf-Imb-for-EUA23
   ```

3. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```
   **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```
This command installs all the necessary packages to run the code specified in **'requirements.txt'** file.

5. **Run the project**

   ```bash
   python main.py
   ```
   This command runs the main file of the project, which contains the code to reproduce the results of the paper.

6. **Congratulations!**
Your project should now be up and running!

Adjust the steps and commands based on your project's specific requirements. If your project involves a different language or tool, you may need to tailor the installation instructions accordingly. Additionally, providing clear and concise instructions with helpful comments can significantly enhance the user experience. If you run into some problems or you have any questions [contact me](mailto:c.salvagnin@unibs.it), or [Aldo Glielmo](mailto:aldo.glielmo@gmail.com).

## Usage
This work is based on Jupiter notebooks, the user can find, for each section of the paper the corresponding notebook. The user can run the notebook to reproduce the results of the paper.

### Code
The [Code](#code) section is organized as follows:
- **'0_data_preparation.ipynb'** contains the code to prepare the data used in the paper.
- **'1_introduction.ipynb'** contains the code to reproduce the plots in the *Introduction* section.
- **'2_methodology.ipynb'** contains the code to reproduce the results in *Methdology* section.
- **'3_empirical_analysis.ipynb'** contains the code to reproduce the results in *Empirical analysis* section.
- **'4_methodological_results.ipynb'** contains the code to reproduce the results in *Methodological results* section.
- **'appendix.ipynb'** contains the code to reproduce the results in *Appendix* section.
- **'f_plots'** contains the custom function for all the plotting in the paper.
- **'f_imb'** contains the custom function for the Information Imbalance analysis.
- **'f_gp'** contains the custom function for the Gaussian Process analysis. 

### Data
The [Data](#data) section is organized as follows:
- **'Dataset_EUA23.xlsx'** contains the raw dataset, used in the data preparation code.
- **'daily_phases_data.txt'** contains the data used for the Phase 3 and 4 comparison in the paper.
- **'daily_data.txt'** contains the daily data used in the paper.
- **'weekly_data.txt'** contains the monthly data used in the paper.
- **'monthly_data.txt'** contains the quarterly data used in the paper.

## Documentation
The [Documentation](#documentation) section is organized as follows:
- **'paper.pdf'** contains the paper.
- **'presentation.pdf'** contains the presentation of the paper.
- [f_Docs](#f_Docs) sub-section contains the documentation of the custom functions:
   - **'f_plot_doc.md'** contains the documentation of the custom function for all the plotting in the paper.
   - **'f_imb_doc.md'** contains the documentation of the custom function for the Information Imbalance analysis.
   - **'f_gp_doc.md'** contains the documentation of the custom function for the Gaussian Process analysis.

## Figures
The [Figures](#figures) section contains the figures used in the paper, numbered as in the paper.

## Contributing
We welcome contributions to improve **Inf-Imb-forEUA23**!
If you encounter any issues or have suggestions for improvements, please check the existing issues to see if the topic has already been discussed. If not, feel free to [contact me](mailto:c.salvagnin@unibs.it) or [Aldo Glielmo](mailto:aldo.glielmo@gmail.com).
You should provide the following information when opening an issue:

- A descriptive title
- Steps to reproduce the issue (if applicable)
- Expected behavior
- Actual behavior
- Environment details (e.g., operating system, Python version)
- Screenshots, if applicable

Thank you for your contributions!

## License
This project is licensed under the Apache License 2.0 - see the [License](LICENSE.txt) file for details.