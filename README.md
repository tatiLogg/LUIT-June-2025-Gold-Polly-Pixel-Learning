LUIT-June-2025-Gold-Polly-Pixel-Learning

This project demonstrates a CI/CD pipeline that uses Amazon Polly and S3 to convert educational text into audio automatically. It supports both beta (preview) and production-ready voice outputs.


Setup Instructions

1. AWS Credentials & S3 Bucket
- Create an S3 bucket (e.g., 'my-polly-pixel')
- Add a folder prefix inside S3 named 'polly-audio/'
- Create a new IAM user with permissions to 'PutObject' and 'GetObject' on your S3 bucket
- Generate AWS access keys for that user

Save the following secrets in GitHub:
- 'AWS_ACCESS_KEY_ID'
- 'AWS_SECRET_ACCESS_KEY'
- 'AWS_REGION' (e.g., 'us-east-1')
- 'S3_BUCKET_NAME' (e.g., 'my-polly-pixel')


Modify Text Content
To change the spoken audio:

1. Open 'speech.txt'
2. Edit the text to anything you'd like Amazon Polly to convert to speech
3. Commit the changes and push to GitHub



Workflow Automation

Preview Audio (Beta)
- File: '.github/workflows/on_pull_request.yml'
- Trigger: On Pull Requests targeting 'main'
- Output: 'polly-audio/speech-beta.mp3'

Production Audio
- File: '.github/workflows/on_merge.yml'
- Trigger: On push to 'main' (e.g. after PR merge)
- Output: 'polly-audio/speech-prod.mp3'


Verifying the Results
Go to your AWS S3 console and check the contents of the 'polly-audio/' folder.

You should see:
: 'speech-beta.mp3' (after a PR)
: 'speech-prod.mp3' (after a merge to 'main')

Click the object name to download or stream the audio file.


Why Amazon Polly?
- Serverless + No ML training
- Realistic neural voices
- Easy integration using 'boto3'
- Fast synthesis for real-time automation

Why GitHub Actions?
- Automates preview and production audio flows
- Runs entirely in the GitHub developer workflow
- Secure, isolated environments with secrets handling


Created for:
Pixel Learning Co., a digital-first education startup focused on accessibility and automation.
#LUIT-June-2025-Gold-Polly-Pixel-Learning
