<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Python App" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="pythonapplauncher" src="pythonapplauncher/pythonapplauncher.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
        <File name="main" src="html/main.js" />
        <File name="soundset_browser" src="soundset_browser.py" />
        <File name="jquery.min" src="html/assets/jquery.min.js" />
        <File name="style" src="html/assets/style.css" />
        <File name="index-dropdown" src="html/index-dropdown.html" />
        <File name="index-colors" src="html/index-colors.html" />
    </Resources>
    <Topics>
        <Topic name="pythonapplauncher_enu" src="pythonapplauncher/pythonapplauncher_enu.top" topicName="pythonapplauncher" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
