# Discord Webhook Utility

A powerful and user-friendly tool for managing Discord webhooks. With this utility, you can:
- **Spam a webhook** with custom messages and optional media.
- **Delete a webhook** with a simple command.
- **Test the validity** of a webhook.

## Features
- **Spam Webhook: Send a message to a webhook multiple times with a custom delay.**
- **Delete Webhook: Delete a specified webhook.**
- **Test Webhook: Verify if a webhook is operational.**

## Installation

To install and set up the `Discord Webhook Utility`, follow these steps:

### 1. Prerequisites
Before installing the utility, ensure that you have the following software installed:

- **Python**: Python: The latest version of Python. You can download it from [here](https://www.python.org/downloads/).
- **pip**: pip: Python's package manager, which is typically included with Python.

### 2. Download the Repository
Clone or download the repository to your local machine.

```bash
git clone https://github.com/ZoniBoy00/discord-webhook-utility.git
```

### 3. Install Dependencies
Navigate to the folder where the repository is saved and run the install.bat file. This will install all the necessary Python libraries.

```bash
install.bat
```
This will automatically install the required dependencies listed in the requirements.txt file.

If you face any issues during installation (e.g., missing dependencies), the script will provide error messages to guide you through the troubleshooting process.

### 4. Run the Utility
Once the installation is complete, you can start using the tool by running the start.bat file:

```bash
start.bat
```
This will start the utility and display an interactive menu where you can choose to:

- Spam a webhook
- Delete a webhook
- Test a webhook
- Exit the application

## Usage
### Main Menu
Upon running the tool, you will see a menu with the following options:

```
1. Spam Webhook
2. Delete Webhook
3. Test Webhook
4. Exit
```

### 1. Spam Webhook
- **Webhook URL**: Enter the Discord webhook URL you want to spam.
- **Message**: Specify the message you wish to send.
- **Count**: Set the number of times you want to send the message.
- **Delay**: Choose the delay between each message (in seconds).
- **Image/GIF URL (Optional)**: You can provide an image or GIF URL to include in the messages.

### 2. Delete Webhook
- **Webhook URL**: Provide the URL of the webhook you wish to delete. The tool will attempt to delete it from Discord.

### 3. Test Webhook
- **Webhook URL**: Enter the webhook URL you want to test. The tool will check if it is valid and operational.

### 4. Exit
This will exit the program.

## Customization
You can customize the tool by editing the Python script. You can modify the default settings or add new features as needed.

## Troubleshooting
- **Python not installed**: Make sure you have Python installed and that it's added to your system's PATH.
- **Pip not installed**: If pip is not installed, download the latest version of Python, which includes pip.
- **Failed to install dependencies**: If the install.bat file fails, check your internet connection and make sure you're running the script with administrator privileges.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/ZoniBoy00/Discord-Webhook-Utility/blob/main/LICENSE) file for details.

## Contribution
Feel free to contribute to this project by forking the repository and submitting pull requests. If you have any ideas for new features or improvements, don't hesitate to open an issue or send a pull request.

## Contact
If you have any questions or feedback, you can reach out to me through the GitHub Issues.
