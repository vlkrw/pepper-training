Notes
-----

## #13

* Microphones directed to the front
* Blue Circling Eyes -> Listening
* Green Eyes -> Processing

* Tactile Sensors
    * 3 on top of the head
    *  top of hands

## #19
	
	• Shoulder Led for robot status

	Transportation

	• Push in red stop button
	• Move around (roll) with power latch open (unblocks the wheels)

## #26

* old settings page
```
${Robot}.local/advanced
```

## #33

* boot-config application via choregraphe + behavior.xar starts settings on tablet

	
# Misc

	
* If not in path

```
alias qicli="/cygdrive/c/Program\ Files\ \(x86\)/Aldebaran/Choregraphe\ Suite\ 2.5/bin/qicli.exe"
```
	
Python 2.7.x 32bit mandatory for NAOqi API
	
* Dictionaries can be found in 

```
    /.local/share/PackageManager/apps/dialog_lexicon/
```

* Logs can be found in

```	
    /var/log/naoqi/servicemanager
```	

* Virtual Robot on Windows is in 
	
    For choregraphe vm
        
        `%USER_HOME%\AppData\Roaming\choregraphe`
        
	For naoqi-bin.exe
			`%USER_HOME%\Roaming\PackageManager`
	
	
* Access Android Settings on Tablet
	
	`Session.service("ALTabletService")._openSettings()`
	
	
	
## Services
	
In manifest.xml (not possible to add via UI)
	
```	
<package>
	…
	<services>
		<service autorun="false" name="PythonAppMain" execStart="/usr/bin/python main.py"/>
	</services>
	<executableFiles> <!-- not ultimately necessary>
		<file path="main.py"/>
	</executableFiles>
	…
</package>
```

Service name should match the service name registered with naoqi
```
    service_id = app.session.registerService("PythonAppMain",service_instance)
```

Even better if the class name also matches and service name is retrieved like 
```
    self.__class__.__name__
``` 
For proper service registration on auto started apps see 
```
    15-111-ReservationService/reservation_service.py
```


