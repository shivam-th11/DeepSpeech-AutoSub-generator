**AutoSub**

	AutoSub
 
		About
		How it works
		Motivation
		References
	
**About**

AutoSub is a CLI application to generate subtitle files (.srt, .vtt, and .txt transcript) for any video file using either Mozilla DeepSpeech or Coqui STT. I use their open-source models to run inference on audio segments and pyAudioAnalysis to split the initial audio on silent segments, producing multiple smaller files (makes inference easy).

⭐ Featured in DeepSpeech Examples by Mozilla

**How it works**

Mozilla DeepSpeech is an open-source speech-to-text engine with support for fine-tuning using custom datasets, external language models, exporting memory-mapped models and a lot more. You should definitely check it out for STT tasks. So, when you run the script, I use FFMPEG to extract the audio from the video and save it in audio/. By default DeepSpeech is configured to accept 16kHz audio samples for inference, hence while extracting I make FFMPEG use 16kHz sampling rate.

Then, I use pyAudioAnalysis for silence removal - which basically takes the large audio file initially extracted, and splits it wherever silent regions are encountered, resulting in smaller audio segments which are much easier to process. I haven't used the whole library, instead I've integrated parts of it in autosub/featureExtraction.py and autosub/trainAudio.py. All these audio files are stored in audio/. Then for each audio segment, I perform DeepSpeech inference on it, and write the inferred text in a SRT file. After all files are processed, the final SRT file is stored in output/.

When I tested the script on my laptop, it took about 40 minutes to generate the SRT file for a 70 minutes video file. My config is an i5 dual-core @ 2.5 Ghz and 8GB RAM. Ideally, the whole process shouldn't take more than 60% of the duration of original video file.

**Motivation**

	In the age of OTT platforms, there are still some who prefer to download movies/videos from YouTube/Facebook or even torrents rather than stream. I am one of them and on one such occasion, I couldn't find the subtitle file for a particular movie I had downloaded. Then the idea for AutoSub struck me and since I had worked with DeepSpeech previously, I decided to use it.


**Reference**

	https://github.com/mozilla/DeepSpeech/
          
    https://github.com/tyiannak/pyAudioAnalysis
          
	https://deepspeech.readthedocs.io/
