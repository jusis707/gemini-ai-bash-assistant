# gemini-ai-bash-assistant
<br> Gemini-AI assistant for automation via bash/python and nice prompt/output in any *nix terminal.
<br>Almost 'headless' near 'lazy' installation. With <b>no-selenium</b>, <b>no-chrome-driver</b>, no by-passes or other tricky manipulations.
<br> For complex coding, Gemini offers a clear advantage in accuracy and efficiency, way more excels ChatGPT or DeepSeek.
<br>
<br>This tool has to help with automation, real-time event detection, making it highly effective for log monitoring and system alert generation.
<br>  Requirments:
    Linux or 
    FreeBSD or
    Termux and
    Python
    (will to install some python modules).
<br>Usage:
<br>git clone https://github.com/jusis707/gemini-ai-bash-assistant
<br>cd gemini-ai-bash-assistant
<br> Replace inline <b><i>gemini.py</i></b> with your actual API key -> https://aistudio.google.com/app/apikey
<br>
<br>python3 gemini.py -i 'time in Riga'
<br>python3 gemini.py -i 'President of the USA'
<br>python3 gemini.py -i 'meaning of init 1 in linux'
<br>
<br> More *nix <i>way</i> for grep/automation of output monitoring eg. <i>tail -f</i>:
<br>python3 gemini.py -i 'time in Riga' | tee -a gemini.out
<br>python3 gemini.py -i 'President of the USA' | tee -a gemini.out
<br>python3 gemini.py -i 'meaning of init 1 in linux' | tee -a gemini.out
<br>
<br>Uniqness in output file guaranteed by timestamp in seconds of datetime, appended to each AI response.
<br>

<br>p.s. gemini LLM model named <i><b>flash-2.0</b></i> <i>lives</i> in between of October of 2023 and June of 2024 (28 of March, 2025 as per today, as true date).
<br>
<br><b>Automation:</b>
<br><i> - from terminal (runs in <b>background</b>), before any promt performed:</i>
<br>chmod +x gemini-monitor.sh
<br>bash gemini-monitor.sh
<br><i> - from another terminal open:</i>
<br>python3 gemini.py -post -i 'bash code, create a file, 6 digit time in Riga as filename, file in current folder' | tee -a gemini.out
<br>
<br><b>-post</b> argument passes universal text, of content of file 'post' as appendix for each user prompt to Gemini AI.
<br>
<br><b>gemini-monitor.sh</b> runs in background (optionally, might use '&' or 'nohup') to keep <i>backgrounded</i> and monitors Gemini AI responses - if any code responded, then the code executes and actions will be appended to logfile.
<br>
<br>Reminder:
<br>  If:
<br>  <b>-post</b> argument added
<br>and
<br>  <b>bash gemini-monitor.sh</b> started, then:
<br>  <b>Gemini AI responded <i>code</i> WILL executes locally against your local environment.</b>
<br>
<br>
<b>Automation example:</b>
<br>
<br>nohup bash gemini-monitor.sh &
<br>![screenshot](5.png)
<br>python3 gemini.py -post -i 'bash code, create a folder, named of deepest lake in Latvia, in the current folder' | tee -a gemini.out
<br>![screenshot](6.png)
<br>cat code_execution.log
<br>![screenshot](7.png)
<br>ls
<br>![screenshot](8.png)
<br>
<br>Added Ubuntu .deb package for x86_64/amd64, for easy/lazy installation, <b>at the stage of developing, after deb installation, use folder of the content where this git hub repo cloned</b>.
<br><b>sudo dpkg -i ./gemini-agent_0.1.0-1_amd64.deb</b>
<br>API key asked during installation and saved in <b>config.ini</b> file.
<br>Ubuntu package uninstallation perfomed by:
<br><b>sudo dpkg -r gemini-agent</b>
<br>Ubuntu deb package installation:
<br>![screenshot](4.png)
<br>Ubuntu version with deb file installation runs with:
<br><b>gemini -i 'time in riga'</b>
<br> note the difference between Ubuntu direct run <i>gemini</i> and python way of <i>python3 gemini.py</i>
<br>
<br>Ubuntu (<i>python3</i>) way:
<br>![screenshot](1.png)
<br>
<br> Termux (Android mobile phone - Redmi 7):
<br>![screenshot](2.jpg)
<br>
<br> FreeBSD:
<br>![screenshot](3.png)
