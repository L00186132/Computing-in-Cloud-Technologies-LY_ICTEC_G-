
<br>

<!-- INSERT ICON AND TITLE -->
<div align="center">
  <img src="../images/temp_Logo.png" alt="Icon" width="80" height="50">
  <a name="top"></a>
  <h3 align="center">Status Report</h3>
</div>

<br>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#project-status">Project Status</a></li>
    <li><a href="#highlights">HighLights</a></li>
    <li><a href="#risks">Risks</a></li>
    <li><a href="#improvements">Improvements</a></li>
    <li><a href="#other-updates">Other Updates</a></li>
  </ol>
</details>

<br><br>


<!-- PROJECT STATUS -->
## Project Status
This project contains a fully working codebase for a temperature monitor system. The code has been designed to monitor network data transfer across a network using UDP (User Datagram Protocol). More details can be found in following sections.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- HIGHLIGHTS -->
### HighLights

<span style="color:lightgreen">*All code listed is this repository is fully working to specifications*</span>



Assignment1\
├─ config\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ <span style="color:yellow">*properties_email.py*</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ <span style="color:yellow">*properties_server.py*</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ <span style="color:yellow">*properties_temperature.py*</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ <span style="color:yellow">*properties_udp.py*</span>\
├─ docs\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ <span style="color:grey">*Status.md*</span>\
├─ images\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ <span style="color:grey">*temp_Logo.png.md*</span>\
├─ src\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ <span style="color:while">alert</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ <span style="color:lightgreen">*generate_email_test.py*</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ <span style="color:lightgreen">*generate_email.py*</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ <span style="color:while">reporting</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ <span style="color:lightgreen">*generate_logs_test.py*</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ <span style="color:lightgreen">*generate_logs.py*</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ <span style="color:while">server</span>\
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ <span style="color:lightgreen">*udp_server.py*</span>\
└─ <span style="color:lightgreen">*main.py*</span>

<br>

* <span style="color:yellow">*properties_email.py*</span> - for easy modification of email parameters,
* <span style="color:yellow">*properties_server.py*</span> - for easy modification of server parameters,
* <span style="color:yellow">*properties_temperature.py*</span> - for easy modification of temperature threshold,
* <span style="color:yellow">*properties_udp.py*</span> - for easy modification of udp network parameters,
* <span style="color:lightgreen">*generate_email_test.py*</span> - unittest for testing email functionality,
* <span style="color:lightgreen">*generate_email.py*</span> - allows for ability to send email notifications,
* <span style="color:lightgreen">*generate_logs_test.py*</span> - unittest for testing logging functionality,
* <span style="color:lightgreen">*generate_logs.py*</span> - allows for logging of received network data packets,
* <span style="color:lightgreen">*upd_server.py*</span> - allows for continual monitoring of network traffic,
* <span style="color:lightgreen">*main.py*</span> - starts application,

<p align="right">(<a href="#top">back to top</a>)</p>


### Risks
* Load testing should be carried out to ensure application runs as expected,
* Improve Error handling checks across all modules,

<p align="right">(<a href="#top">back to top</a>)</p>


### Improvements

* Improve error handling,
* Improve email notification - to handle multiple notification,
* Improve unittest tests

<p align="right">(<a href="#top">back to top</a>)</p>


### Other Updates

* n/a

<p align="right">(<a href="#top">back to top</a>)</p>



## pylint Results

Class | Results | Comments
---|---|---
properties_email.py | Your code has been rated at 10.00/10 | 
properties_server.py | Your code has been rated at 10.00/10 | 
properties_temperature.py | Your code has been rated at 10.00/10 | 
properties_udp.py | Your code has been rated at 0.00/10 | 
generate_email.py | Your code has been rated at 9.50/10 | Too few public methods (1/2) (too-few-public-methods)
generate_logs.py | Your code has been rated at 9.41/10 | Consider using 'sys.exit' instead (consider-using-sys-exit) <br> Formatting a regular string which could be an f-string (consider-using-f-string)
udp_server.py | Your code has been rated at 4.35/10 | Unable to import 'config.properties_udp' (import-error) <br> Unable to import 'config.properties_server' (import-error) <br> Unable to import 'config.properties_temperature' (import-error) <br> Unable to import 'src.reporting.generate_logs' (import-error) <br> Unable to import 'src.alert.generate_email' (import-error) <br> Unused variable 'addr' (unused-variable)
main.py | Your code has been rated at 10.00/10 |

<p align="right">(<a href="#top">back to top</a>)</p>