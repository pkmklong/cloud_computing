aws transcribe start-transcription-job 
--transcription-job-name $1
--language-code en-US
--media-format wav
--media MediaFileUrl=https://s3.amazonaws.com/contents.aws.a/$2/.wav
--output-bucket-name $3 
