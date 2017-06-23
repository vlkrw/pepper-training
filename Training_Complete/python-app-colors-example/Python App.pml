<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Python App" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="color" src="color/color.dlg" />
        <Dialog name="pythonapplauncher" src="pythonapplauncher/pythonapplauncher.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
        <File name="main" src="html/main.js" />
        <File name="main" src="main.py" />
    </Resources>
    <Topics>
        <Topic name="color_enu" src="color/color_enu.top" topicName="color" language="en_US" />
        <Topic name="pythonapplauncher_enu" src="pythonapplauncher/pythonapplauncher_enu.top" topicName="pythonapplauncher" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
</Package>
