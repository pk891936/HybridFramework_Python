REM ***************grouping Test  after pytest.ini
REM python -m pytest -v -s -m "sanity" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
REM python -m pytest -v -s -m "regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
python -m pytest -v -s -m "sanity and regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
 

REM python -m pytest -v -s -m "sanity or regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 

PAUSE