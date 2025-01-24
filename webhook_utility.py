import os
import requests
import time
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_image(image_url):
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
        print(f"{Fore.RED}An error occurred while downloading the image: {e}")
        return None

def spam_webhook(webhook_url, message, count, delay, image_url=None):
    image_path = None
    if image_url:
        print(f"{Fore.YELLOW}Downloading image/GIF...")
        image_path = download_image(image_url)
        if not image_path:
            print(f"{Fore.RED}Skipping image/GIF due to download failure.")
    
    # Send spam messages
    for i in range(count):
        payload = {'content': message}
        files = {'file': open(image_path, 'rb')} if image_path else None

        try:
            response = requests.post(webhook_url, data=payload, files=files)
            if response.status_code in [200, 204]:
                print(f"{Fore.GREEN}Message {i+1}/{count} sent successfully: {message}")
            else:
                print(f"{Fore.RED}Failed to send message {i+1}/{count}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}An error occurred: {e}")
        finally:
            # Ensure the file is closed before attempting to delete it
            if files:
                files['file'].close()
        time.sleep(delay)

    # Clean up downloaded image file
    if image_path and os.path.exists(image_path):
        try:
            os.remove(image_path)
            print(f"{Fore.GREEN}Image/GIF file deleted successfully.")
        except PermissionError as e:
            print(f"{Fore.RED}Failed to delete image file: {e}")

def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(f"{Fore.GREEN}Webhook deleted successfully.")
        elif response.status_code == 404:
            print(f"{Fore.RED}Webhook not found. It may have already been deleted.")
        else:
            print(f"{Fore.RED}Failed to delete webhook. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}An error occurred while deleting the webhook: {e}")

def test_webhook(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}Webhook is valid and operational.")
        elif response.status_code == 404:
            print(f"{Fore.RED}Webhook not found.")
        else:
            print(f"{Fore.RED}Failed to test webhook. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}An error occurred while testing the webhook: {e}")

def validate_input(prompt, input_type, condition=lambda x: True, error_msg="Invalid input."):
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
    while True:
        clear_console()
        print(f"{Style.BRIGHT}{Fore.CYAN}Discord Webhook Utility")
        print(f"{Style.BRIGHT}{Fore.CYAN}=======================")
        print(f"{Style.BRIGHT}{Fore.YELLOW}1. Spam Webhook")
        print(f"{Style.BRIGHT}{Fore.YELLOW}2. Delete Webhook")
        print(f"{Style.BRIGHT}{Fore.YELLOW}3. Test Webhook")
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
                f"{Style.BRIGHT}{Fore.YELLOW}Enter the Discord webhook URL to test: ",
                str,
                lambda url: url.startswith("https://discord.com/api/webhooks/") or url.startswith("https://discordapp.com/api/webhooks/"),
                "Please enter a valid Discord webhook URL."
            )
            test_webhook(webhook_url)

        elif choice == 4:
            print(f"{Fore.GREEN}Exiting the program. Goodbye!")
            sys.exit(0)

        input(f"{Fore.YELLOW}Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
