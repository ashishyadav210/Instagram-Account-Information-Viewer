import os
import time
import random
import string
import requests
from bs4 import BeautifulSoup
import json

# Clear the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Color codes for terminal
class Colors:
    RED = '\033[91m'
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Display the main interface
def display_interface():
    clear_screen()
    
    # Instagram ASCII Art in Red
    print(f"{Colors.RED}{Colors.BOLD}")
    print("█ █▄░█ █▀ ▀█▀ ▄▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█")
    print("█ █░▀█ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀░█")
    print(f"{Colors.END}")
    
    # Account Info Viewer in Purple
    print(f"{Colors.PURPLE}{Colors.BOLD}𝕬𝖈𝖈𝖔𝖚𝖓𝖙 𝕴𝖓𝖋𝖔 𝖁𝖎𝖊𝖜𝖊𝖗{Colors.END}")
    
    # Border line
    border = ""
    for i in range(50):
        if i % 2 == 0:
            border += f"{Colors.WHITE}█{Colors.END}"
        else:
            border += f"{Colors.BLACK}█{Colors.END}"
    print(border)
    print()

# Hacker type animation
def hacker_animation(username):
    print(f"{Colors.CYAN}Extracting information for {username}...{Colors.END}")
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    lines = [
        f"Connecting to Instagram servers...",
        f"Initializing secure connection...",
        f"Bypassing authentication...",
        f"Accessing user database...",
        f"Retrieving encrypted data...",
        f"Decrypting user information...",
        f"Analyzing account activity...",
        f"Compiling profile data...",
        f"Generating report...",
        f"Finalizing results..."
    ]
    
    for i in range(10):
        print(f"{Colors.YELLOW}{lines[i]}{Colors.END}", end="")
        for _ in range(20):
            print(f"{Colors.GREEN}{random.choice(chars)}{Colors.END}", end="", flush=True)
            time.sleep(0.05)
        print("\r" + " " * 80 + "\r", end="")
        time.sleep(0.5)
    
    print(f"{Colors.GREEN}✓ Information extraction complete!{Colors.END}")

# Generate random data
def generate_random_data():
    # Random email
    email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    email = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))) + "@" + random.choice(email_domains)
    
    # Random mobile number (10 digits)
    mobile = ''.join(random.choices(string.digits, k=10))
    
    # Random address
    states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    districts = ["Jaipur", "Mumbai City", "Kolkata", "Chennai", "Lucknow", "Patna", "Bhopal", "Hyderabad", "Bengaluru Urban", "Pune", "Surat", "Kanpur Nagar", "Nagpur", "Indore", "Thane", "Ghaziabad", "Visakhapatnam", "Agra", "Varanasi", "Meerut", "Nashik", "Rajkot", "Srinagar", "Dhanbad", "Amritsar", "Jodhpur", "Raipur", "Kota", "Guwahati (Kamrup Metropolitan)", "Gwalior", "Jabalpur", "Vijayawada", "Madurai", "Warangal", "Salem", "Tiruchirappalli", "Kochi (Ernakulam)", "Bhubaneswar (Khordha)", "Cuttack", "Dehradun", "Shimla", "Ranchi", "Jamshedpur (East Singhbhum)", "Bokaro", "Udaipur", "Ajmer", "Bikaner", "Alwar", "Gorakhpur", "Noida (Gautam Buddh Nagar)", "Aligarh", "Bareilly", "Moradabad", "Saharanpur", "Jhansi", "Mathura", "Firozabad", "Muzaffarnagar", "Bhavnagar", "Jamnagar", "Aurangabad (Chhatrapati Sambhajinagar)", "Solapur", "Kolhapur", "Amravati", "Nanded", "Akola", "Panipat", "Sonipat", "Rohtak", "Hisar", "Karnal", "Gurugram", "Faridabad", "Ludhiana", "Jalandhar", "Patiala", "Bathinda", "Hoshiarpur", "Mohali", "Anantapur", "Kurnool", "Nellore", "Guntur", "Prakasam", "Chittoor", "Kadapa", "Kozhikode", "Thiruvananthapuram", "Thrissur", "Kollam", "Kannur", "Palakkad", "Malappuram", "Alappuzha", "Mysuru", "Mangaluru (Dakshina Kannada)", "Hubli-Dharwad", "Belagavi", "Shivamogga"]
    villages = ["Mawlynnong", "Punsari", "Dhordo", "Majuli", "Malana", "Kollengode", "Ziro", "Gahmar", "Bara Basti", "Pothanikkad", "Khonoma", "Lamayuru", "Diskit", "Hunder", "Mandawa", "Kuldhara", "Lachen", "Yuksom", "Nako", "Chitkul", "Kalpa", "Sarahan", "Munsiyari", "Chopta", "Almora", "Binsar", "Kausani", "Gokarna", "Agumbe", "Hampi", "Badami", "Pattadakal", "Aihole", "Maravanthe", "St. Mary's Islands", "Mattur", "Shani Shingnapur", "Hiware Bazar", "Kila Raipur", "Kodini", "Shetpal", "Mayong", "Dhanushkodi", "Rameshwaram", "Kanyakumari", "Valparai", "Pollachi", "Theni", "Cumbum", "Bodinayakanur", "Munnar", "Thekkady", "Kumarakom", "Alleppey", "Varkala", "Bekal", "Wayanad", "Idukki", "Palakkad", "Kasargod", "Kannur", "Kozhikode", "Malappuram", "Thrissur", "Ernakulam", "Kottayam", "Pathanamthitta", "Alappuzha", "Kollam", "Thiruvananthapuram", "Cherrapunji", "Mawsynram", "Dawki", "Shillong", "Tawang", "Bomdila", "Itanagar", "Pasighat", "Along", "Daporijo", "Anini", "Tezu", "Roing", "Kohima", "Dimapur", "Wokha", "Mokokchung", "Zunheboto", "Phek", "Mon", "Tuensang", "Kiphire", "Longleng", "Peren", "Imphal", "Bishnupur"]
    pincode = ''.join(random.choices(string.digits, k=6))
    address = f"{random.choice(states)}, {random.choice(districts)}, {random.choice(villages)}, {pincode}"
    
    # Random mobile information
    phone_models = ["Apple iPhone 13", "Apple iPhone 13 Pro", "Apple iPhone 13 Pro Max", "Apple iPhone 14", "Apple iPhone 14 Plus", "Apple iPhone 14 Pro", "Apple iPhone 14 Pro Max", "Apple iPhone 15", "Apple iPhone 15 Plus", "Apple iPhone 15 Pro", "Apple iPhone 15 Pro Max", "Samsung Galaxy S21 FE 5G", "Samsung Galaxy S22", "Samsung Galaxy S22 Ultra 5G", "Samsung Galaxy S23", "Samsung Galaxy S23 Plus", "Samsung Galaxy S23 Ultra", "Samsung Galaxy S23 FE", "Samsung Galaxy A34 5G", "Samsung Galaxy A54 5G", "Samsung Galaxy M34 5G", "Samsung Galaxy F54 5G", "Redmi Note 10 Pro", "Redmi Note 11", "Redmi Note 11 Pro", "Redmi Note 12 5G", "Redmi Note 12 Pro 5G", "Redmi Note 13 5G", "Redmi 12C", "Poco X5 Pro 5G", "Poco X6 Pro 5G", "Poco F5 5G", "Poco M6 Pro 5G", "Realme 9 Pro 5G", "Realme 10 Pro 5G", "Realme 11 Pro Plus 5G", "Realme Narzo 50 5G", "Realme Narzo 60 5G", "Realme C55", "Realme P1 5G", "OnePlus Nord 2T 5G", "OnePlus Nord CE 3 Lite 5G", "OnePlus 11R 5G", "OnePlus 11 5G", "OnePlus Open", "OnePlus 12R 5G", "Google Pixel 6a", "Google Pixel 7", "Google Pixel 7a", "Google Pixel 8", "Google Pixel 8 Pro", "Nothing Phone 1", "Nothing Phone 2", "Nothing Phone 2a", "Moto G54 5G", "Moto G84 5G", "Motorola Edge 40", "Motorola Edge 40 Neo", "Motorola Edge 50 Pro", "Vivo V25 5G", "Vivo V27 5G", "Vivo V29e 5G", "Vivo Y36 5G", "Vivo T2 5G", "Oppo Reno 8 5G", "Oppo Reno 10 Pro 5G", "Oppo F23 5G", "Oppo A78 5G", "Oppo Find N3 Flip", "Infinix Note 30 5G", "Infinix Hot 30 5G", "Infinix Zero 30 5G", "Tecno Camon 20 Pro 5G", "Tecno Pova 5 Pro 5G", "Tecno Phantom X2 5G", "Lava Blaze 5G", "Lava Agni 2 5G", "Lava Storm 5G", "iQOO Neo 7 5G", "iQOO Neo 7 Pro 5G", "iQOO Z7 5G", "iQOO Z9 5G", "Samsung Galaxy A14 5G", "Samsung Galaxy A24", "Samsung Galaxy M14 5G", "Redmi 13C", "Redmi Note 13 Pro Plus 5G", "Realme C53", "Realme Narzo N55", "Vivo Y17s", "Vivo Y100 5G", "Oppo A58 5G", "Oppo A38", "Moto G14", "Moto G24 Power", "Google Pixel 6", "Google Pixel 5a 5G", "Apple iPhone SE 2022", "Samsung Galaxy Z Flip 5", "Samsung Galaxy Z Fold 5"]
    battery_levels = random.randint(65, 98)
    phone_info = f"{random.choice(phone_models)}, Battery: {battery_levels}%, OS: {random.choice(['iOS 15', 'Android 12', 'Android 11'])}"
    
    return email, mobile, address, phone_info

# Get Instagram profile information
def get_instagram_info(username):
    try:
        # This is a simplified approach and might not work reliably due to Instagram's restrictions
        url = f"https://www.instagram.com/{username}/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try to extract data from script tags
            scripts = soup.find_all('script')
            for script in scripts:
                if script.string and 'window._sharedData' in script.string:
                    try:
                        json_data = script.string.split(' = ')[1].rstrip(';')
                        data = json.loads(json_data)
                        
                        # Extract profile information
                        profile_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
                        
                        followers = profile_data['edge_followed_by']['count']
                        following = profile_data['edge_follow']['count']
                        posts = profile_data['edge_owner_to_timeline_media']['count']
                        bio = profile_data['biography']
                        
                        return {
                            'followers': followers,
                            'following': following,
                            'posts': posts,
                            'bio': bio
                        }
                    except (IndexError, KeyError, json.JSONDecodeError):
                        pass
            
            # If we couldn't extract from JSON, try to extract from HTML
            try:
                meta_description = soup.find('meta', attrs={'name': 'description'})
                if meta_description:
                    content = meta_description['content']
                    parts = content.split(' - ')
                    if len(parts) >= 2:
                        followers = parts[0].split(' ')[0].replace(',', '')
                        posts = parts[1].split(' ')[0].replace(',', '')
                        
                        # Try to get bio
                        bio_element = soup.find('meta', attrs={'property': 'og:description'})
                        bio = bio_element['content'] if bio_element else "Not available"
                        
                        return {
                            'followers': followers,
                            'following': "Not available",
                            'posts': posts,
                            'bio': bio
                        }
            except (AttributeError, IndexError):
                pass
        
        # If all else fails, return None
        return None
    except Exception as e:
        print(f"{Colors.YELLOW}Warning: Could not fetch real Instagram data. Using simulated data instead.{Colors.END}")
        return None

# Display the extracted information
def display_info(username):
    # Generate random data
    email, mobile, address, phone_info = generate_random_data()
    
    # Try to get real Instagram data
    real_data = get_instagram_info(username.lstrip('@'))
    
    # Display success message
    print(f"\n{Colors.GREEN}• Information Has Been Extracted Successful ✅{Colors.END}\n")
    
    # Display the information
    print(f"{Colors.CYAN}--> Account Username: {Colors.WHITE}{username}{Colors.END}")
    print(f"{Colors.CYAN}--> Account Status: {Colors.WHITE}Active{Colors.END}")
    print(f"{Colors.CYAN}--> Email: {Colors.WHITE}{email}{Colors.END}")
    print(f"{Colors.CYAN}--> Mobile Number: {Colors.WHITE}{mobile}{Colors.END}")
    print(f"{Colors.CYAN}--> Address: {Colors.WHITE}{address}{Colors.END}")
    print(f"{Colors.CYAN}--> Mobile Information: {Colors.WHITE}{phone_info}{Colors.END}")
    
    # Display real Instagram data if available
    if real_data:
        print(f"\n{Colors.PURPLE}• Instagram Profile Information:{Colors.END}")
        print(f"{Colors.CYAN}--> Followers: {Colors.WHITE}{real_data['followers']}{Colors.END}")
        print(f"{Colors.CYAN}--> Following: {Colors.WHITE}{real_data['following']}{Colors.END}")
        print(f"{Colors.CYAN}--> Posts: {Colors.WHITE}{real_data['posts']}{Colors.END}")
        print(f"{Colors.CYAN}--> Bio: {Colors.WHITE}{real_data['bio'][:100]}{'...' if len(real_data['bio']) > 100 else ''}{Colors.END}")
    else:
        # Generate random Instagram data if real data couldn't be fetched
        followers = random.randint(100, 10000)
        following = random.randint(50, 5000)
        posts = random.randint(80, 500)
        bio = "Null."
        
        print(f"\n{Colors.PURPLE}• Instagram Profile Information (Simulated):{Colors.END}")
        print(f"{Colors.CYAN}--> Followers: {Colors.WHITE}{followers}{Colors.END}")
        print(f"{Colors.CYAN}--> Following: {Colors.WHITE}{following}{Colors.END}")
        print(f"{Colors.CYAN}--> Posts: {Colors.WHITE}{posts}{Colors.END}")
        print(f"{Colors.CYAN}--> Bio: {Colors.WHITE}{bio}{Colors.END}")

# Main function
def main():
    display_interface()
    
    # Get username input
    username = input(f"{Colors.WHITE}• Send Instagram Username (Send With \"@\") Ex: @Instagram: {Colors.END}")
    
    # Validate username
    if not username.startswith('@'):
        username = '@' + username
    
    # Show hacker animation
    hacker_animation(username)
    
    # Display the information
    display_info(username)
    
    print(f"\n{Colors.YELLOW}Note: This tool/data is provided for informational and educational purposes only. Do not use it for any unethical or malicious activities. The user assumes full responsibility for their actions and any consequences that may arise from the use of this tool. The creator is not liable for any misuse or damage.{Colors.END}")

if __name__ == "__main__":
    main()
