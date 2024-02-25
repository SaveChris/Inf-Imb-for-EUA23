# Supplementary material for the paper "Investigating the price determinants of the European Carbon Trading System: a non-parametric approach" by C. Salvagnin, A. Glielmo, M.E. De Giuli, A. Mira
This repository contains the supplementary material for the paper "Investigating the price determinants of the European Carbon Trading System: a non-parametric approach" by C. Salvagnin, A. Glielmo, M.E. De Giuli, A. Mira.

## Overview
The European carbon market plays a pivotal role in the European Union's ambitious target of achieving carbon neutrality by 2050. Understanding the intricacies of factors influencing EU ETS market prices is paramount for effective policy making and strategy implementation. Employing the Information Imbalance, a non-parametric measure, the study delves into the relationships among macroeconomic, economic, uncertainty, and energy variables concerning EUA prices.
The EU Allowances price (EUA) went through different phases. Our analysis shows that, in Phase 3, the ERIX index, is the most important variable to explain the behaviours of the price. Its close price behaviour to EUA indicates similar market dynamics, underscoring the relevance of renewable energy considerations. Transitioning to Phase 4, financial fluctuations take center stage, with the uncertainty in the EUR/CHF exchange rate emerging as a crucial determinant. The dataset reflects the disruptive impacts of the COVID-19 pandemic and the energy crisis, reshaping the information content.
Beyond variable analysis, the Information Imbalance methodology extends to time scale selection, identifying the weekly time scale as the most informative. This insight enhances our understanding of the temporal dynamics shaping EUA prices. Additionally, the study employs Gaussian Processes for nowcasting and forecasting predictions, emphasising the precision achieved by focusing on the three most informative variables identified by the Information Imbalance approach.
This study provides nuanced insights into the evolving dynamics of the EUA price, shedding light on the changing significance of key variables across different phases. From renewable energy considerations to financial fluctuations, the research navigates through these complexities, offering valuable perspectives for stakeholders in the carbon market landscape.

## Table of contents
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [SRC](#SRC)
  - [Data](#data)
- [Documentation](#documentation)
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

Adjust the steps and commands based on your project's specific requirements. If your project involves a different language or tool, you may need to tailor the installation instructions accordingly. Additionally, providing clear and concise instructions with helpful comments can significantly enhance the user experience. If you run into some problems or you have any questions contact me [(Cristiano Salvagnin)](mailto:c.salvagnin@unibs.it), or [Aldo Glielmo](mailto:aldo.glielmo@gmail.com).

## Usage
This work is based on Jupiter notebooks, the user can find, for each section of the paper the corresponding notebook. The user can run the notebook to reproduce the results of the paper.

### SRC
The [SRC](https://github.com/SaveChris/Inf-Imb-for-EUA23/tree/main/SRC) section is organized as follows:
- **'Sec_1_Introduction.ipynb'** contains the code to reproduce the results obtained in *Section 1 - Introduction*;
- **'Sec_3_Methods.ipynb'** contains the code to reproduce the results obtained in *Section 3 - Methods*;
- **'Sec_4_Price_determinants.ipynb'** contains the code to reproduce the results in *Section 4 - Price_determinants*;
- **'Sec_5_Time-scale_aggregation_and_forecasting.ipynb'** contains the code to reproduce the results in *Section 5 - Time-scale aggregation and forecasting*;
- **'A_appendix.ipynb'** contains the code to reproduce the results in *Appendix*;
- **'S_Supplementary_material.ipynb'** contains the code to reproduce supplementary results;
- **'check_equal_distances.py'** contains new custom function for analyzing the distances between points;
- **'utils_perturb.py'** contains new custom function for random perturbation of points;
- **'utils_zero_dist_imbalance.py'** contains the custom function for dealing with zero distance points. 

### Data
The [Data](https://github.com/SaveChris/Inf-Imb-for-EUA23/tree/main/Data) section is organized as follows:
- **'Dataset_EUA23.xlsx'** contains raw dataset;
- **'Dataset_Sample_GDP_Weekly.xlsx'** contains dataset used for the imputation and aggregation example;
- **'Dataset_X_Final_Weekly.xlsx'** contains dataset used for the imputation and imputation example;
- **'Dataset_eua_IMv4.3.xlsx'** contains raw dataset;
- **'Dataset_eua_Macro_V1.xlsx'** contains raw macroeconomic dataset;
- **'DescriptiveStatisticsAll.xlsx'** contains the descriptive statistics of the data;
- **'biweekly_data.txt'** contains the biweekly data used in the paper;
- **'daily_data.txt'** contains the daily data used in the paper;
- **'monthly_data.txt'** contains the quarterly data used in the paper;
- **'weekly_data.txt'** contains the monthly data used in the paper.

## Documentation
The [Documentation](https://github.com/SaveChris/Inf-Imb-for-EUA23/tree/main/Documentation) section is organized as follows:
- **'Inf_Imb_EUA_23.pdf'** contains the paper.
- **'Inf_Imb_EUA_23_p.pdf'** contains the presentation of the paper.

## Figures
The [Figures](https://github.com/SaveChris/Inf-Imb-for-EUA23/tree/main/Figures) section contains the figures used, numbered as in the paper.

## Contributing
We welcome contributions to improve **Inf-Imb-forEUA23**!
If you encounter any issues or have suggestions for improvements, please check the existing issues to see if the topic has already been discussed. If not, feel free to contact me [(Cristiano Salvagnin)](mailto:c.salvagnin@unibs.it) or [Aldo Glielmo](mailto:aldo.glielmo@gmail.com).
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