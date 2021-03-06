# Speaker Verification Using Azure

## Setup
1. Clone this repository
2. Log into your [azure console](https://portal.azure.com/#home).  You must have some kind of Azure subscription before moving on.
3. Click "Create a Resource", then search for "Speech", and click "Create".
4. Name the resource, associate it with a subscription, and make sure the location is **(US) West US**.  Select **Standard S0** pricing tier.  Add it to, or create a new resource group to hold this resource.
5. Click "Go to Resource"-> "Keys and Endpoint" (on the left), and copy one of the keys (either one). Paste it in `secrets.json` in place of `YOUR_API_KEY_HERE`.

## Usage
1. Make sure you're in this working directory (if not, `cd speaker_verification` first).
2. Install requirements
```
pip install librosa soundfile numpy
```
3. Record the person speaking.  This recording should be 30 seconds to a minute in length, and the subject can say anything in English.  Noise should be minimal.  Name the file `enrollment.wav`.  As long as you save the file as a `.wav`, the program should make any other adjustments (e.g., sample rate, bit encoding) to conform to the API's requirements.
4. Enter this command, and a new user will be created with the enrollment wav file.
```
python3 speaker_verification.py
```
You should see an output like this:
```
Profile id is:
72bf0c07-ed74-40d1-b732-d4b25cb8d081
Enrollment successful!
```
5. For advanced cases (or curiosity) see `test.py`, reproduced below:
```
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
```