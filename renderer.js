// Load Video
document.getElementById('loadVideo').addEventListener('click', async () => {
  const result = await window.electron.openFileDialog();
  if (result.length > 0) {
    videoPath = result[0];
    console.log('Video loaded:', videoPath);
  }
});

// Process Video
document.getElementById('processVideo').addEventListener('click', () => {
  if (!videoPath) {
    alert("Please load a video first.");
    return;
  }

  const command = `python ./scripts/extract_audio.py ${videoPath}`;
  window.electron.execPython(command)
    .then(result => {
      console.log('Audio extracted:', result);
      
      const detectCommand = `python ./scripts/detect_and_mute_music.py ${videoPath}`;
      window.electron.execPython(detectCommand)
        .then(result => {
          console.log('Music segments detected and muted:', result);
        })
        .catch(error => console.error('Error detecting and muting music:', error));
    })
    .catch(error => console.error('Error extracting audio:', error));
});

// Render Video
document.getElementById('renderVideo').addEventListener('click', () => {
  if (!videoPath) {
    alert("Please load and process the video first.");
    return;
  }

  const command = `python ./scripts/combine_video_and_audio.py ${videoPath}`;
  window.electron.execPython(command)
    .then(result => {
      console.log('Video rendered:', result);
    })
    .catch(error => console.error('Error rendering video:', error));
});
