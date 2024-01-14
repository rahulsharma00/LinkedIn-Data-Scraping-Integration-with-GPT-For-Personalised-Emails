import openai
import os
import json

# Set your OpenAI API key
openai.api_key = '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'

def clean_text(text):
    return ' '.join(str(text).split())

def load_linkedin_data(username, folder_path='/Users/rahulsharma/Desktop/Zenskar/profile_data'):
    file_path = os.path.join(folder_path, f"{username}_profile_info.json")
    try:
        with open(file_path, 'r') as file:
            linkedin_data = json.load(file)
        return linkedin_data
    except FileNotFoundError:
        print(f"LinkedIn data file not found for username '{username}'.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON for username '{username}'.")
        return None

def save_to_txt(output_file_path, text):
    with open(output_file_path, 'w') as output_file:
        output_file.write(text)

def generate_and_save_emails(profile_data_folder, company_name='Zenskar'):
    output_folder = '/Users/rahulsharma/Desktop/Zenskar/emails'
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(profile_data_folder):
        if filename.endswith("_profile_info.json"):
            username = filename.split("_profile_info.json")[0]
            linkedin_data = load_linkedin_data(username, profile_data_folder)

            if linkedin_data:
                # Extract relevant information from LinkedIn data
                name = linkedin_data.get('Name', '')

                # Construct email for the specific LinkedIn user
                email_content = generate_personalized_email(linkedin_data, company_name)

                # Save the generated email to a text file
                file_name = f"{name.replace(' ', '_')}_{company_name}_email.txt"
                output_file_path = os.path.join(output_folder, file_name)
                save_to_txt(output_file_path, email_content)
                print(f"Generated email saved to: {output_file_path}")

def generate_personalized_email(linkedin_data, company_name='Zenskar', recipient_name='Jake'):
    if not linkedin_data:
        print("Invalid LinkedIn data.")
        return None

    # Extract relevant information from LinkedIn data
    name = linkedin_data.get('Name', '')
    job_title = linkedin_data.get('Experience', [{}])[0].get('Title', '')
    company = linkedin_data.get('Experience', [{}])[0].get('Company', '')

    # Construct prompt for GPT-3
    prompt = f"Generate a personalized email for {name} at {company} about {company_name}. {recipient_name}, {name} is the {job_title}. In your role, Zenskar can enhance your finance workflows with automated billing, accurate revenue recognition, and valuable insights. If interested, our billing tool can help implement these strategies. Can we schedule a quick call?"

    # GPT-3 API call
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.6,
        max_tokens=300
    )

    # Extract and return the generated email
    generated_email = response.choices[0].text.strip()

    # Adjustments to remove incorrect mentions
    generated_email = generated_email.replace("Zenskar Team", "Zenskar Team")

    return generated_email






# Example usage:
# Assuming you want to generate emails for all profiles in the specified folder
profile_data_folder = '/Users/rahulsharma/Desktop/Zenskar/profile_data'
generate_and_save_emails(profile_data_folder)
