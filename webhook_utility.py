import os
import requests
import time
import sys
from colorama import init, Fore, Style
from discord import Webhook

# Initialize colorama for colored output
init(autoreset=True)

def clear_console():
    """Clear the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def download_image(image_url):
    """Download an image or GIF from a given URL."""
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            filename = image_url.split("/")[-1]
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return filename
        else:
            print(f"{Fore.RED}Failed to download image. HTTP Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error downloading image: {e}")
        return None

def spam_webhook(webhook_url, message, count, delay, image_url=None):
    """Send multiple messages to a Discord webhook.

    Args:
        webhook_url (str): The Discord webhook URL.
        message (str): The message to send.
        count (int): Number of messages to send.
        delay (float): Delay between each message (in seconds).
        image_url (str, optional): URL of an image or GIF to attach.
    """
    image_path = None
    if image_url:
        print(f"{Fore.YELLOW}Downloading image/GIF...")
        image_path = download_image(image_url)
        if not image_path:
            print(f"{Fore.RED}Skipping image/GIF due to download failure.")
    
    for i in range(count):
        payload = {'content': message}
        files = {'file': open(image_path, 'rb')} if image_path else None

        try:
            response = requests.post(webhook_url, data=payload, files=files)
            if response.status_code in [200, 204]:
                print(f"{Fore.GREEN}Message {i+1}/{count} sent successfully.")
            else:
                print(f"{Fore.RED}Failed to send message {i+1}/{count}: HTTP {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Error occurred: {e}")
        finally:
            if files:
                files['file'].close()

        time.sleep(delay)

    if image_path and os.path.exists(image_path):
        try:
            os.remove(image_path)
            print(f"{Fore.GREEN}Image/GIF file deleted successfully.")
        except PermissionError as e:
            print(f"{Fore.RED}Failed to delete image file: {e}")

def delete_webhook(webhook_url):
    """Delete a Discord webhook.

    Args:
        webhook_url (str): The Discord webhook URL to delete.
    """
    try:
        if webhook_url.startswith("https://discord.com/api/webhooks/") or webhook_url.startswith("https://discordapp.com/api/webhooks/"):
            response = requests.delete(webhook_url)
            if response.status_code == 204:
                print(f"{Fore.GREEN}Webhook deleted successfully.")
            else:
                print(f"{Fore.RED}Failed to delete webhook. HTTP Status Code: {response.status_code}")
        else:
            print(f"{Fore.RED}Invalid webhook URL. Deletion aborted.")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error deleting webhook: {e}")

def get_webhook_info(webhook_url):
    """Retrieve and display information about a webhook.

    Args:
        webhook_url (str): The Discord webhook URL.
    """
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            json = response.json()
            print(f"Webhook Info:\n"
                  f"Name: {json['name']}\n"
                  f"Avatar URL: https://cdn.discordapp.com/avatars/{json['id']}/{json['avatar']}.png\n"
                  f"Guild ID: {json['guild_id']}\n"
                  f"Channel ID: {json['channel_id']}\n"
                  f"Webhook ID: {json['id']}\n"
                  f"Webhook Token: {json['token']}")
        else:
            print(f"{Fore.RED}Webhook not found or unable to retrieve information.")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error retrieving webhook info: {e}")

def validate_input(prompt, input_type, condition=lambda x: True, error_msg="Invalid input."):
    """Validate user input with custom conditions.

    Args:
        prompt (str): The input prompt message.
        input_type (type): The expected type of the input (e.g., int, float).
        condition (func): A function to validate the input.
        error_msg (str): Error message to display if validation fails.
    """
    while True:
        try:
            user_input = input_type(input(prompt))
            if condition(user_input):
                return user_input
            else:
                print(f"{Fore.RED}{error_msg}")
        except ValueError:
            print(f"{Fore.RED}Invalid input type. Please try again.")

def main():
    """Main program loop for the Discord Webhook Utility."""
    while True:
        clear_console()
        print(f"{Style.BRIGHT}{Fore.CYAN}Discord Webhook Utility")
        print(f"{Style.BRIGHT}{Fore.CYAN}=======================")
        print(f"{Style.BRIGHT}{Fore.YELLOW}1. Spam Webhook")
        print(f"{Style.BRIGHT}{Fore.YELLOW}2. Delete Webhook")
        print(f"{Style.BRIGHT}{Fore.YELLOW}3. Get Webhook Info")
        print(f"{Style.BRIGHT}{Fore.YELLOW}4. Exit")

        choice = validate_input(
            f"{Style.BRIGHT}{Fore.YELLOW}Enter your choice (1/2/3/4): ",
            int,
            lambda x: x in [1, 2, 3, 4],
            "Please choose 1, 2, 3, or 4."
        )

        if choice == 1:
            webhook_url = validate_input(
                f"{Style.BRIGHT}{Fore.YELLOW}Enter the Discord webhook URL: ",
                str,
                lambda url: url.startswith("https://discord.com/api/webhooks/") or url.startswith("https://discordapp.com/api/webhooks/"),
                "Please enter a valid Discord webhook URL."
            )
            message = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the message to spam: ").strip()
            count = validate_input(
                f"{Style.BRIGHT}{Fore.YELLOW}Enter the number of times to spam: ",
                int,
                lambda x: x > 0,
                "Count must be a positive integer."
            )
            delay = validate_input(
                f"{Style.BRIGHT}{Fore.YELLOW}Enter the delay between messages (in seconds): ",
                float,
                lambda x: x >= 1,
                "Delay must be at least 1 second to avoid rate limiting."
            )
            image_url = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter an image/GIF URL to include (leave blank for none): ").strip() or None
            spam_webhook(webhook_url, message, count, delay, image_url)

        elif choice == 2:
            webhook_url = validate_input(
                f"{Style.BRIGHT}{Fore.YELLOW}Enter the Discord webhook URL to delete: ",
                str,
                lambda url: url.startswith("https://discord.com/api/webhooks/") or url.startswith("https://discordapp.com/api/webhooks/"),
                "Please enter a valid Discord webhook URL."
            )
            delete_webhook(webhook_url)

        elif choice == 3:
            webhook_url = validate_input(
                f"{Style.BRIGHT}{Fore.YELLOW}Enter the Discord webhook URL to get info: ",
                str,
                lambda url: url.startswith("https://discord.com/api/webhooks/") or url.startswith("https://discordapp.com/api/webhooks/"),
                "Please enter a valid Discord webhook URL."
            )
            get_webhook_info(webhook_url)

        elif choice == 4:
            print(f"{Fore.GREEN}Exiting the program. Goodbye!")
            sys.exit(0)

        input(f"{Fore.YELLOW}Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
