# PyPart: Partogram Generation Tool

PyPart is a Jupyter Notebook-based tool designed to simplify the process of generating partograms from CSV files. Utilizing the power of Matplotlib, PyPart converts raw clinical data into a visually informative partogram, assisting healthcare professionals in auditing the progress of labour efficiently, as well as presenting partograms in a matter suitable for inclusion in academic publications.

## Features

-   **Automated Partogram Generation:** Quickly convert CSV data into a detailed partogram.
-   **Interactive Jupyter Notebook Interface:** Easy to use and modify for different datasets.
-   **Customizable Visualization:** Adapt the partogram to meet specific needs.

## Installation

Clone the repository to get started:

```bash
git clone https://github.com/CillySu/PyPart.git
cd PyPart
```

Ensure you have Jupyter Notebook, Numpy and Matplotlib installed:

```bash
pip install notebook matplotlib
```

Run Jupyter Notebook (or use Google Colab, VSCode, etc):

```bash
jupyter notebook
```

## Usage

Open the `PyPart.ipynb` file in Jupyter Notebook. Load your CSV file and run the notebook to generate the partogram.

## CSV File Format

The CSV file should follow this structure:

```csv
Time, CervicalDilation, FetalHeartRate, MaternalHeartRate, MaternalSystolic, MaternalDiastolic
16:30, 4, 130, 88, 100, 63
16:45, , 120, 82, ,
17:00, , 120, 78, ,
17:15, , 130, 75, 113, 70
17:30, 10, 112, 80, ,
```

-   `Time` is in HH:MM format.
-   `CervicalDilation` is measured in cm.
-   `FetalHeartRate`, `MaternalHeartRate`, `MaternalSystolic`, and `MaternalDiastolic` are measured in bpm and mmHg, respectively.
-   Empty fields are permissible for missing data points.

## Screenshot

![Sample Partogram](https://i.imgur.com/9FA6sTd.jpg)

## Contributing

Contributions are welcome! Please read our contributing guidelines for more information.

