## **Project Keyhole** ##
----------

A python framework to automatically backdoor binaries or source code

Steps of binary injection:

	 1. Decompile binary to source
	 2. Inject malware
	 3. Recompile binary

Steps of source injection:

	1. Determine source language
	2. Use appropriate malware
	3. Profit

Dependencies:
	
	python   (apt install python)        -- to run the framework
	java JDK (apt instapp openjdk-8-jdk) -- to decompile/recompile java jars
	pygments (pip install pygments)      -- to detect source code language

	
