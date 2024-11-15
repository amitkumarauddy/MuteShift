const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  execPython: (command) => ipcRenderer.invoke('exec-python', command),
  openFileDialog: () => ipcRenderer.invoke('open-file-dialog')  // Added file dialog function
});
