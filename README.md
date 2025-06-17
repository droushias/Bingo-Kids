Bingo Caller

A simple, standalone Bingo caller application built with Python and Pygame. Draws random bingo numbers, displays them in large text, and shows a history grid of previously drawn balls.

⸻

Features
	•	One-click executable for Windows/macOS/Linux—no Python install required
	•	Source version for developers to customize or extend
	•	Large, clear number display and history grid
	•	Greek (UTF-8) and English text support
	•	Startup screen with “Press to Start” button

⸻

Downloads

Download the latest release from the Releases page:
	•	Standalone ZIP (BingoCaller-vX.Y.zip)
	•	Contains a single executable (Windows .exe, macOS/Linux binary) for immediate launch
	•	Source ZIP (source-vX.Y.zip)
	•	Contains display.py, logic.py, requirements.txt, .gitignore, and this README

⸻

Running the Standalone
	1.	Download BingoCaller-vX.Y.zip for your operating system.
	2.	Extract the ZIP file.
	3.	Run the executable:
	•	Windows: double-click BingoCaller.exe in File Explorer.
	•	macOS/Linux:

cd path/to/extracted
chmod +x BingoCaller      # macOS/Linux only (once)
./BingoCaller



No additional setup or Python installation is required.

⸻

Running from Source

Use this if you’d like to view or modify the code.
	1.	Clone the repository

git clone https://github.com/your-username/your-repo.git
cd your-repo


	2.	Create a virtual environment

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1


	3.	Install dependencies

pip install -r requirements.txt


	4.	Launch the game

python display.py



⸻

Configuration
	•	Adjust WINDOW_WIDTH, WINDOW_HEIGHT in display.py for custom window sizes.
	•	Change GRID_COLS, GRID_ROWS, CELL_SIZE, CELL_SPACING, and GRID_PADDING to control history grid layout.
	•	Modify fonts and colors at the top of display.py for different visual themes.

⸻

Contributing

Contributions are welcome! Feel free to open issues or pull requests for:
	•	New features (e.g. sound effects, animations)
	•	Bug fixes or performance improvements
	•	Localization or accessibility enhancements

Please follow the existing code style and add tests where appropriate.

⸻

License

This project is released under the MIT License.