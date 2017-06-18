import subprocess

def captureImage(fileName):
	subprocess.call("./scripts/capture-image.sh " + fileName, shell=True)


