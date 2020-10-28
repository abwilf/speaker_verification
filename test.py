from speaker_verification import *
import numpy as np

region = 'westus'
api_key = load_json('./real_secrets.json')['api_key']
wav_path = './enrollment.wav'
temp_path = './temp.wav'

# If you want to list users by profile_id
print('All users are: ', list_users(api_key, region))

# This is handled by the development / production code, but if you want to test the identification...
profile_id = create_profile(api_key, region)
enroll_user(api_key, region, wav_path, profile_id)

print(f'Likelihood that {wav_path} came from this subject')
identify_user(api_key, region, wav_path, profile_id)

print(f'Likelihood that {wav_path} came from this subject or another (randomly chosen)')
identify_user(api_key, region, wav_path, profile_ids=[profile_id, np.random.choice(list_users(api_key, region))])

print('Removing this profile id...')
remove_user(api_key, region, profile_id)
