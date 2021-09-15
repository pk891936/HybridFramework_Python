REM ***************grouping Test  after pytest.ini
python -m pytest -v -s -m "mytest" -n=2 --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
REM python -m pytest -v -s -m "regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
REM python -m pytest -v -s -m "sanity and regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
REM python -m pytest -v -s -m "sanity or regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 

REM python -m pytest -v -s --html=HTMLReports\APITestreport.html --self-contained-html --capture=tee-sys API_Automation\TestCases\test_End_To_End.py
REM python -m pytest -v -s -n=2 --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases/test_searchCustomerByEmail_Action.py --browser chrome
REM python -m pytest -v -s -n=2 --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases/test_searchCustomerByName_Action.py --browser chrome
REM python -m pytest -v -s -n=2 --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases/test_Login_Allure.py --browser chrome



PAUSE