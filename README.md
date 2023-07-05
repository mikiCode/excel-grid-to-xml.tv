<h1>Excel TV grid to XMLTV</h2>
<p>API made with FastAPI to upload excel TV grid to XMLTV format. </p>
Sample TV grid was randomly generated based on the structure of the real TV grid leaving only crucial data for the project and simplified for development purpose.</p>
<p>"Channel 1 20230702 20230710.json" represents parsed excel file of the sample TV grid.</p>
<hr>

## Installation
```bash
pip install -r requirements.txt
```
## Usage
```bash
python app/main.py
```
## Project status
<b>Work in progress</b>
## Things to do
- [x] Upload excel grid file
  - [x] Create POST endpoint in FastAPI to upload excel file
  - [x] Parse excel file with pandas to format date and time to format suitable for XMLTV
  - [x] Save parsed data to .json file with name of the file as channel and date of the grid
  - [ ] Add configuration file to remember settings for excel file
- [ ] Fetch data from .json file and create XMLTV file
  - [ ] Create XMLTV file
  - [ ] Add data from .json file to XMLTV file
  - [ ] Save XMLTV file
- [ ] Reorganize project structure
- [ ] Add docker to project
  
## License
[MIT](https://choosealicense.com/licenses/mit/)

