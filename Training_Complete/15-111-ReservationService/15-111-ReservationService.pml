<?xml version="1.0" encoding="UTF-8" ?>
<Package name="15-111-ReservationService" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="my_super_service" src="reservation_service.py" />
        <File name="translation_en_US" src="translations/translation_en_US.ts" />
        <File name="index" src="html/index.html" />
        <File name="jquery.min" src="html/jquery.min.js" />
        <File name="stl" src="html/stl.css" />
    </Resources>
    <Topics>
        <Topic name="reservation_enu" src="reservation/reservation_enu.top" topicName="reservation" language="en_US" />
        <Topic name="reservation_frf" src="reservation/reservation_frf.top" topicName="reservation" language="fr_FR" />
    </Topics>
    <IgnoredPaths />
</Package>
