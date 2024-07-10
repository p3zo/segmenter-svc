# Segmenter SVC

Segmenter SVC identifies temporal segments in structured music. It takes as input an audio file and outputs timestamps for segment boundaries and labels for each segment.

To run the service locally, run

```bash
python run_handler.py --filepath=PATH_TO_AUDIO_FILE
```

To build the zip for uploading to AWS Lambda, run

```bash
./aws_lambda/scripts/build_lambda.sh
```
