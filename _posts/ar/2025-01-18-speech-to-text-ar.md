---
audio: false
generated: false
image: false
lang: ar
layout: post
title: نقل Google Cloud
translated: true
---

لقد قمت مؤخرًا بتجربة واجهة برمجة التطبيقات (API) الخاصة بتحويل الكلام إلى نص من Google Cloud. فيما يلي دالة Python استخدمتها لإجراء عملية النسخ.

```python
import os
import argparse
from google.cloud import storage

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    يقوم بتحويل ملف صوتي إلى نص باستخدام واجهة برمجة التطبيقات (API) الخاصة بتحويل الكلام إلى نص من Google Cloud.

    Args:
        audio_gcs_uri: رابط GCS لملف الصوت.
        output_gcs_folder: رابط GCS للمجلد لتخزين النص المحول.
        language_code: رمز اللغة للتحويل (مثل "en-US"، "cmn-CN").
    """
    client = SpeechClient()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config={},
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
    )

    output_config = cloud_speech.RecognitionOutputConfig(
        gcs_output_config=cloud_speech.GcsOutputConfig(uri=output_gcs_folder),
    )

    files = [cloud_speech.BatchRecognizeFileMetadata(uri=audio_gcs_uri)]

    request = cloud_speech.BatchRecognizeRequest(
        recognizer="projects/graphite-ally-445108-k3/locations/global/recognizers/_",
        config=config,
        files=files,
        recognition_output_config=output_config,
    )
    operation = client.batch_recognize(request=request)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    print(response)


def process_audio_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    all_audio_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
    total_files = len(all_audio_files)
    print(f"Total audio files to process: {total_files}")

    if total_files == 0:
        print(f"No audio files found in '{input_dir}' directory.")
        return

    files_processed = 0

    for filename in all_audio_files:
        audio_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        if os.path.exists(output_filename):
            print(f"Skipping {filename}: {output_filename} already exists.")
            continue
        print(f"\nProcessing {files_processed + 1}/{total_files}: {filename}")
        try:
            # تحديد اللغة بناءً على لاحقة اسم الملف
            if filename.endswith('-zh.mp3') or filename.endswith('-zh.wav') or filename.endswith('-zh.m4a'):
                language_code = "cmn-CN"
            else:
                language_code = "en-US"

            # بناء روابط GCS
            gcs_audio_uri = f"gs://test2x/audio-files/{filename}"  # استبدل مع سطل ومجلدك
            gcs_output_uri = f"gs://test2x/transcripts/{os.path.splitext(filename)[0]}" # استبدل مع سطل ومجلدك
            
            # تحميل الملف إلى GCS إذا لم يكن موجودًا
            # هذا الجزء غير مطبق، ستحتاج إلى إضافة كود لتحميل الملف إلى GCS
            # على سبيل المثال، باستخدام مكتبة google-cloud-storage

            storage_client = storage.Client()
            bucket = storage_client.bucket("test2x")
            blob = bucket.blob(f"audio-files/{filename}")
            if not blob.exists():
                blob.upload_from_filename(audio_file_path)
                print(f"Uploaded {filename} to GCS.")
            else:
                print(f"{filename} already exists in GCS.")


            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code
            )
            files_processed += 1
            print(f"File {files_processed}/{total_files} processed.\n")

            # تنزيل النص المحول
            output_gcs_uri_json = f"{gcs_output_uri}/{os.path.splitext(filename)[0]}_transcript_*.json"
            
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{os.path.splitext(filename)[0]}")
            
            for blob in blobs:
                if blob.name.endswith(".json"):
                    local_output_path = os.path.join(output_dir, os.path.basename(blob.name))
                    blob.download_to_filename(local_output_path)
                    print(f"Downloaded {blob.name} to {local_output_path}")


        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            continue

    print(f"Processing complete! {files_processed}/{total_files} files processed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process audio files to generate transcriptions.")
    parser.add_argument('--input_dir', type=str, default="assets/audios", help="Input directory for audio files.")

    args = parser.parse_args()

    process_audio_files(
        input_dir=args.input_dir,
        output_dir=OUTPUT_DIRECTORY,
    )

```

النتيجة. تم تعديلها لإظهار عينة من مخرجات JSON، مع إزالة بعض القيم للإيجاز. سيحتوي JSON الكامل على معلومات أكثر تفصيلاً.

```json
{
    "results": [
        {
            "alternatives": [
                {
                    "transcript": "Here's To The Crazy Ones The Misfits the Rebels the troublemakers the round pegs in the square holes the ones who see things differently they're not fond of rules and they have no respect for the status quo",
                    "confidence": 0.95684826,
                    "words": [
                        {
                            "startOffset": "1s",
                            "endOffset": "4.200s",
                            "word": "Here's",
                            "confidence": 0.8265989
                        },
                        {
                            "startOffset": "4.200s",
                            "endOffset": "4.400s",
                            "word": "To",
                            "confidence": 0.9994259
                        },
                        {
                            "startOffset": "4.400s",
                            "endOffset": "4.400s",
                            "word": "The",
                            "confidence": 0.9994259
                        },
                        {
                            "startOffset": "4.400s",
                            "endOffset": "4.900s",
                            "word": "Crazy",
                            "confidence": 0.9975712
                        },
                        {
                            "startOffset": "4.900s",
                            "endOffset": "5.100s",
                            "word": "Ones",
                            "confidence": 0.9904002
                        },
                        {
                            "startOffset": "5.100s",
                            "endOffset": "6.700s",
                            "word": "The",
                            "confidence": 0.9994307
                        },
                        {
                            "startOffset": "6.700s",
                            "endOffset": "7.200s",
                            "word": "Misfits",
                            "confidence": 0.9352707
                        },
                        {
                            "startOffset": "7.200s",
                            "endOffset": "8.400s",
                            "word": "the",
                            "confidence": 0.99881697
                        },
                        {
                            "startOffset": "8.400s",
                            "endOffset": "8.800s",
                            "word": "Rebels",
                            "confidence": 0.9900544
                        },
                        {
                            "startOffset": "8.800s",
                            "endOffset": "10.300s",
                            "word": "the",
                            "confidence": 0.99904335
                        }                        
                    ]
                }
            ],
            "resultEndOffset": "23.780s",
            "languageCode": "en-us"
        }
    ]
}
```