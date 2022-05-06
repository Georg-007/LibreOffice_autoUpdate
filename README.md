# LibreOffice autoUpdate

This is a program to update LibreOffice automatically, because LibreOffice itself does net provide this option yet.
It gets the latest version from the website and can download and run it.
It cannot see the currently installed version, but LibreOffice will notify you when an update is available. Then you can install it here.
It is currently only available for Windows x64, support for Linux, macOS and x86 architecture is planned (you can of course change the url in the source code to math your os).

## Getting Started

### Installing

Download the installer from [here](https://github.com/Georg-007/LibreOffice_autoUpdate/releases/download/v1.0/LibreOffice_autoUpdate-Installer.exe) and run it. Follow the instructions there.
You can also use the portable version stored in [LibreOffice_autoUpdate.exe](bin/LibreOffice_autoUpdate.exe).

## Deployment

The binary was built with pyinstaller and the auto-py-to-exe gui. The configuration ist stored in [comp.json](comp.json) (You will have to update the paths to match your files' locations.).
Alternatively, you can run the python source directly, make sure to install dependencies with
```
pip install -r requirements.txt
```
in the repository.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the Unlicense - see the [LICENSE.md](LICENSE.md) file for details.
