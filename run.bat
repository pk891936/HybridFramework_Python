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

REM C://Users//Praveen//PycharmProjects//Hybrid_Framework//Drivers//chromedriver.exe
REM python -m pytest -v -s testCases/test_Login.py
REM python -m pytest -v -s testCases/test_Login.py --browser chrome
REM python -m pytest -v -s -n=2 testCases/test_Login.py --browser chrome
REM python -m pytest -v -s -n=2 --html=HTMLReports\report.html testCases/test_Login.py --browser chrome ####parallel run
REM python -m pytest -v -s --html=HTMLReports\report.html --self-contained-html testCases/test_Login.py --browser chrome
REM 
REM python -m pytest -v -s -n=2 --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases/test_Login_Actions.py --browser chrome
REM python -m pytest -v -s --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases/test_Login.py --browser chrome
REM python -m pytest -v -s --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases/test_new.py --browser chrome
REM 
REM ###grouping Test  after pytest.ini
REM python -m pytest -v -s -m "sanity" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
REM python -m pytest -v -s -m "regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
REM 
REM 
REM python -m pytest -v -s -m "regression" --html=HTMLReports\report.html --self-contained-html --capture=tee-sys testCases --browser chrome 
REM python -m pytest -v -s --alluredir=./reports testCases\test_tableDataExtraction.py --browser chrome 
REM API Testing
REM python -m pytest -v -s --html=HTMLReports\APITestreport.html --self-contained-html --capture=tee-sys API_Automation\TestCases\test_End_To_End.py
REM python -m pytest -v -s --html=HTMLReports\APITestreport.html --self-contained-html --capture=tee-sys API_Automation\CoopsAPI_Automation\test_End_To_End.py
REM python -m pytest -v -s --alluredir=./reports API_Automation\CoopsAPI_Automation\test_End_To_End.py
REM python -m pytest -v -s --html=HTMLReports\APITestreport.html --self-contained-html --capture=tee-sys API_Automation\TestCases\test_peopleAPI.py
REM _______________________________________________________________________________________________________________________________________________________________
REM python -m pytest -v -s API_Automation\TestCases\test_End_To_End.py
REM 
REM Allure Report
REM python -m pytest -v -s --alluredir=./reports --self-contained-html --capture=tee-sys API_Automation\TestCases\test_End_To_End.py
REM 
REM cmd for allure report
REM 
REM allure generate --clean C:\Users\Praveen\PycharmProjects\Hybrid_Framework\Reports