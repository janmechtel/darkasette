# darkasette
A [datasette](https://datasette.io/) exploration of the [Hunchly Dark Web Reports](https://www.hunch.ly/darkweb-osint/)

# How to reproduce
1. Clone this repo
1. Sign up for the [Hunchly Dark Web Reports](https://www.hunch.ly/darkweb-osint/)
1. You'll receive a dropbox link to download the reports
1. Extract reports into the folder `rawreports/` 
     
    1. Either download individual reports - or -
    1. Click "Download Archive" and extract all from the .zip file 
1. Run all cells in the `import.ipynb` notebook
1. Run `datasette serve darkasette.db` to start the server


# Requirements
- `pip install datasette, sqlite3, pandas, openpyxl`