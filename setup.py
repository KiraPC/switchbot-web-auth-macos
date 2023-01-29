from setuptools import setup

APP = ["src/app.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "src/icon.png",
    "plist": {
        "CFBundleShortVersionString": "0.2.0",
        "LSUIElement": True,
        "CFBundleURLTypes": [
            {
                "CFBundleURLName": "switchbot",
                "CFBundleURLSchemes": [
                    "switchbot"
                ]
            }
        ]
    },
    "packages": ["rumps",],
    "includes": ["os", "platform"],
}

setup(
    app=APP,
    name="switchbot",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=["rumps"],
)
