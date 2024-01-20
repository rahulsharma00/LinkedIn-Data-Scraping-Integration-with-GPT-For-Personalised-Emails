from linkedin_api import Linkedin
import os
import json

def clean_text(text):
    return ' '.join(str(text).split())

def get_profile_data(api, username):
    try:
        profile_data = api.get_profile(username)
        return profile_data
    except Exception as e:
        print(f"Error retrieving data for the username '{username}': {str(e)}")
        return None

def save_to_json(output_file_path, data_dict):
    with open(output_file_path, 'w') as output_file:
        json.dump(data_dict, output_file, indent=2)

def process_linkedin_data(profile_data):
    if not profile_data:
        return None

    # Extract relevant information
    first_name = clean_text(profile_data.get('firstName', ''))
    last_name = clean_text(profile_data.get('lastName', ''))
    about = clean_text(profile_data.get('summary', ''))

    # Extract education details
    education_details = []
    for edu in profile_data.get('education', []):
        school = clean_text(edu.get('school', {}).get('schoolName', ''))
        degree = clean_text(edu.get('degreeName', ''))
        field_of_study = clean_text(edu.get('fieldOfStudy', ''))
        grade = clean_text(edu.get('grade', ''))
        education_details.append({
            'School': school,
            'Degree': degree,
            'Field of Study': field_of_study,
            'Grade': grade
        })

    # Extract top skills
    top_skills = [clean_text(skill.get('name', '')) for skill in profile_data.get('skills', [])]

    # Extract experience details
    experience_details = []
    for job in profile_data.get('experience', []):
        company_name = clean_text(job.get('companyName', ''))
        title = clean_text(job.get('title', ''))
        start_date = job.get('timePeriod', {}).get('startDate', {})
        end_date = job.get('timePeriod', {}).get('endDate', {})
        description = clean_text(job.get('description', ''))

        start_month = start_date.get('month', '')
        start_year = start_date.get('year', '')
        end_month = end_date.get('month', '')
        end_year = end_date.get('year', '')

        experience_entry = {
            'Title': title,
            'Company': company_name,
            'Start Date': f"{start_month}/{start_year}" if start_month and start_year else '',
            'End Date': f"{end_month}/{end_year}" if end_month and end_year else 'Present',
            'Description': description
        }
        experience_details.append(experience_entry)

    data_dict = {
        'Name': f"{first_name} {last_name}",
        'About': about,
        'Education': education_details,
        'Top Skills': top_skills,
        'Experience': experience_details
    }

    return data_dict

def main():
    api = Linkedin('EMAIL', 'PASSWORD')
    username = input("Enter the username: ")

    profile_data = get_profile_data(api, username)
    processed_data = process_linkedin_data(profile_data)

    if processed_data:
        output_folder = '/Users/rahulsharma/Desktop/Zenskar/profile_data'
        os.makedirs(output_folder, exist_ok=True)

        file_name = f"{username}_profile_info.json"
        output_file_path = os.path.join(output_folder, file_name)

        save_to_json(output_file_path, processed_data)

        print(f"Output saved to {output_file_path}")
    else:
        print(f"Failed to process and retrieve data for the username: {username}")

if __name__ == "__main__":
    main()
