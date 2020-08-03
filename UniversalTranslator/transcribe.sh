function transcribe() {
aws transcribe start-transcription-job \
    --transcription-job-name testing \
    --language-code en-US \
    --media-format mp4  \
    --media MediaFileUri=https://s3.amazonaws.com/aws-bucket-fun/testing.mp4 \
    --output-bucket-name aws-bucket-fun  
}

transcribe
