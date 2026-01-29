@echo off
echo ===============================
echo QA Automation Project Setup
echo ===============================

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Install Playwright browsers
echo Installing Playwright browsers...
playwright install

echo ===============================
echo Setup completed successfully!
echo ===============================
pause
