# Quick WhatsApp Group Creator

This project automates the process of adding participants to a WhatsApp group using Selenium and Python. It reads phone numbers from a `.csv` file and adds them to an existing WhatsApp group.

## Features

- **Automated Participant Addition**: Automatically adds multiple participants to a specified WhatsApp group.
- **CSV File Input**: Reads phone numbers from a `.csv` file.
- **Simple Interface**: Minimal user input required to specify the `.csv` file, phone number column, and WhatsApp group name.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- pandas

You can install the required Python packages using pip:

```bash
pip install selenium pandas
```

## Usage

1. **Prepare Your CSV File**: Ensure your `.csv` file is formatted correctly with a column containing phone numbers. The column name should be unique and easy to identify.

2. **Run the Script**:

   - Clone the repository or download the script.
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python:

     ```bash
     python quick_whatsapp_group_creator.py
     ```

3. **Input Required Information**:

   - Enter the name of your `.csv` file when prompted (without the `.csv` extension).
   - Enter the name of the column containing the phone numbers.
   - Enter the name of the WhatsApp group to which you want to add members.

4. **Scan WhatsApp QR Code**:

   - The script will open WhatsApp Web in a Chrome browser.
   - Scan the QR code using your mobile device to log in.

5. **Adding Participants**:

   - The script will search for the specified WhatsApp group and start adding participants based on the phone numbers from the `.csv` file.
   - Once the process is complete, you will need to manually confirm the addition by clicking the green tick button.

6. **Exit**:

   - Press `Enter` after adding all participants to close the browser and end the session.

## Notes

- Ensure that your ChromeDriver version matches your installed Chrome version.
- The script assumes that the WhatsApp Web interface is in English. If your interface is in another language, you may need to adjust the XPaths accordingly.
- The script does not handle errors that may occur if a phone number is not registered on WhatsApp.

## Disclaimer

This script is for educational purposes only. Automating interactions with WhatsApp Web may violate WhatsApp's terms of service. Use at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
