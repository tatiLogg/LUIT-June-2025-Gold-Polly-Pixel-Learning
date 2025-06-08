import boto3
import os

# Initialize Polly client
polly = boto3.client('polly')

# Read text from file
with open('speech.txt', 'r') as file:
    text = file.read()

# Synthesize speech
response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'  # You can change this to another voice like 'Matthew'
)

# Get the output file name from environment variable, fallback to speech.mp3
output_filename = os.getenv('OUTPUT_FILE', 'speech.mp3')

# Save the audio stream to a file
with open(output_filename, 'wb') as out_file:
    out_file.write(response['AudioStream'].read())

print(f"✅ Speech synthesized and saved as '{output_filename}'")

# Optional: Upload to S3 if environment variables are present
bucket = os.getenv('S3_BUCKET')
if bucket:
    s3 = boto3.client('s3')
    s3.upload_file(output_filename, bucket, output_filename)
    print(f"✅ Uploaded to s3://{bucket}/{output_filename}")














