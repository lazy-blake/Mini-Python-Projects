import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

URL = "https://appbrewery.github.io/gym/"
EMAIL = os.getenv("USER")
PASSWORD = os.getenv("PASS")
RETRIES = 10

user_data_dir = r"C:/Users/akash/OneDrive/Documents/Python/Projects/booking_automation/chrome_profile"

# Initialize counters
booked_count = 0
waitlist_count = 0
already_booked_count = 0
new_booked = []
new_waitlist = []


# Set up Chrome driver
def setup_driver():
    """Initialize Chrome driver with options"""
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("detach", True)
    driver_options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=driver_options)
    driver.get(URL)
    return driver


def login(driver):
    """Handle login process"""
    try:
        # Click login button
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

        # Wait for and fill email
        email_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "email-input"))
        )
        email_input.clear()
        email_input.send_keys(EMAIL)

        # Fill password
        password_input = driver.find_element(By.ID, "password-input")
        password_input.clear()
        password_input.send_keys(PASSWORD)

        # Submit login
        submit_button = driver.find_element(By.ID, "submit-button")
        submit_button.click()

        # Wait for successful login
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "logout-button"))
        )
        print("✓ Successfully logged in")
        return True

    except (TimeoutException, NoSuchElementException) as e:
        print(f"❌ Login failed: {e}")
        return False


def process_booking_button(
    driver, button, button_text, button_id, class_name, day_name
):
    """Process different booking button states"""
    global booked_count, waitlist_count, already_booked_count

    if button_text == "Booked":
        already_booked_count += 1
        print(f"✓ Already booked: {class_name} on {day_name}")

    elif button_text == "Waitlisted":
        already_booked_count += 1
        print(f"✓ Already waitlisted: {class_name} on {day_name}")

    elif button_text == "Book Class":
        try:
            button.click()
            WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element((By.ID, button_id), "Booked")
            )
            booked_count += 1
            new_booked.append((class_name, day_name))
            print(f"✓ Successfully booked: {class_name} on {day_name}")
        except TimeoutException:
            print(f"❌ Failed to book: {class_name} on {day_name}")

    elif button_text == "Join Waitlist":
        try:
            button.click()
            WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element((By.ID, button_id), "Waitlisted")
            )
            waitlist_count += 1
            new_waitlist.append((class_name, day_name))
            print(f"✓ Joined waitlist: {class_name} on {day_name}")
        except TimeoutException:
            print(f"❌ Failed to join waitlist: {class_name} on {day_name}")


def book_class(driver):
    """Book gym classes on Tuesday and Thursday at 6:00 PM"""
    try:
        # Wait for schedule page to load
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "schedule-page"))
        )
    except TimeoutException:
        print("❌ Schedule page failed to load")
        return False

    # Find all class cards
    all_classes = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
    print(f"Found {len(all_classes)} classes")

    for card in all_classes:
        try:
            # Get day information
            day_group = card.find_element(
                By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]"
            )
            day_name = day_group.find_element(By.TAG_NAME, "h2").text

            # Check if it's Tuesday or Thursday
            if "Tue" not in day_name and "Thu" not in day_name:
                continue

            # Get class time
            class_time = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

            # Check if it's 6:00 PM
            if "6:00 PM" not in class_time:
                continue

            # Get class name
            class_name = card.find_element(By.TAG_NAME, "h3").text

            # Find and process booking button
            book_button = card.find_element(
                By.CSS_SELECTOR, "button[id^='book-button-']"
            )
            button_text = book_button.text
            button_id = book_button.get_attribute("id")

            # NOTE: Calling the process booking function to actually book the classes
            process_booking_button(
                driver, book_button, button_text, button_id, class_name, day_name
            )

        except (TimeoutException, NoSuchElementException) as e:
            print(f"⚠️ Error processing a class card: {e}")
            continue

    return True


def verify_bookings(driver):
    """Verify bookings on My Bookings page"""
    try:
        # Navigate to My Bookings page
        my_bookings_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My Bookings"))
        )
        my_bookings_link.click()

        # Wait for page to load
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[id*='card-']"))
        )

        verified_bookings = 0
        all_bookings = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

        print("\n--- VERIFYING BOOKINGS ---")
        for card in all_bookings:
            try:
                time_date = card.find_element(By.TAG_NAME, "p").text

                if (
                    "Tue" in time_date or "Thu" in time_date
                ) and "6:00 PM" in time_date:
                    class_name = card.find_element(By.TAG_NAME, "h3").text
                    print(f"✓ Verified: {class_name}")
                    verified_bookings += 1

            except NoSuchElementException:
                continue

        return verified_bookings

    except (TimeoutException, NoSuchElementException) as e:
        print(f"❌ Error verifying bookings: {e}")
        return 0


def print_summary(verified_bookings=0):
    """Print booking summary"""
    total_processed = booked_count + waitlist_count + already_booked_count

    print("\n" + "=" * 50)
    print("           BOOKING SUMMARY")
    print("=" * 50)
    print(f"New bookings:           {booked_count}")
    print(f"New waitlists:          {waitlist_count}")
    print(f"Already booked/listed:  {already_booked_count}")
    print(f"Total processed:        {total_processed}")

    if new_booked:
        print("\n--- NEW BOOKINGS ---")
        for class_name, day in new_booked:
            print(f"• {class_name} on {day}")

    if new_waitlist:
        print("\n--- NEW WAITLISTS ---")
        for class_name, day in new_waitlist:
            print(f"• {class_name} on {day}")

    if verified_bookings > 0:
        print("\n--- VERIFICATION ---")
        print(f"Expected bookings: {total_processed}")
        print(f"Verified bookings: {verified_bookings}")

        if total_processed == verified_bookings:
            print("✅ SUCCESS: All bookings verified!")
        else:
            print(
                f"❌ MISMATCH: {abs(total_processed - verified_bookings)} booking(s) not matching"
            )


def run_with_retries(func, *args, max_retries=RETRIES, delay=3):
    """Run a function with retries"""
    for attempt in range(max_retries):
        try:
            if func(*args):
                return True
            print(f"Attempt {attempt + 1} failed. Retrying in {delay} seconds...")
            if (
                attempt < max_retries - 1
            ):  # so that it dont sleep agter the last attempt
                time.sleep(delay)

        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)

    print(f"❌ Failed after {max_retries} attempts")
    return False


def main():
    """Main execution function"""
    print("🤖 Starting Gym Booking Bot...")

    # Set up driver
    driver = setup_driver()

    try:
        # Login with retries
        if not run_with_retries(login, driver):
            print("❌ Login failed after all retries. Exiting.")
            return

        # Book classes with retries
        if not run_with_retries(book_class, driver, delay=5):
            print("❌ Booking failed after all retries.")
            return

        # Verify bookings
        verified_count = verify_bookings(driver)
        if verified_count == 0:
            verified_count = verify_bookings(driver)

        # Print summary
        print_summary(verified_count)

        # Keep browser open for inspection
        print("\nPress Enter to close the browser...")
        input()

    finally:
        driver.quit()


main()
