import boto3

import os
 
# === Project Configuration ===

bucket_name = "my-polly-pixel"

region = "us-east-1"  # Update if your bucket is in a different region

output_filename = "speech-prod.mp3"

s3_key = f"polly-audio/{output_filename}"

input_file = "speech.txt"
 
# === Read text from local file ===

with open(input_file, "r") as file:

     text = file.read()
 
# === Initialize Polly and S3 clients ===

polly = boto3.client("polly", region_name=region)

s3 = boto3.client("s3", region_name=region)
 
# === Use Polly to synthesize speech ===

response = polly.synthesize_speech(

     Text=text,

     OutputFormat="mp3",

     VoiceId="Joanna"  # You can change to Matthew, Amy, etc.

 )
 
# === Save audio locally ===

local_path = f"/tmp/{output_filename}"

with open(local_path, "wb") as file:

     file.write(response["AudioStream"].read())
 
print(f"✅ Audio saved to {local_path}")
 
# === Upload to S3 ===

try:

     s3.upload_file(local_path, bucket_name, s3_key)

     print(f"✅ Uploaded to s3://{bucket_name}/{s3_key}")

except Exception as e:

     print(f"❌ Failed to upload: {e}")














